from sqlalchemy.orm import Session
from entities import DivisionEntity

def get_by_id_division(db:Session, id = int):
    return db.query(DivisionEntity.MtrDivision).filter(DivisionEntity.MtrDivision.division_id == id).first()

def get_all_division(db:Session):
    return db.query(DivisionEntity.MtrDivision).order_by(DivisionEntity.MtrDivision.division_id).all()

def post_division(db:Session, payload: DivisionEntity.MtrDivision):
    return DivisionEntity.MtrDivision(**payload.dict())
def delete_division(db:Session, id = int):
    return db.query(DivisionEntity.MtrDivision).filter(DivisionEntity.MtrDivision.division_id == id).delete(synchronize_session=False)

def put_division(db:Session, payload:DivisionEntity.MtrDivision, id = int):
    update_division = db.query(DivisionEntity.MtrDivision).filter(DivisionEntity.MtrDivision.division_id == id)
    update_division.update(payload.dict())
    update_message = update_division.first()
    return update_division, update_message

    
