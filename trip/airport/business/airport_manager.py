import math
import os
from decimal import Decimal

from airport.business.airport_errors import AirportNotFoundError, InternalError
from airport.business.file_manager import FileManager
from trip.settings import BASE_DIR


class AirportManager:
    def __init__(self):
        self.delimiter = ','
        file_name = 'airport_lat_long.txt'
        self.info_file = FileManager(file_name, os.path.join(BASE_DIR, 'airport', 'input'))

    def load_all(self):
        row = self.info_file.load_column(',', 0)
        return row

    def load_by_iata(self, code):
        return self.info_file.search_for_row(r"^{},.*".format(code))

    def compute_distance(self, first_airport_code, second_airport_code):
        second_airport = self.load_by_iata(first_airport_code)
        first_airport = self.load_by_iata(second_airport_code)
        if first_airport and second_airport:
            try:
                first_latitude, first_longitude = self.get_coordinates(first_airport)
                second_latitude, second_longitude = self.get_coordinates(second_airport)
                distance = self.calculate_distance(first_latitude, first_longitude,
                                                   second_latitude,
                                                   second_longitude)
                return distance
            except ValueError:
                print("Could not fetch coordinates for airport")
                raise InternalError("Could not fetch coordinates for airport")
        else:
            print("Airport not found")
            raise AirportNotFoundError("Airport not found")

    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        r = 6371e3

        lat_diff = lat2 - lat1
        lon_diff = lon2 - lon1

        a = math.pow(math.sin(lat_diff / 2), 2) + \
            math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(lon_diff / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = r * c

        distance_in_kilometer = round(d / 1000, 3)
        return distance_in_kilometer

    def get_coordinates(self, data):
        return [Decimal(d) for d in data.split(self.delimiter)[1:]]
