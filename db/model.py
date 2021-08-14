class Car(object):
    def __init__(
            self,
            brand,
            model,
            mileage,
            category,
            year,
    ):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.category = category
        self.year = year


class Poster(object):
    def __init__(
            self,
            poster_id,
            car_id,
            title,
            price,
            publish_date,
            location,
            professional,
            link
    ):
        self.poster_id = poster_id
        self.car_id = car_id
        self.title = title
        self.price = price
        self.publish_date = publish_date
        self.location = location
        self.professional = professional
        self.link = link
