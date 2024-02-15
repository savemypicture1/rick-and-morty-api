from pydantic import BaseModel, AnyUrl
from typing import Union


class InfoSchema(BaseModel):
    count: int
    next: Union[AnyUrl, None]
    pages: int
    prev: Union[AnyUrl, None]
