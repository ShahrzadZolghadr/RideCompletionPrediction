from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.ensemble import GradientBoostingClassifier


class FeaturesIn(BaseModel):
    C_Income: int
    C_UID: int
    Destination: int
    C_Time:int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the version 1.0 of Ride Canselation Prediction service!"}

@app.post("/gradient_boosting_cls")
async def gbc_predict(features: FeaturesIn):

    with open("app/gbc.pkl", "rb") as f:
        clf = pickle.load(f)

    prediction = clf.predict([[features.C_UID, features.Destination, features.C_Time, features.C_Income]])[0]
    return {"class": str(prediction), "info":"Class 1 means the ride canselation is probable!"}
