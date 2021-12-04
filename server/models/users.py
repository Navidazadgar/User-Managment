from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional


class UsersModel(BaseModel):
    username: str
    FirstName: str = Field(...)
    LastName: str = Field(...)
    email: EmailStr = Field(...)
    password: str
    national_id: str

    class Config:
        schema_extra = {
            "example": {
                "username": "navidaz",
                "FirstName": "Navid",
                "LastName": "Azadgar",
                "email": "navidazadgar@gmail.com",
                "password": "asdgajkh",
                "national_id": "0014409437",
            }
        }

    @validator('national_id')
    def IdValidator(cls, value):
        if len(value) == 10:
            k = 10
            Sum = 0
            for i in range(0, 9):
                x = (k - i) * int(value[i])
                Sum = Sum + x
                y = Sum % 11
            if y == 0:
                if int(value[9]) != 0:
                    raise ValueError("National-ID is incorrect")
                else:
                    return value
            if y == 1:
                if int(value[9]) != 1:
                    raise ValueError("National-ID is incorrect")
                else:
                    return value
            if y != 1 and y != 0:
                if int(value[9]) != 11 - y:
                    raise ValueError("National-ID is incorrect")
                else:
                    return value
        else:
            raise ValueError("National-ID must be 10 character")


class UpdateUserModel(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    email: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "FirstName": "Navid",
                "LastName": "Azadgar",
                "email": "navidazadgar@gmail.com",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
