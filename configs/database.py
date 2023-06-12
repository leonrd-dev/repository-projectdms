from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#server = 'nomad2805'
#database = 'DMSTEST'

database_url = "" #MSSQL SERVER#database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
#database_url = f"postgresql://{check.db_user}:{check.db_password}@{check.db_server}:{check.db_port}/{check.db_name}" #POSTGRESQL
# database_url = f"mssql+pyodbc://LAPTOP-SB8ST6RK/DMSTEST?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes" #MSSQL SERVER#database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
