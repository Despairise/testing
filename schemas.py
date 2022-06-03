from pydantic import BaseModel, Field


class UserList(BaseModel):
    id: int
    full_name: str
    gender: str
    b_day: str
    address: str


class UserCreate(BaseModel):
    id: int = Field(..., example=1)
    full_name: str = Field(..., example='Oleg Popov')
    gender: str = Field(..., example='male')
    b_day: str = Field(..., example='1955.21.03')
    address: str = Field(..., example='Krasnoyarsk')


class UserUpdate(BaseModel):
    id: int = Field(..., example="enter id")
    full_name: str = Field(..., example='')
    gender: str = Field(..., example='')
    b_day: str = Field(..., example='')
    address: str = Field(..., example='')


class UserDelete(BaseModel):
    id: int = Field(..., example=1)


class PhoneList(BaseModel):
    id: int
    type: str
    number_phone: str


class PhoneCreate(BaseModel):
    id: int = Field(..., example=1)
    type: str = Field(..., example="enter type")
    number_phone: str = Field(..., example="enter number phone")


class PhoneUpdate(BaseModel):
    id: int = Field(..., example="enter id")
    type: str = Field(..., example='')
    number_phone: str = Field(..., example='')


class PhoneDelete(BaseModel):
    id: int = Field(..., example=1)


class MailList(BaseModel):
    id: int
    type: str
    mail_address: str


class MailCreate(BaseModel):
    id: int = Field(..., example=1)
    type: str = Field(..., example="enter type")
    mail_address: str = Field(..., example="enter mail")


class MailUpdate(BaseModel):
    id: int = Field(..., example="enter id")
    type: str = Field(..., example='')
    mail_address: str = Field(..., example='')


class MailDelete(BaseModel):
    id: int = Field(..., example=1)
