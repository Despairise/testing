from typing import List
from fastapi import FastAPI
import schemas
from db import database, users, phones, mails
import logging
from log.mainlog import main_log

app = FastAPI()


logger = logging.getLogger(__name__)
main_log(logger)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.post('/users', response_model=List[schemas.UserList])
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post('/users/{users_id}', response_model=schemas.UserList)
async def read_user(users_id: int):
    query = users.select().where(users.c.id == users_id)
    return await database.fetch_one(query)


@app.put('/users', response_model=schemas.UserList)
async def create_user(user: schemas.UserCreate):
    query = users.insert().values(
        id=user.id,
        full_name=user.full_name,
        gender=user.gender,
        b_day=user.b_day,
        address=user.address
    )
    logger.warning("user create")
    return await database.execute(query)


@app.patch('/users', response_model=schemas.UserList)
async def update_user(user: schemas.UserUpdate):
    query = users.update(). \
        where(users.c.id == user.id). \
        values(
        full_name=user.full_name,
        gender=user.gender,
        b_day=user.b_day,
        address=user.address
    )
    logger.warning("user add")
    return await database.execute(query)

    return read_user(user.id)


@app.delete('/users/{users_id}')
async def delete_user(user: schemas.UserDelete):
    query = users.delete().where(users.c.id == user.id)
    await database.execute(query)
    logger.warning("user remove")
    return {'user delete'}


@app.post('/phones/', response_model=List[schemas.PhoneList])
async def read_all_phones():
    query = phones.select()
    return await database.fetch_all(query)


@app.post('/phones/{phones_id}', response_model=schemas.PhoneList)
async def read_phone(phones_id: int):
    query = phones.select().where(phones.c.id == phones_id)
    return await database.fetch_one(query)


@app.put('/phones', response_model=schemas.PhoneList)
async def create_phone(phone: schemas.PhoneCreate):
    query = phones.insert().values(
        id=phone.id,
        type=phone.type,
        number_phone=phone.number_phone,
    )
    logger.warning('phone add')
    return await database.execute(query)


@app.patch('/phones', response_model=schemas.PhoneList)
async def update_phone(phone: schemas.PhoneUpdate):
    query = phones.update(). \
        where(phones.c.id == phone.id). \
        values(
        type=phone.type,
        mobile_phone=phone.number_phone
    )
    logger.warning('phone changed')

    return await database.execute(query)

    return read_phone(phone.id)


@app.delete('/phones/{phones_id}')
async def delete_phone(phone: schemas.PhoneDelete):
    query = phones.delete().where(phones.c.id == phone.id)
    await database.execute(query)
    logger.warning("phone remove")
    return {'phone delete'}


@app.post('/mails/', response_model=List[schemas.MailList])
async def read_all_mails():
    query = mails.select()
    return await database.fetch_all(query)


@app.post('/mails/{mails_id}', response_model=schemas.MailList)
async def read_mail(mails_id: int):
    query = mails.select().where(mails.c.id == mails_id)
    return await database.fetch_one(query)


@app.put('/mails', response_model=schemas.MailList)
async def create_mail(mail: schemas.MailCreate):
    query = mails.insert().values(
        id=mail.id,
        type=mail.type,
        mail_address=mail.mail_address,
    )
    logger.warning('mail add')
    return await database.execute(query)


@app.patch('/mails', response_model=schemas.MailList)
async def update_mail(mail: schemas.MailUpdate):
    query = mails.update(). \
        where(mails.c.id == mail.id). \
        values(
        type=mail.type,
        mail_address=mail.mail_address
    )
    logger.warning('mail changed')
    return await database.execute(query)

    return read_mail(mail.id)


@app.delete('/mails/{mails_id}')
async def delete_mail(mail: schemas.MailDelete):
    query = mails.delete().where(mails.c.id == mail.id)
    await database.execute(query)
    logger.warning("mail remove")
    return {'mail delete'}
