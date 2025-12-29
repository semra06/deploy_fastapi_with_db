from fastapi.routing import APIRouter
from fastapi import Depends, Request
from sqlmodel import Session
from models import Advertising, RequestAdvertising
from database import get_db
import joblib

router = APIRouter()

model = joblib.load("saved_models/03.randomforest_with_advertising.pkl")


def make_prediction(model, data):
    X = [[data.tv, data.radio, data.newspaper]]
    return float(model.predict(X)[0])


def insert_advertising(data, prediction, client_ip, db):
    record = Advertising(
        tv=data.tv,
        radio=data.radio,
        newspaper=data.newspaper,
        prediction=prediction,
        client_ip=client_ip
    )

    with db as session:
        session.add(record)
        session.commit()
        session.refresh(record)

    return record


@router.post("/prediction/advertising")
def predict_advertising(
    request: RequestAdvertising,
    fastapi_req: Request,
    db: Session = Depends(get_db)
):
    prediction = make_prediction(model, request)
    db_record = insert_advertising(request, prediction, fastapi_req.client.host, db)
    return {"prediction": prediction, "db_record": db_record}
