from fastapi import APIRouter
from apis.version1 import route_users, route_patients

api_router = APIRouter()

api_router.include_router(route_users.router, prefix='/v1/users', tags=["users"])
api_router.include_router(route_patients.router, prefix='/v1/patients', tags=["patients"])
