# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import auth, user, dish, reservation, profile  # Add profile router
# from routers import order  # Add profile router
import os

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app's URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Adjust allowed HTTP methods as needed
    allow_headers=["*"],
)

# Define the path for the images directory
base_dir = os.path.dirname(os.path.abspath(__file__))
image_directory = os.path.join(base_dir, "images")

# Ensure the images directory exists
os.makedirs(image_directory, exist_ok=True)

# Mount the /images directory to serve static files
app.mount("/images", StaticFiles(directory=image_directory), name="images")

# Include your routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/user", tags=["user"])
app.include_router(dish.router, prefix="/api/dishes", tags=["dishes"])
# app.include_router(order.router, prefix="/api/orders", tags=["orders"])
app.include_router(reservation.router, prefix="/api/reservations", tags=["reservations"])
app.include_router(profile.router, prefix="/api/user", tags=["profile"])  # Add profile router
