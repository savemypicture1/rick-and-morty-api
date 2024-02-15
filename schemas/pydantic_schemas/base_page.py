from pydantic import BaseModel, AnyUrl


class BasePageSchema(BaseModel):
    characters: AnyUrl
    locations: AnyUrl
    episodes: AnyUrl
