from sqlalchemy import String,Column,Float,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from configs.database import Base

class MtrDistrict(Base):
    __tablename__ = "mtr_district"
    is_active = Column(Boolean, default=True, nullable=False)
    district_id = Column(Integer, primary_key= True, nullable=False, autoincrement=True)
    district_code = Column(String(5), nullable=False, unique=True)
    district_name = Column(String(100),nullable=False)
    city_id = Column(Integer, ForeignKey('mtr_city.city_id'))

    city = relationship("MtrCity",back_populates= "district")