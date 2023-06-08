from sqlalchemy import String,Column,Float,Integer, Boolean
from sqlalchemy.orm import relationship
from configs.database import Base

class MtrDivision(Base):
    __tablename__ = "mtr_division"
    is_active = Column(Boolean, default=True, nullable=False)
    division_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    division_code = Column(String(3), nullable=False, unique=True)
    division_name = Column(String(35), nullable=False)