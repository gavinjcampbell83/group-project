from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

# Adds demo users, ensuring no duplicates
def seed_users():
    # Get all existing emails in the database
    existing_emails = {user.email for user in User.query.all()}

    # Users to seed
    users_to_add = [
        User(username='Demo', first_name='demo', last_name='test', email='demo@aa.io', password='password'),
        User(username='marnie', first_name='marnie', last_name='test', email='marnie@aa.io', password='password'),
        User(username='bobbie', first_name='bobbie', last_name='test', email='bobbie@aa.io', password='password'),
    ]

    # Add only users with unique emails
    for user in users_to_add:
        if user.email not in existing_emails:
            db.session.add(user)
            existing_emails.add(user.email)  # Add the email to the set to prevent duplicates

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()