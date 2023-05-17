from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

#engine = create_engine('sqlite:///basepaises.db', echo=True)
engine = create_engine("postgresql+psycopg2://invitado:UTPLUTPL@localhost:5432/demo1", echo=True)