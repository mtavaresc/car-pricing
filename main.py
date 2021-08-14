from datetime import datetime

from flata import Flata
from flata import JSONStorage

from spider.olx import olx_spider

if __name__ == "__main__":
    begin = datetime.now().replace(microsecond=0)

    _db = Flata("db/t1.json", storage=JSONStorage)
    olx_spider(_db)

    end = datetime.now().replace(microsecond=0)
    print(f"\n\n**********")
    print(f"Elapsed time: {end - begin}")
