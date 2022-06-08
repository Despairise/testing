from typing import List

from fastapi import APIRouter

from db import mails, database
from log import logger
from schemas import Mails

m_router = APIRouter()


@m_router.post('/mails/', response_model=List[Mails])
async def read_all_mails():
    query = mails.select()
    return await database.fetch_all(query)


@m_router.post('/mails/{mails_id}', response_model=Mails)
async def read_mail(mails_id: int):
    query = mails.select().where(mails.c.id == mails_id)
    return await database.fetch_one(query)


@m_router.put('/mails', response_model=Mails)
async def create_mail(mail: Mails):
    query = mails.insert().values(
        mail_type=mail.mail_type,
        mail_address=mail.mail_address,
        owner_id=mail.owner_id
    )
    logger.info('mail add')

    mail.id = await database.execute(query)
    return mail


@m_router.patch('/mails/{mails_id}', response_model=Mails)
async def update_mail(mail_id: int, mail: Mails):
    query = mails.update(). \
        where(mails.c.id == mail.id). \
        values(
        mail_type=mail.mail_type,
        mail_address=mail.mail_address,
        owner_id=mail.owner_id
    )
    logger.info('mail changed')
    await database.execute(query)
    return mail


@m_router.delete('/mails/{mails_id}')
async def delete_mail(mails_id: int):
    query = mails.delete().where(mails.c.id == mails_id)
    await database.execute(query)
    logger.info("mail remove")
    return {'mail delete'}
