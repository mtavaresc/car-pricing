import pandas as pd
import json


with open('db/t1.json') as f:
    data = json.load(f)

pd.json_normalize(data, 'car').to_csv('dataset/car.csv')
pd.json_normalize(data, 'poster').to_csv('dataset/poster.csv')
