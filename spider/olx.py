from math import ceil
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from flata import Query
from tqdm import tqdm

from db.model import Car
from db.model import Poster

"""
with open('t1.json') as f:
    data = json.load(f)
df = pd.json_normalize(data, 'car')
"""


def olx_spider(db, brand=""):
    url = f"https://ce.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{brand}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.122 "
        "Safari/537.36"
    }
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    total = soup.find("span", class_="sc-1mi5vq6-0 eDXljX sc-ifAKCX fhJlIo").text
    total = int(total.split()[4].replace(".", ""))
    pages = ceil(total / 50)

    # print(f"Total posters: {total}, Total pages: {pages}")
    for page in tqdm(range(1, pages + 1), desc=brand.upper()):
        res = requests.get(f"{url}&o={page}", headers=headers)
        s = BeautifulSoup(res.text, "html.parser")

        block = s.find("ul", class_="sc-1fcmfeb-1 kntIvV")
        items = block.find_all("li")
        for item in items:
            if item.find("a"):
                a = item.find("a")
                poster_id = a.get("data-lurker_list_id")
                poster_title = a.get("title")
                poster_link = a.get("href")

                poster_table = db.table("poster")
                search_poster = db.get("poster").search(Query().poster_id == poster_id)
                if search_poster:
                    continue

                req = requests.get(poster_link, headers=headers)
                poster = BeautifulSoup(req.text, "html.parser")

                try:
                    car_features = (
                        poster.find_all("div", class_="sc-bwzfXH h3us20-0 cBfPri")[1]
                        .find("div", class_="duvuxf-0 h3us20-0 jAHFXn")
                        .find("div", class_="h3us20-6 eaygqA")
                        .find_all("div", class_="sc-hmzhuo HlNae sc-jTzLTM iwtnNi")
                    )
                except (AttributeError, IndexError):
                    continue
                try:
                    car_model = car_features[1].find("a").text
                except (AttributeError, IndexError):
                    car_model = None
                try:
                    car_brand = car_features[2].find("a").text
                except (AttributeError, IndexError):
                    car_brand = None
                try:
                    car_category = (
                        car_features[3].find("span", class_="sc-ifAKCX cmFKIN").text
                    )
                except (AttributeError, IndexError):
                    car_category = None
                try:
                    poster_car_year = car_features[4].find("a").text
                except (AttributeError, IndexError):
                    poster_car_year = None
                try:
                    poster_car_mileage = (
                        car_features[5].find("span", class_="sc-ifAKCX cmFKIN").text
                    )
                except (AttributeError, IndexError):
                    poster_car_mileage = None

                car = Car(
                    brand=car_brand,
                    model=car_model,
                    category=car_category,
                )
                car_table = db.table("car")
                search_car = db.get("car").search(Query().model == car.model)
                if search_car:
                    car_id = search_car[0].id
                else:
                    new_car = car_table.insert(car.__dict__)
                    car_id = new_car.get("id")

                try:
                    price = poster.find("h2", class_="sc-ifAKCX eQLrcK").text
                except AttributeError:
                    continue
                poster_price = int(price.split(" ")[1].replace(".", ""))
                poster_info = poster.find(
                    "div", class_="sc-hmzhuo fpFNoN sc-jTzLTM iwtnNi"
                ).find_all("span")
                publish_date = poster_info[0].text
                publish_date = (
                    f"{publish_date.split(' ')[2]} {publish_date.split(' ')[-1]}"
                )
                publish_date = datetime.strptime(publish_date, "%d/%m %H:%M")
                poster_publish_date = publish_date.replace(year=2021)
                poster_professional = True if len(poster_info) > 3 else False
                poster_location = (
                    poster.find_all(
                        "div", class_="sc-hmzhuo sc-1f2ug0x-3 ONRJp sc-jTzLTM iwtnNi"
                    )[1]
                    .find("dd")
                    .text
                )

                poster = Poster(
                    poster_id=poster_id,
                    car_id=car_id,
                    car_mileage=poster_car_mileage,
                    car_year=poster_car_year,
                    title=poster_title,
                    price=poster_price,
                    publish_date=poster_publish_date.isoformat(),
                    location=poster_location,
                    professional=poster_professional,
                    link=poster_link,
                )
                poster_table.insert(poster.__dict__)
