# # app\routers\order.py
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from utils.security import decode_access_token
# from controllers.order import get_all_orders, create_order, get_order
# from schemas.order import OrderCreate

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# router = APIRouter()

# @router.get("/")
# def read_all_orders(token: str = Depends(oauth2_scheme)):
#     # Assuming decode_access_token function to validate the token
#     user = decode_access_token(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
#     return get_all_orders()

# @router.post("/")
# def create_new_order(order: OrderCreate, token: str = Depends(oauth2_scheme)):
#     user = decode_access_token(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
#     return create_order(order)

# @router.get("/{order_id}")
# def read_order(order_id: int, token: str = Depends(oauth2_scheme)):
#     user = decode_access_token(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
#     order = get_order(order_id)
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
