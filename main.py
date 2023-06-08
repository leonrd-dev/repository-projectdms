from fastapi import FastAPI
from controllers import DivisionController
from utils.AddModelsEngine import createTable

app = FastAPI()

createTable()


app.include_router(DivisionController.routerDivision)


