from fastapi import FastAPI
from controllers import DivisionController,DistrictController
from utils.AddModelsEngine import createTable

app = FastAPI()

createTable()


app.include_router(DivisionController.routerDivision)
app.include_router(DistrictController.routerDistrict)


