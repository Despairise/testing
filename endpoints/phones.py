from typing import List

from fastapi import APIRouter

from db import phones, database
from log import logger
from schemas import Phones

p_router = APIRouter()


@p_router.post('/phones/', response_model=List[Phones])
async def read_all_phones():
    query = phones.select()
    return await database.fetch_all(query)


@p_router.post('/phones/{phones_id}', response_model=Phones)
async def read_phone(phones_id: int):
    query = phones.select().where(phones.c.id == phones_id)
    return await database.fetch_one(query)


@p_router.put('/phones', response_model=Phones)
async def create_phone(phone: Phones):
    query = phones.insert().values(
        phone_type=phone.phone_type,
        number_phone=phone.number_phone,
        owner_id=phone.owner_id
    )
    logger.info('phone add')
    phone.id = await database.execute(query)
    return phone


@p_router.patch('/phones/{phones_id}', response_model=Phones)
async def update_phone(phone_id: int, phone: Phones):
    query = phones.update(). \
        where(phones.c.id == phone.id). \
        values(
        phone_type=phone.phone_type,
        number_phone=phone.number_phone,
        owner_id=phone.owner_id
    )
    logger.info('phone changed')
    await database.execute(query)
    return phone


@p_router.delete('/phones/{phones_id}')
async def delete_phone(phone_id: int):
    query = phones.delete().where(phones.c.id == phone_id)
    await database.execute(query)
    logger.info("phone remove")
    return {'phone delete'}
