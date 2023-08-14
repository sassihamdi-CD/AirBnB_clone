#!/usr/bin/python3
'''this hold the entire Amenity class'''
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Representing the Amenity model'''
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        '''initializing the Amenity class'''
        super().__init__(*args, **kwargs)
