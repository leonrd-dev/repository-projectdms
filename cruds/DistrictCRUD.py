from sqlalchemy.orm import Session
from entities import DistrictEntity, CityEntity, ProvinceEntity


def get_by_id_district(db:Session, id = int):
    district = db.query(CityEntity.MtrCity.province_id,
                        ProvinceEntity.MtrProvince.province_name,
                        DistrictEntity.MtrDistrict.city_id,
                        CityEntity.MtrCity.city_name,
                        DistrictEntity.MtrDistrict.district_code,
                        DistrictEntity.MtrDistrict.district_name
                        ).join(CityEntity.MtrCity, DistrictEntity.MtrDistrict.city_id==CityEntity.MtrCity.city_id, isouter=True
                        ).join(ProvinceEntity.MtrProvince, CityEntity.MtrCity.province_id == ProvinceEntity.MtrProvince.province_id, isouter=True
                        ).filter(DistrictEntity.MtrDistrict.district_id==id).order_by(DistrictEntity.MtrDistrict.district_id).first()
    
    if district is None:
        return None
    
    response = {}
    response.update(district._asdict())


    
    return response

def get_all_district(db:Session):
    return db.query(DistrictEntity.MtrDistrict).order_by(DistrictEntity.MtrDistrict.district_id).all()

def post_district(db:Session, payload: DistrictEntity.MtrDistrict):
    return DistrictEntity.MtrDistrict(**payload.dict()) 

def delete_district(db:Session, id = int):
    return db.query(DistrictEntity.MtrDistrict).filter(DistrictEntity.MtrDistrict.district_id == id).delete(synchronize_session=False)

def put_district(db:Session, payload:DistrictEntity.MtrDistrict, id = int):
    update_district = db.query(DistrictEntity.MtrDistrict).filter(DistrictEntity.MtrDistrict.district_id == id)
    update_district.update(payload.dict())
    update_message = update_district.first()
    return update_district, update_message

    
