from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///dados.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class mape(Base):
    __tablename__ = "mape"
    id = Column(Integer, primary_key=True, autoincrement=True)
    setor = Column("setor", String)
    caminho = Column("caminho", String)
    
    def __init__(self, setor, caminho):
        self.setor = setor
        self.caminho = caminho
Base.metadata.create_all(bind=db)

#Adicionar
#mape = mape(setor="PB4", caminho= r"\\brtja20p\Acessos\Pb4")
#session.add(mape)
#session.commit()

#Deletar
delet = session.query(mape).filter_by(id="45").first()
session.delete(delet)
session.commit()

#READ
#lista_setor = session.query(mape).filter_by(setor="manutencao")
#print(lista_setor)