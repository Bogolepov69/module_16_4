from fastapi import FastAPI, HTTPException
from starlette import status
from pydantic import BaseModel

app = FastAPI()
users = {}

class Users(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    next_id = str(int(max(users.keys(), default="0")) + 1)
    users[next_id] = f"Имя: {username}, возраст: {age}"
    return f"User {next_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id in users:
        user_data = users.pop(user_id)
        return f"The user {user_id} has been deleted"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")