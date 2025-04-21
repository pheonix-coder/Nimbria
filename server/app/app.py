from fastapi import FastAPI
from .models import Base, Product
from .lib.db import engine
from .routers import router as api_router

Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import Session
from .lib.db import get_db

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    db: Session = next(get_db())
    try:
        # Add static products
        products = [
            {"name": "Mobile Phone", "description": "A smartphone for communication and entertainment", "price": 799.99},
            {"name": "Laptop", "description": "A portable computer for work and personal use", "price": 1299.99},
            {"name": "Television", "description": "A device for watching movies and shows", "price": 599.99},
            {"name": "Headphones", "description": "For listening to music and audio privately", "price": 99.99},
            {"name": "Smartwatch", "description": "A wearable device with fitness tracking and notifications", "price": 299.99},
            {"name": "Tablet", "description": "A portable device for reading and browsing", "price": 399.99},
            {"name": "Wireless Mouse", "description": "A cordless mouse for computer navigation", "price": 29.99},
            {"name": "Keyboard", "description": "A device for typing on a computer", "price": 79.99},
            {"name": "Webcam", "description": "A camera for video conferencing", "price": 49.99},
            {"name": "Printer", "description": "A device for printing documents", "price": 149.99},
            {"name": "External Hard Drive", "description": "For storing extra files and backups", "price": 99.99},
            {"name": "USB Flash Drive", "description": "A portable storage device", "price": 19.99},
            {"name": "Monitor", "description": "A display screen for computers", "price": 249.99},
            {"name": "Graphics Card", "description": "For enhancing computer graphics performance", "price": 399.99},
            {"name": "CPU", "description": "The central processing unit of a computer", "price": 299.99},
            {"name": "RAM", "description": "Random access memory for computers", "price": 129.99},
            {"name": "Motherboard", "description": "The main circuit board of a computer", "price": 199.99},
            {"name": "Power Supply", "description": "Provides power to a computer", "price": 79.99},
            {"name": "Computer Case", "description": "The enclosure for computer components", "price": 99.99},
            {"name": "SSD", "description": "Solid state drive for fast storage", "price": 149.99},
            {"name": "Router", "description": "Connects devices to the internet", "price": 59.99},
            {"name": "Modem", "description": "Connects to the internet service provider", "price": 49.99},
            {"name": "Ethernet Cable", "description": "Connects devices to a network", "price": 9.99},
            {"name": "HDMI Cable", "description": "Connects devices to a display", "price": 7.99},
            {"name": "Power Adapter", "description": "Provides power to devices", "price": 14.99},
            {"name": "Screen Protector", "description": "Protects device screens from scratches", "price": 4.99},
            {"name": "Phone Case", "description": "Protects phones from damage", "price": 19.99},
            {"name": "Cleaning Kit", "description": "For cleaning electronic devices", "price": 9.99},
            {"name": "Stylus", "description": "For drawing and writing on touch screens", "price": 24.99},
        ]

        for product_data in products:
            db_product = Product(**product_data)
            db.add(db_product)
        db.commit()

    finally:
        db.close()
