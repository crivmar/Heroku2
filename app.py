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


@app.route ('/juegos/<identificador>', methods=["GET"])
def detalle(identificador):
    for i in documento:
        if identificador == str(i.get('id')):
            try: 
                nombre=i.get('nombre')
                distribuidor=i.get('distribuidor')
                anno=i.get('año')
                categoria=i.get('categoria')
            except:
                abort(404)
    return render_template("detalle.html", nombre=nombre, distribuidor=distribuidor, anno=anno, categoria=categoria)

@app.route ('/listajuegos', methods=["POST"])
def lista():
    cadena= request.form.get("nombre_control")
    for i in documento:
        if i.get("nombre").startswith(cadena):
            conf=True
            nombre=i.get('nombre')
            desarrollador=i.get('desarrollador')
            identificador=i.get('id')
            return render_template("listajuegos.html", documento=documento, cadena=cadena, nombre=nombre, desarrollador=desarrollador, identificador=identificador)
    return render_template("listajuegos.html", documento=documento)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)