from pydantic import BaseModel, Field


class Products(BaseModel):
    name: str
    price: int
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "galaxy s20",
                "price": "240000000",
                "description": "This is for DibaTech",
            }
        }


class UpdateProductModel(BaseModel):
    name: str
    price: int
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "galaxy s20",
                "price": "240000000",
                "description": "This is for DibaTech",
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
