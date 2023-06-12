from typing import List, Optional
from pydantic import BaseModel

class MtrDistrictGetModel(BaseModel):
    province_id:Optional[int] = None
    province_name:Optional[str] = None
    city_id:Optional[int] = None
    city_name:Optional[str] = None
    district_code:Optional[str] = None
    district_name:Optional[str] = None
    
    class Config:
        orm_mode = True


class MtrDistrictPostModel(BaseModel):
    city_id: Optional[int] = None
    district_code: Optional[str] = None
    district_name: Optional[str] = None

    class Config:
        orm_mode = True
