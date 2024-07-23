from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description":"Not found"}}
)