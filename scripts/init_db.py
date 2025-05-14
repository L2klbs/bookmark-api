import sys
import os
import asyncio

# Add the parent directory (project root) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.db import engine
from app.models import EntryDB
from app.db import Base

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created")

if __name__ == "__main__":
    asyncio.run(init())
