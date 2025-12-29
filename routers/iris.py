from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from models import IrisPrediction, IrisRequest
from database import get_db
import joblib

router = APIRouter()

model = joblib.load("saved_models/01.knn_with_iris_dataset.pkl")
encoder = joblib.load("saved_models/02.iris_label_encoder.pkl")


@router.post("/prediction/iris")
def predict_iris(
    request: IrisRequest,
    fastapi_req: Request,
    db: Session = Depends(get_db)
):
    X = [[
        request.SepalLengthCm,
        request.SepalWidthCm,
        request.PetalLengthCm,
        request.PetalWidthCm
    ]]
    raw = model.predict(X)
    prediction = encoder.inverse_transform(raw)[0]

    record = IrisPrediction(
        sepal_length=request.SepalLengthCm,
        sepal_width=request.SepalWidthCm,
        petal_length=request.PetalLengthCm,
        petal_width=request.PetalWidthCm,
        prediction=prediction,
        client_ip=fastapi_req.client.host
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {"prediction": prediction}
