from datetime import date

from pydantic import BaseModel, Field, validator
from pydantic import ValidationError


class Users(BaseModel):
    id: int = Field(..., example=0)
    full_name: str = Field(..., example='Oleg Popov')
    gender: str = Field(..., example='male')
    b_day: date = Field(..., example='1955-12-03')
    address: str = Field(..., example='Krasnoyarsk')

    @validator('gender', pre=True, always=True)
    def check_gender(cls, gender):
        if gender not in ('male', 'female'):
            raise ValidationError('gender must be male or female')
        return gender

    @validator('b_day', always=True)
    def check_b_day(cls, b_day):
        if not isinstance(b_day, date):
            raise ValidationError('b_day should have type date')
        return b_day

    @validator('full_name', pre=True, always=True)
    def check_full_name(cls, full_name):
        if not full_name:
            raise ValidationError('Full name is empty!')
        return full_name

    class Config:
        orm_mode = True


class Phones(BaseModel):
    id: int = Field(..., example=0)
    phone_type: str = Field(..., example="city or mobile")
    number_phone: str = Field(..., example="9998887755")
    owner_id: int = Field(..., example=1)

    @validator('phone_type', pre=True, always=True)
    def check_phone_type(cls, phone_type):
        if phone_type not in ('city', 'mobile'):
            raise ValidationError('phone_type must be city or mobile')
        return phone_type

    @validator('number_phone', pre=True, always=True)
    def check_phone_number(cls, number_phone):
        if len(number_phone) < 10:
            raise ValidationError('number_phone must contains 10 number, Example: 9998887755')
        return number_phone

    class Config:
        orm_mode = True


class Mails(BaseModel):
    id: int = Field(..., example=0)
    mail_type: str = Field(..., example='personal or work')
    mail_address: str = Field(..., example='aaa@mail.ru')
    owner_id: int = Field(..., example=1)

    @validator('mail_type', pre=True, always=True)
    def check_mail_type(cls, mail_type):
        if mail_type not in ('personal', 'work'):
            raise ValidationError('mail_type must be personal or work')
        return mail_type

    @validator('mail_address', pre=True, always=True)
    def check_mail_address(cls, mail_address):
        if '@' not in mail_address:
            raise ValidationError('mail_address must contains @. Example: aaaaaa@mail.ru')
        return mail_address

    class Config:
        orm_mode = True
