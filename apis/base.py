from fastapi import APIRouter
from apis.version1 import route_users, route_patients, route_pharmacies, route_transactions, route_login

api_router = APIRouter()

api_router.include_router(route_users.router, prefix='/v1/users', tags=["users"])
api_router.include_router(route_login.router, prefix='/v1/login', tags=["login"])

api_router.include_router(route_patients.router, prefix='/v1/patients', tags=["patients"])
api_router.include_router(route_pharmacies.router, prefix='/v1/pharmacies', tags=["pharmacies"])
api_router.include_router(route_transactions.router, prefix='/v1/transactions', tags=["transactions"])
