from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.database import engine, Base
from app.modules.category.router import router as category_router
from app.modules.product.router import router as product_router


# database initialization
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully")
    yield
    print("Shutting down...")


app = FastAPI(title="Inventory Management System", lifespan=lifespan)

# frontend works on different port so we need to allow it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, etc.
    allow_headers=["*"],  # Allow all headers
)

# Include Routers
app.include_router(category_router)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "API is running"}
