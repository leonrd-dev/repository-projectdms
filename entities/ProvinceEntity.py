from sqlalchemy import Column, String, Integer, Boolean,ForeignKey,Identity
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrProvince(Base):
    __tablename__ = "mtr_province"
    is_active = Column(Boolean, nullable=False, default=True)
    province_id = Column(Integer,primary_key=True)
    province_code = Column(String(5),nullable=False,unique=True)
    province_name = Column(String(100), nullable=False)
    country_id = Column(Integer,ForeignKey("mtr_country.country_id",ondelete="CASCADE"))

    country = relationship("MtrCountry",back_populates="province")
    citys = relationship("MtrCity",back_populates="province")