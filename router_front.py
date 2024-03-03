from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from router import get_tasks

router = APIRouter(
    prefix='/pages',
    tags=['Фронтенд'],
)

templates = Jinja2Templates(directory='templates')


@router.get('/last_code')
async def get_last_code(
        request: Request,
        code=Depends(get_tasks)
):
    return templates.TemplateResponse(
        name='last_code.html',
        context={
            'request': request,
            'last_code': code,
        },
    )


