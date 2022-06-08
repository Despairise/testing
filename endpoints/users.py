from typing import List

from fastapi import APIRouter

from db import users, database
from log import logger
from schemas import Users

u_router = APIRouter()


@u_router.post('/users', response_model=List[Users])
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@u_router.post('/users/{users_id}', response_model=Users)
async def read_user(users_id: int):
    query = users.select().where(users.c.id == users_id)
    return await database.fetch_one(query)


@u_router.put('/users', response_model=Users)
async def create_user(user: Users):
    query = users.insert().values(
        full_name=user.full_name,
        gender=user.gender,
        b_day=user.b_day,
        address=user.address
    )
    logger.info("user create")
    user.id = await database.execute(query)
    return user


@u_router.patch('/users/{user_id}', response_model=Users)
async def update_user(user_id: int, user: Users):
    query = users.update(). \
        where(users.c.id == user_id). \
        values(
        full_name=user.full_name,
        gender=user.gender,
        b_day=user.b_day,
        address=user.address
    )
    logger.info("user update")
    await database.execute(query)
    return user


@u_router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    logger.info("user remove")
    return {'user delete'}
