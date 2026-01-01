# FastAPI ML Application with Database Persistence

This project demonstrates a production-style FastAPI application where
machine learning predictions are persisted into a relational database,
following a common **Advertising pattern**.

##  Features

- FastAPI-based REST API
- Machine Learning predictions
  - Advertising Sales Prediction
  - Iris Species Prediction
- Database persistence using SQLModel
- PostgreSQL (Docker) or SQLite support
- Clean router-based architecture

##  Project Structure

deploy_fastapi_with_db/
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── routers/
│ ├── advertising.py
│ ├── iris.py
│ └── product_review_llm.py
└── saved_models/


## 🧠 Implemented Tasks

### Part 1 – Iris Prediction
- Iris prediction endpoint implemented
- Prediction results are inserted into the database
- Follows the same persistence pattern as Advertising

### Part 2 – Product Review Analysis
- Product review analysis logic implemented
- Database model (`ProductReviewRate`) created
- Persistence logic aligned with Advertising pattern  
*(LLM integration is optional and environment-dependent)*

## ⚙️ Setup & Run

### 1. Activate virtual environment
```bash
source .venv/bin/activate
