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
    listado=[]
    cadena= request.form.get("nombre_control").capitalize()
    if cadena =="":
        return render_template("listajuegos.html", documento=documento)
    else:
        for i in documento:
            diccionario={}
            if str(i.get('nombre')).startswith(cadena):
                conf=True
                diccionario['nombre']=i.get('nombre')
                diccionario['desarrollador']=i.get('desarrollador')
                diccionario['id']=i.get('id')
                listado.append(diccionario)
    return render_template("listajuegos.html", listado=listado, conf=conf)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)