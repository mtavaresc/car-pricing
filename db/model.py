class Car(object):
    def __init__(
            self,
            brand,
            model,
            category
    ):
        self.brand = brand
        self.model = model
        self.category = category


class Poster(object):
    def __init__(
            self,
            poster_id,
            car_id,
            car_mileage,
            car_year,
            title,
            price,
            publish_date,
            location,
            professional,
            link
    ):
        self.poster_id = poster_id
        self.car_id = car_id
        self.car_mileage = car_mileage
        self.car_year = car_year
        self.title = title
        self.price = price
        self.publish_date = publish_date
        self.location = location
        self.professional = professional
        self.link = link
