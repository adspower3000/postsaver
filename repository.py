from sqlalchemy import select, desc
from database import TaskOrm, new_session
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)

            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_tasks(cls) -> STask:
        async with new_session() as session:
            query = select(TaskOrm).order_by(desc(TaskOrm.id))
            result = await session.execute(query)
            task_model = result.scalar()
            task = STask.model_validate(task_model)
            return task
