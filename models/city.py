ity Module for HBNB project """
# Imports the Base Model Class
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

