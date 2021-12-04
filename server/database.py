import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("users_collection")
product_collection = database.get_collection("products_collection")


# helpers

def user_helper(user) -> dict:
    return {
        "id": str(["_id"]),
        "FirstName": user["FirstName"],
        "LastName": user["LastName"],
        "email": user["email"],
        "national_id": user["national_id"],
    }


def product_helper(product) -> dict:
    return {
        "id": str(["_id"]),
        "name": product["name"],
        "price": product["price"],
        "description": product["description"]
    }


# operators for users
# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True


# oprators for products
async def retrieve_products():
    products = []
    async for product in product_collection.find():
        products.append(user_helper(product))
    return products


# Add a new product into to the database
async def add_product(product_data: dict) -> dict:
    product = await product_collection.insert_one(product_data)
    new_product = await product_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)


# Retrieve a product with a matching ID
async def retrieve_product(id: str) -> dict:
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)


# Update a product with a matching ID
async def update_product(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        updated_product = await product_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_product:
            return True
        return False


# Delete a product from the database
async def delete_product(id: str):
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        await product_collection.delete_one({"_id": ObjectId(id)})
        return True
