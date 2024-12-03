from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle 
import pandas as pd

from fastapi.encoders import jsonable_encoder
from sklearn.preprocessing import OneHotEncoder ,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

PATH = 'https://raw.githubusercontent.com/Murcha1990/MLDS_ML_2022/main/Hometasks/HT1/cars_test.csv'

def process_dataset(df):
    df = df.drop(columns=['name', 'torque', 'selling_price'], errors='ignore')
    df['mileage'] = df['mileage'].astype(str).str.replace(' kmpl', '', regex=False)
    df['mileage'] = df['mileage'].astype(str).str.replace(' km/kg', '', regex=False).astype(float)
    df['engine'] = df['engine'].astype(str).str.replace(' CC', '', regex=False).astype(float)
    df['max_power'] = df['max_power'].astype(str).str.replace('1 bhp', ' bhp', regex=False)
    df['max_power'] = df['max_power'].astype(str).str.replace(' bhp', '', regex=False).astype(float)
    df['engine'] = df['engine'].fillna(0).astype(int)
    df['seats'] = df['seats'].fillna(0).astype(int)
    return df


app = FastAPI()


class Item(BaseModel):
    name: str
    year: int
    selling_price: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str
    engine: str
    max_power: str
    torque: str
    seats: float

class selling_price(Item):
    prediction: float

class Items(BaseModel):
    objects: List[Item]

def pydantic_model_to_df(model_instance):
    x_df = pd.DataFrame([jsonable_encoder(model_instance)])
    pred = process_dataset(x_df)
    return pd.DataFrame(pred)

@app.post("/predict_item")
def predict_item(item: Item) -> dict:
    with open("./piper.pkl", 'rb') as model_file:
        piper = pickle.load(model_file)
    df_instance = pydantic_model_to_df(item)
    res = piper.predict(df_instance).tolist()[0]
    return {"prediction": res}


@app.post("/predict_items")
def predict_items(items: List[Item]) -> List[dict]:
    predictions = list()
    for item in items:
        predictions.append(predict_item(item))
    return predictions
