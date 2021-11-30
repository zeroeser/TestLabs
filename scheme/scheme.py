from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

import re


# Creating user
class User(BaseModel):
    id: Optional[int]
    name: str
    patronymic: Optional[str] = None
    surname: str
    email: EmailStr
    password: str
    when: Optional[datetime]
    update: datetime

    @validator("password")
    def password_check(cls, password, **kwargs):
        if re.search('(?=.*[A-Z])(?=.*\d)(?=.{6}).*', password) is None:
            raise ValueError("Пароль не соотвествует")
        return password

    @validator("name")
    def name_check(cls, name, **kwargs):
        if not all(char.isalpha() for char in name):
            raise ValueError("Имя должно быть заполнено")
        return name

    @validator("surname")
    def surname_check(cls, surname, **kwargs):
        if not all(char.isalpha() for char in surname):
            raise ValueError("Фамилия должна быть заполнена")
        return surname
