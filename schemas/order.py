# # schemas/order.py
# from pydantic import BaseModel
# from datetime import datetime

# class OrderCreate(BaseModel):
#     user_id: int
#     dish_id: int
#     quantity: int

# class OrderResponse(BaseModel):
#     id: int
#     user_id: int
#     dish_id: int
#     quantity: int
#     total_price: float
#     order_date: datetime

#     class Config:
#         from_attributes = True