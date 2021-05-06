## IMPORTAR MÓDULOS ##

from flask import Flask, render_template, request, abort
import os, json

app= Flask (__name__)

## ABRIR ARCHIVO Y GUARDAR DATOS ##

with open ('./MSX.json') as f:
    documento=json.load(f)

## PROGRAMA PRINCIPAL ##

@app.route ('/', methods=["GET"])
def inicio():
    return render_template("index.html")

@app.route ('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html")

@app.route ('/listajuegos', methods=["POST"])
def lista():
    return render_template("listajuegos.html", documento=documento)



port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)