#!/usr/bin/python3

""" Defines Review module for AirBnB """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for storing review information """
    place_id = ""
    user_id = ""
    text = ""
