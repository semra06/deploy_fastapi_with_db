from datetime import datetime
from typing import Optional, Literal, List
from sqlmodel import SQLModel, Field


# ---------- DB MODELS ----------

class Advertising(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tv: float
    radio: float
    newspaper: float
    prediction: float
    prediction_time: datetime = Field(default_factory=datetime.utcnow)
    client_ip: str


class IrisPrediction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    prediction: str
    prediction_time: datetime = Field(default_factory=datetime.utcnow)
    client_ip: str


class ProductReviewRate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_info: str
    product: str
    review: str
    rate: Optional[int]
    sentiment: Optional[str]
    key_points: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ---------- REQUEST MODELS ----------

class RequestAdvertising(SQLModel):
    tv: float
    radio: float
    newspaper: float


class IrisRequest(SQLModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float


class AnalyzedReview(SQLModel):
    user: str
    product: str
    review: str


# ---------- LLM OUTPUT ----------

class ProductReview(SQLModel):
    rating: Optional[int] = Field(ge=1, le=5)
    sentiment: Literal["positive", "negative"]
    key_points: List[str]
