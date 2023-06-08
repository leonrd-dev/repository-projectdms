import os
import importlib
from configs.database import engine

def createTable():
    moduleNamesOST = os.listdir("entities")
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if (ext == ".py"):
            module = importlib.import_module("entities." + name)
            module.Base.metadata.create_all(bind=engine)