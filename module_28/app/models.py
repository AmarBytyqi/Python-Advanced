from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):  # 9 usages  new *
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
