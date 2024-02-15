from pydantic import BaseModel, AnyUrl
from datetime import datetime
from typing import List, Union


class Origin(BaseModel):
    name: str
    url: Union[AnyUrl, str]


class Location(BaseModel):
    name: str
    url: Union[AnyUrl, str]


class CharacterSchema(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: Origin
    location: Location
    image: str
    episode: List[AnyUrl]
    url: AnyUrl
    created: datetime
