from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from router import get_tasks
from router import get_tasks_by_id

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


@router.get('/code_by_id/{code_id}')
async def get_code_by_id(
        request: Request,
        code_id: int,
        code=Depends(get_tasks_by_id)
):
    return templates.TemplateResponse(
        name='code_by_id.html',
        context={
            'code_id': code_id,
            'request': request,
            'code_by_id': code,
        },
    )