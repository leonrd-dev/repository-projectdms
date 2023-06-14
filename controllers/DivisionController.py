from fastapi import APIRouter, Depends, status, HTTPException
from cruds import DivisionCRUD
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from schemas import DivisionSchema




router = APIRouter(tags=["Division"],prefix="/api/general")

@router.get("/get-divisions", status_code=status.HTTP_200_OK)
def get_division(db:Session=Depends(get_db)):
    divisions = DivisionCRUD.get_all_division(db)
    if not divisions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return (divisions, "Successfully retrieved")

@router.get("/get-division/{division_id}", status_code=status.HTTP_200_OK)
def get_division_by_id(division_id, db:Session=Depends(get_db)):
    division = DivisionCRUD.get_by_id_division(db, division_id)
    if not division: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return (division, "Successfully retrieved")

@router.post("/create-division/", status_code=status.HTTP_201_CREATED)
def post_division(payload: DivisionSchema.MtrDivisionGetSchema, db: Session = Depends(get_db)) :
    try:
        create_division = DivisionCRUD.post_division(db, payload)
        db.add(create_division)
        db.commit()
        

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    
    
    db.refresh(create_division)
    return (create_division, "Successfully created")


@router.delete("/delete-division/{division_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_division(division_id, db:Session=Depends(get_db)):
    remove_division = DivisionCRUD.delete_division(db,division_id)

    if not remove_division:
        db.rollback()
    
    db.commit()

    return (remove_division, "Successfully deleted")

@router.put("/update-division/{division_id}",status_code=status.HTTP_202_ACCEPTED)
def put_division(payload:DivisionSchema.MtrDivisionGetSchema, division_id, db:Session=Depends(get_db)):
    update_division, print_update = DivisionCRUD.put_division(db, payload, division_id)

    if not update_division:
        db.rollback()

    db.commit()
    db.refresh(print_update)

    return print_update



    
routerDivision = router

  
