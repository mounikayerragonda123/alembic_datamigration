
"""from fastapi import FastAPI
import Models
from database import engine
from routers import auth, todos

app=FastAPI()

Models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)"""

from fastapi import FastAPI, Depends, HTTPException, Path
import Models
from database import engine
from routers import auth,todos,admin,users

app=FastAPI()

Models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
