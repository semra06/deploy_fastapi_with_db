from fastapi import APIRouter, Depends
from sqlmodel import Session
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.chat_models import init_chat_model
from models import ProductReview, AnalyzedReview, ProductReviewRate
from database import get_db

load_dotenv()
router = APIRouter()

model = init_chat_model(
    model="gemini-2.5-flash-lite",
    model_provider="google_genai",
    max_tokens=500
)

agent = create_agent(
    model=model,
    tools=[],
    response_format=ToolStrategy(schema=ProductReview),
    system_prompt="Analyze product reviews and extract structured data."
)


@router.post("/llm/chat")
def analyze_review(
    request: AnalyzedReview,
    db: Session = Depends(get_db)
):
    result = agent.invoke({
        "messages": [{"role": "user", "content": request.review}]
    })

    structured = result["structured_response"]

    record = ProductReviewRate(
        user_info=request.user,
        product=request.product,
        review=request.review,
        rate=structured.get("rating"),
        sentiment=structured.get("sentiment"),
        key_points=", ".join(structured.get("key_points", []))
    )

    db.add(record)
    db.commit()

    return structured
