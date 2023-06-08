from typing import List, Optional
from pydantic import BaseModel

class MtrDivisionGetSchema(BaseModel):
    division_code:Optional[str] = None
    division_name:Optional[str] = None
    
    class Config:
        orm_mode = True