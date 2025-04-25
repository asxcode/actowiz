from fastapi import FastAPI, Query, Depends
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os

load_dotenv()


engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    price = Column(DECIMAL(10, 2))
    quantity = Column(String(100))
    image = Column(String(255))
    rating = Column(DECIMAL(3, 2))

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search")
def search_products(
    query: str = Query(..., min_length=1),
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * page_size
    products = db.query(Product).filter(Product.name.ilike(f"%{query}%")).offset(offset).limit(page_size).all()
    
    result = [
        {
            "product name": p.name,
            "price": str(p.price),
            "image": p.image,
            "quantity": p.quantity,
            "rating": str(p.rating)
        }
        for p in products
    ]
    return result
