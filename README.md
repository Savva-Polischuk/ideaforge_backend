terminal:

pip install -r requirements.txt

alembic init alembic

alembic revision --autogenerate

alembic upgrade head 

uvicorn app:app --reload