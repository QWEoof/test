import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str


users = []


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/create_user", response_model=User, status_code=201)
async def create_user(user: User):
    user["id"] = len(users) + 1
    users.append(user)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
