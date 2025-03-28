# Packages and imports
import numpy as np

# Defines the Aircraft class
class Aircraft:
    def __init__(self):
        self.passengers = 72
        self.total_length = 27.17  # in meters
        self.total_height = 7.65  # in meters
        self.wingspan = 27.05  # in meters
        self.wing_area = 61  # in square meters
        self.aspect_ratio = 12
        self.cabin_width = 2.57  # in meters
        self.mtow = 23000  # in kilograms
        self.oew = 13600  # in kilograms
        self.payload = 7400  # in kilograms
        self.max_fuel = 5000  # in kilograms
        self.cruise_speed = 510  # in km/h
        self.max_range = 1404  # in kilometers
        self.takeoff_length = 1279  # in meters
        self.landing_length = 915  # in meters
        self.mzfw = 21000  # in kilograms
        self.mlw = 22350  # in kilograms
        self.climb_speed = 170  # in knots
        self.max_cruise_speed = 500  # in km/h (95% MTOW - ISA - FL240)
        self.fuel_consumption_cruise = 650  # in kg/h (95% MTOW - ISA - FL240)
        self.one_engine_out_ceiling = 2987  # in meters (95% MTOW - ISA +10)
        self.range_max_pax = 1370  # in kilometers (long-range cruise speed)
        self.co2_per_seat_km = 69  # in grams
        self.takeoff_field_length = 1315  # in meters (@ MTOW - ISA - Sea Level)
