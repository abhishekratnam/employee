from fastapi import APIRouter
from api.employee import employee

router = APIRouter()
router.include_router(employee.router)
