from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class BaseModelFields(BaseModel):
    id : int
    created_at : datetime
    updated_at : Optional[datetime] = None
    is_active = bool
