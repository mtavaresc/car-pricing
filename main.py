from datetime import datetime

from flata import Flata
from flata import JSONStorage
from twiggy import quick_setup

from spider.olx import olx_spider


def search_brands(brands_file):
    with open(brands_file, 'r') as f:
        content = f.readlines()
    return [line.replace('\n', '') for line in content]


quick_setup(file='log/olx.log')
if __name__ == "__main__":
    begin = datetime.now().replace(microsecond=0)

    _db = Flata("db/t1.json", storage=JSONStorage)

    brands = search_brands('brands.txt')
    for brand in brands:
        olx_spider(_db, brand=brand.replace(" ", "").lower())

    end = datetime.now().replace(microsecond=0)
    print(f"\n\n**********")
    print(f"Begin: {begin}")
    print(f"End: {end}")
    print(f"Elapsed time: {end - begin}")
