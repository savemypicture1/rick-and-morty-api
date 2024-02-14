import requests
import pytest
from jsonschema import validate
from schemas.base_page_schema import BASE_PAGE_SCHEMA
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA


# ENDPOINT: LOCATION