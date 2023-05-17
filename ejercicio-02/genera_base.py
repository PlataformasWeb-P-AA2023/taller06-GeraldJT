from sqlalchemy import create_engine
from configuracion import engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombreP = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameID = Column(String)
    itu = Column(String)
    lenguage = Column(String)
    depend = Column(String)



Base.metadata.create_all(engine)

