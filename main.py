from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, LargeBinary
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Создаем экземпляр FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите разрешенные домены (лучше уточнить на продакшене)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Устанавливаем соединение с базой данных SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Определяем модель данных для хранения в базе данных
files = Table(
    "files",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("data", LargeBinary),
)

# Создаем таблицы в базе данных
metadata.create_all(bind=engine)

# Создаем сессию базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Модель данных для приема данных от клиента
class ItemIn(BaseModel):
    data: str

# Роут для приема данных от скрипта
@app.post("/api/data", response_model=dict)
def receive_data(item: ItemIn):
    data = item.data

    # Сохраняем данные в базу данных
    db = SessionLocal()
    try:
        db.execute(files.insert().values(data=data))
        db.commit()
    finally:
        db.close()

    # Возвращаем успешный JSON-ответ
    return {"message": "Data received successfully", "data": data}

# Роут для получения данных из базы
@app.get("/api/data/{item_id}", response_model=dict)
def get_data(item_id: int):
    db = SessionLocal()

    try:
        query = files.select().where(files.c.id == item_id)
        result = db.execute(query).fetchone()

        if result:
            data = result["data"]
            return {"message": "Data retrieved successfully", "data": data}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    finally:
        db.close()

# Запуск сервера с использованием Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)