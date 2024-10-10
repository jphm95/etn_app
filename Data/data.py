
class Data:

    @staticmethod
    def get_trip_data():
        return {
            "origin_city": "Aguascalientes",
            "destination_city": "Guadalajara",
            "depart_month": "Octubre",
            "return_month": "Octubre",
            "depart_day": "10",
            "return_day": "17"
        }

    @staticmethod
    def get_seat_number():
        return {
            "departure_seat": "1",
            "return_seat": "5"
        }


    @staticmethod
    def get_payment_data():
        return {
            "card_name": "Juan PHM",
            "card_number": "4567098712341234",
            "expiration_month": "05",
            "expiration_year": "2028",
            "cvv": "987",
        }


    @staticmethod
    def get_passenger_data():
        return {
            "name": "Juanaa",
            "last_name_one": "Pabloo",
            "last_name_two": " HerMO",
            "email": "johnpaul@gmail.com",
            "phone": "4499067144",
            "birthday": "02061995",
            "tariff": "Adulto"

        }
    @staticmethod
    def get_user_data():
        return {
            "user": "jphm",
            "password": "Abc012"
        }
