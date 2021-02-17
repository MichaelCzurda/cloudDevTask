from fastapi import FastAPI, Header, Security, HTTPException, Depends
from pydantic import BaseModel

from typing import List, Optional

from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN, HTTP_406_NOT_ACCEPTABLE
#Request Model
class Item(BaseModel):
    values: List[int]

#Key
API_KEY = "1234567890123456789012345678901234567890"
API_KEY_NAME = "secret"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
#Checking for KEy in order query > header


#Startin FastAPI
app = FastAPI()

async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header)):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )


@app.post('/task1/')
async def return_ordered(item:Item, api_key: APIKey = Depends(get_api_key)):
    if all(isinstance(value, int) for value in item.values):
        print(sorted(item.values, key=int, reverse= True))
        return sorted(item.values, key=int, reverse= True)
    else:
        raise HTTPException(
        status_code=HTTP_406_NOT_ACCEPTABLE, detail="Not all elements in values are from type integer"
    )