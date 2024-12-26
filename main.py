import uvicorn
from fastapi import FastAPI
from routers import router_car,router_comment,router_user

app = FastAPI()
app.include_router(router_car)
app.include_router(router_comment)
app.include_router(router_user)


if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000,reload=True) #хост и порт для докера
    # uvicorn это ASGI-сервер нужен для запуска FastAPI приложений (что бы не писать каждый раз "uvicorn main:app --reload" в консоли а использовать обычный python main.py так удобнее будет для запуска в контейнере)

