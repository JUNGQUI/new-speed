# main.py
from fastapi import FastAPI
from fetcher import get_today_summary

app = FastAPI()

@app.get("/summary/today")
def today_summary():
    return {"summary": get_today_summary()}
