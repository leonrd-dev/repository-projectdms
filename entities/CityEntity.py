from sqlalchemy.orm import relationship
from configs.database import Base
from sqlalchemy import Column,Integer,String,Identity,Boolean,ForeignKey

class MtrCity(Base):
    __tablename__ = 'mtr_city'
    is_active = Column(Boolean, nullable=False,default=True)
    city_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    city_code = Column(String(5),nullable=False, unique=True)
    city_phone_area = Column(String(5), nullable=False)
    city_name= Column(String(100),nullable=False)
    province_id = Column(Integer,ForeignKey('mtr_province.province_id'))

    province = relationship("MtrProvince",back_populates="citys")
    district = relationship("MtrDistrict",back_populates="city")

   
    