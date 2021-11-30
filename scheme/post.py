from scheme.users import UserRepository
from db.models import URL
from databases import Database
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from scheme.scheme import User

db = Database(URL)

router = APIRouter()


def get_user_repository() -> UserRepository:
    return UserRepository(db)


@router.get("/", response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 0):
    return await users.get_all(limit=limit, skip=0)


@router.get("/id", response_model=User)
async def read_users(id: int, users: UserRepository = Depends(get_user_repository)):
    return await users.get_by_id(id=id)


@router.get("/email", response_model=User)
async def read_users(email: str, users: UserRepository = Depends(get_user_repository)):
    return await users.get_by_email(email=email)


@router.post("/", response_model=User)
async def create_user(
    user: User,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=User)
async def update_user(id: int, user: User,  users: User = Depends(get_user_repository)):
    old_user = await users.get_by_id(id=id)
    if old_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)


@router.delete("/")
async def delete_user(id: int, users: User = Depends(get_user_repository)):
    user = await users.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден")
    if user is None:
        raise not_found_exception
    await users.delete(id=id)
    return {"status": True}







