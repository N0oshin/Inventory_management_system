import uuid
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.core.config import settings

# Create the Engine
engine = create_async_engine(settings.database_url, echo=True)

# Create new Session for every request
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


# The Base Class
class Base(DeclarativeBase):
    # Requirement: UUID as Primary Key for all models
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, index=True
    )


# This function is used by FastAPI to provide a DB session to routes
async def get_db():
    # 'async with' ensures the session is closed automatically when finished
    async with AsyncSessionLocal() as session:
        yield session
