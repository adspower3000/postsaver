from contextlib import asynccontextmanager
import uvicorn

from fastapi import FastAPI
from database import create_tables
#delete_tables
from fastapi.middleware.cors import CORSMiddleware

from router import router as tasks_router



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    # await delete_tables()
    # print("База очищена")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)