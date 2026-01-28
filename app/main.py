from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine, Base
from app.modules.category.router import router as category_router
from app.modules.product.router import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully")
    yield  # This is where the app "lives" and handles requests
    print("Shutting down...")


app = FastAPI(title="Inventory Management System", lifespan=lifespan)

# Include Routers
app.include_router(category_router)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "API is running"}
