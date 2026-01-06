from fastapi import FastAPI, Depends
from typing import List

import schemas
from database import get_db
from psycopg2.extras import RealDictCursor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://scanx.squarespace.com", "https://www.scanx.care"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  
    allow_headers=["*"], 
)

@app.get("/coupons/", response_model=List[schemas.Coupon])
def read_coupons(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT id, coupon_name, discount, coupon_usage FROM coupon OFFSET %s LIMIT %s",
            (skip, limit),
        )
        coupons = cur.fetchall()
    return coupons