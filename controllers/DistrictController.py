from fastapi import APIRouter, Depends, status, HTTPException
from cruds import DistrictCRUD
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from schemas import DistrictSchema




router = APIRouter(tags=["District"],prefix="/api/general")

@router.get("/get-districts", status_code=status.HTTP_200_OK)
def get_district(db:Session=Depends(get_db)):
    districts = DistrictCRUD.get_all_district(db)
    if not districts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return (districts, "Successfully retrieved")

@router.get("/get-district/{district_id}", status_code=status.HTTP_200_OK)
def get_district_by_id(district_id, db:Session=Depends(get_db)):
    district = DistrictCRUD.get_by_id_district(db, district_id)
    if not district: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return (district, "Successfully retrieved")

@router.post("/create-district/", status_code=status.HTTP_201_CREATED)
def post_district(payload: DistrictSchema.MtrDistrictPostModel, db: Session = Depends(get_db)) :
    try:
        create_district = DistrictCRUD.post_district(db, payload)
        db.add(create_district)
        db.commit()
        

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    
    
    db.refresh(create_district)
    return (create_district, "Successfully created")


@router.delete("/delete-district/{district_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_division(district_id, db:Session=Depends(get_db)):
    remove_district = DistrictCRUD.delete_district(db,district_id)

    if not remove_district:
        db.rollback()
    
    db.commit()

    return (remove_district, "Successfully deleted")

@router.put("/update-district/{district_id}",status_code=status.HTTP_202_ACCEPTED)
def put_district(payload:DistrictSchema.MtrDistrictPostModel, district_id, db:Session=Depends(get_db)):
    update_district, print_update = DistrictCRUD.put_district(db, payload, district_id)

    if not update_district:
        db.rollback()

    db.commit()
    db.refresh(print_update)

    return print_update



    
routerDistrict = router

  
