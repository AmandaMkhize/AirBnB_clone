#!/usr/bin/python3
""" Defines City module for AirBnB """


from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
