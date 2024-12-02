from app.models import db, Cart, environment, SCHEMA
from sqlalchemy.sql import text

def seed_carts():
    # Query for existing user cart IDs
    existing_cart_user_ids = {cart.user_id for cart in Cart.query.all()}

    # Users to add carts for
    user_ids = [1, 2, 3]

    for user_id in user_ids:
        if user_id not in existing_cart_user_ids:
            new_cart = Cart(user_id=user_id)
            db.session.add(new_cart)

    db.session.commit()

def undo_carts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.carts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM carts"))
        
    db.session.commit()