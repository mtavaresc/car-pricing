import json
from datetime import datetime

import pandas as pd
from flata import Flata
from flata import JSONStorage
from twiggy import quick_setup

from spider.olx import olx_spider


def search_brands(brands_file):
    with open(brands_file, 'r') as f:
        content = f.readlines()
    return [line.replace('\n', '') for line in content]


def json_normalize_to_df():
    with open('db/t1.json') as f:
        data = json.load(f)

    pd.json_normalize(data, 'car').to_csv("./dataset/car.csv")
    pd.json_normalize(data, 'poster').to_csv("./dataset/poster.csv")


quick_setup(file='log/olx.log')
if __name__ == "__main__":
    begin = datetime.now().replace(microsecond=0)

    _db = Flata("db/t1.json", storage=JSONStorage)

    brands = search_brands('brands.txt')
    b = 1
    t = len(brands)
    news = 0

    for brand in brands:
        print(f"{b}/{t}")
        news += olx_spider(_db, brand=brand.replace(" ", "").lower())
        b += 1

    print(f"> Total New Posters: {news}")
    json_normalize_to_df()
    end = datetime.now().replace(microsecond=0)
    print(f"\n\n**********")
    print(f"Begin: {begin}")
    print(f"End: {end}")
    print(f"Elapsed time: {end - begin}")
