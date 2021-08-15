from datetime import datetime

from flata import Flata
from flata import JSONStorage

from spider.olx import olx_spider

if __name__ == "__main__":
    begin = datetime.now().replace(microsecond=0)

    _db = Flata("db/t1.json", storage=JSONStorage)
    brands = [
        "AUDI",
        "BMW",
        "CHERY",
        "CITROEN",
        "DODGE",
        "FIAT",
        "FORD",
        "GM - CHEVROLET",
        "GURGEL",
        "HONDA",
        "HYUNDAI",
        "JAC",
        "JEEP",
        "KIA MOTORS",
        "LAND ROVER",
        "MAZDA",
        "MERCEDES-BENZ",
        "MITSUBISHI",
        "NISSAN",
        "PEUGEOT",
        "PORSCHE",
        "RENAULT",
        "SUZUKI",
        "TOYOTA",
        "TROLLER",
        "VOLVO",
        "VW - VOLKSWAGEN",
    ]
    for brand in brands:
        olx_spider(_db, brand=brand.replace(" ", "").lower())

    end = datetime.now().replace(microsecond=0)
    print(f"\n\n**********")
    print(f"Elapsed time: {end - begin}")
