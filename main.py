from fastapi import FastAPI
from database import create_db_and_tables
from routers.advertising import router as advertising_router
from routers.iris import router as iris_router
# from routers.product_review_llm import router as review_router

app = FastAPI(title="ML API")

create_db_and_tables()

app.include_router(advertising_router)
app.include_router(iris_router)
# app.include_router(review_router)

@app.get("/")
def root():
    return {"message": "API is running"}
