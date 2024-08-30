from fastapi import FastAPI
import pickle


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the version 1.0 of Ride Canselation Prediction service!"}

@app.post("/gradient_boosting_cls")
async def gbc_predict(a, b, c, d):
    return {"class": 0, "info":"Class 1 means the ride canselation is probable!"}
