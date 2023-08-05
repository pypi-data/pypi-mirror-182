#!/usr/bin/env python3
from fastapi import FastAPI
import uvicorn
import codefast as cf 
from texthandler.apps.model import predict

app = FastAPI()


@app.post("/")
async def apiserver(payload: dict):
    text = payload['text']
    result = predict(text)
    msg = {'hint':'Telegram text handler prediction', 'text': text, 'result': result}
    cf.info(msg)
    return {'label': result}

def texthandle():
    uvicorn.run(app, host="0.0.0.0", port=5000)
    