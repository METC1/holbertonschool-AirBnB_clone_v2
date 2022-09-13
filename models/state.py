#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel):
    '''
    class State that inherets from BaseModel
    '''
    name=""

    @property
    def cities(self):
        from models import storage
        all_cities = storage.all(City).values()

        new_list = []
        for city in all_cities:
            if (city.state_id == self.id):
                new_list.append(city)
        return (new_list)
