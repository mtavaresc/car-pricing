class Car(object):
    def __init__(
            self,
            brand,
            model,
            car_body,
            fuel_type=None,
            aspiration=None,
            door_number=None,
            drive_wheel=None
    ):
        self.brand = brand
        self.model = model
        self.car_body = car_body
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.door_number = door_number
        self.drive_wheel = drive_wheel


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
