from main import app
from flask import render_template

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
@app.route("/polimento")
def pol():
    return render_template("pol.html")

#Porcelanato
@app.route("/porcelanato")
def porce():
    return render_template("porce.html")