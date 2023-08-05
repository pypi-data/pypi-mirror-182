#!/usr/bin/env python3
from premium.utils import cf_unless_tmp
from sklearn.preprocessing import LabelEncoder
import re
from typing import Callable, Dict, List, Optional, Set, Tuple, Union
import pickle

import codefast as cf
import numpy as np
import pandas as pd
import torch
from rich import print
from torch import nn


class Memo(object):
    model_path = '/tmp/text_handler_pytorch_model.pth'
    label_encoder_path = '/tmp/text_handler_label_encoder.pkl'


class LinearModel(nn.Module):

    def __init__(self, input_dim: int, output_dim: int):
        super(LinearModel, self).__init__()
        self.inp = nn.Linear(input_dim, 128)
        self.hidden = nn.Linear(128, 128)
        self.out = nn.Linear(128, output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.inp(x)
        x = self.relu(x)
        x = self.hidden(x)
        x = self.relu(x)
        x = self.out(x)
        return x

    def get_loss(self, x, y):
        y_pred = self.forward(x)
        return nn.BCELoss()(y_pred, y)

    def predict(self, x):
        return self.forward(x)


class FeatureEngineer(object):

    def is_start_with_twitter(self, text: str) -> bool:
        return text.startswith('https://twitter.com')

    def is_twitter_status(self, text: str) -> bool:
        return re.search('https://twitter.com/\w+/status/\d+',
                         text) is not None

    def is_avatar(self, text: str) -> bool:
        return text.lower() in ['avatar']

    def is_start_with_oncemessage(self, text: str) -> bool:
        return text.lower().startswith(
            ('oncemessage', 'oncemsg', 'onemessage', 'onemsg'))

    def is_oncessmage_format(self, text: str) -> bool:
        texts = text.split(' ')
        return len(texts) >= 3 and re.search('\d+', texts[1]) is not None

    def is_contains_weather(self, text: str) -> bool:
        lt = text.lower()
        return lt.startswith('weather')

    def is_question(self, text: str) -> bool:
        return text.lower().startswith(
            ('how is', 'what is', "what's", "how's"))

    def is_youtube(self, text: str) -> bool:
        return text.lower().startswith('https://www.youtube.com/watch?v=')

    def is_youtube_short(self, text: str) -> bool:
        return text.lower().startswith('https://youtu.be/')

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        for func in dir(self):
            if func.startswith('is_'):
                df[func] = df['text'].apply(getattr(self, func))
        df.drop('text', axis=1, inplace=True)
        df = df.astype('int')
        return df


def get_data() -> Tuple:
    data = cf.io.read('projects/bot_train.csv')[1:]
    data = [d.split(',', 1) for d in data]
    df = pd.DataFrame(data, columns=['label', 'text'])
    fe = FeatureEngineer()
    le = LabelEncoder()
    y = le.fit_transform(df['label'])
    X = fe.process(df[['text']])
    X = torch.FloatTensor(X.values)
    y = torch.LongTensor(y)
    return X, y, fe, le


def train():
    X, y, fe, le = get_data()
    model = LinearModel(input_dim=9, output_dim=5)
    epochs = 100
    learning_rate = 0.01
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    train_accuracies = np.zeros(epochs)
    train_losses = np.zeros(epochs)

    for epoch in range(epochs):
        optimizer.zero_grad()
        y_preds = model(X)

        loss_train = criterion(y_preds, y)
        loss_train.backward()
        optimizer.step()

        acc = (y_preds.argmax(1) == y).float().mean()
        train_accuracies[epoch] = acc
        train_losses[epoch] = loss_train
        if epoch % 10 == 0:
            cf.info('Epoch {:<2}, Loss {:<.4f}, Accuracy {:<.4f}'.format(
                epoch, loss_train, acc))
    torch.save(model.state_dict(), Memo.model_path)
    pickle.dump(le, open(Memo.label_encoder_path, 'wb'))
    return model


def predict(x: str):
    for path_ in [Memo.label_encoder_path, Memo.model_path]:
        path_ = path_.replace('/tmp/', '')
        cf_unless_tmp(path_)

    model = LinearModel(input_dim=9, output_dim=5)
    model.load_state_dict(torch.load(Memo.model_path))
    fe = FeatureEngineer()
    le = pickle.load(open(Memo.label_encoder_path, 'rb'))
    df = pd.DataFrame([x], columns=['text'])
    X = fe.process(df)
    X = torch.FloatTensor(X.values)
    y_preds = model(X)

    return le.inverse_transform(y_preds.argmax(1).numpy())[0]
