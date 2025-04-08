from main import app
import tempfile
from flask import render_template, send_file
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

#Cria o bat para dowload
@app.route("/download_bat/<int:id>")
def download_bat(id):
    pasta = session.query(mape).filter_by(id=id).first()
    
    if not pasta:
        return f"Não foi encontrada a pasta com ID {id}"

    bat_content = f"@echo off\ncls\nnet use J: {pasta.caminho}\ndel /f \"%~f0\"\nexit\n"

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode="w", encoding="utf-8")
    tmp.write(bat_content)
    tmp.close()
    bat_file_path = tmp.name

    return send_file(bat_file_path, as_attachment=True, download_name=f"Mapeamento_{id}.bat")


#Homepage
@app.route("/")
def homepage():
    return render_template("folder.html")

#Manutenção
@app.route("/manutenção")
def manut():
    return render_template("manut.html")

#RH
@app.route("/rh")
def rh():
    return render_template("rh.html")

#Fin
@app.route("/financeiro")
def fin():
    return render_template("fin.html")

#gate
@app.route("/gate")
def gate():
    return render_template("gate.html")

#Expedição
@app.route("/expedição")
def exp():
    return render_template("exp.html")

#Exportação
@app.route("/exportação")
def ext():
    return render_template("ext.html")

#Controladoria
@app.route("/controladoria")
def control():
    return render_template("control.html")

#juridico
@app.route("/juridico")
def jur():
    return render_template("jur.html")

#Polimento
@app.route("/fabricas")
def pol():
    return render_template("fabricas.html")

#Porcelanato
@app.route("/marketing")
def porce():
    return render_template("mkt.html")

###FÁBRICAS###

@app.route("/fabricas/PB1")
def pb1():
    return render_template("PB1.html")

@app.route("/fabricas/PB2")
def pb2():
    return render_template("PB2.html")

@app.route("/fabricas/PB10")
def pb10():
    return render_template("PB10.html")

@app.route("/fabricas/PB4")
def pb4():
    return render_template("PB4.html")

@app.route("/fabricas/PB9")
def pb9():
    return render_template("PB9.html")