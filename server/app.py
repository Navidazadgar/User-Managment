from fastapi import FastAPI
from server.routes.users import router as UserRouter
from server.routes.products import router as ProductRouter

app = FastAPI()
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(ProductRouter, tags=["Product"], prefix="/product")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to DibaTech"}
