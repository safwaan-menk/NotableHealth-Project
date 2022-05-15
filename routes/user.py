from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user.get("/")
async def get_all_users():
    return conn.execute(users.select()).fetchall()

@user.get("/{name}")
async def get_user_by_name(name: str):
    return conn.execute(users.select().where(users.c.name == name)).fetchall()

@user.post("/")
async def add_new_user(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        phone = user.phone
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/{name}")
async def update_existing_user(name: str, user: User):
    conn.execute(users.update().values(
        name = user.name,
        email = user.email,
        phone = user.phone
    ).where(users.c.name == name))
    return conn.execute(users.select()).fetchall()

@user.delete("/{name}}")
async def delete_existing_user(name: str):
    conn.execute(users.delete().where(users.c.name == name))
    return conn.execute(users.select()).fetchall()
