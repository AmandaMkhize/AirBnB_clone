#!/usr/bin/python3

""" Defines User module in AirBnb project """
from models.base_model import BaseModel


class User(BaseModel):
    """ class defines a user by various attributes """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
