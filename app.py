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

@app.route ('/juegos',methods=["GET","POST"])
def juegos():
    if request.method=="GET":
        categoria=[]
        for i in documento:
            if i.get('categoria') not in categoria:
                categoria.append(i.get('categoria'))       
        return render_template("juegos.html", categoria=categoria)
    else:
        post=True
        listado=[]
        cadena= request.form.get("nombre_control").capitalize()
        if cadena =="":
            return render_template("juegos.html", documento=documento, post=post, cadena=cadena)
        else:
            var=True
            for i in documento:
                diccionario={}
                if str(i.get('nombre')).startswith(cadena):
                    conf=True
                    diccionario['nombre']=i.get('nombre')
                    diccionario['desarrollador']=i.get('desarrollador')
                    diccionario['id']=i.get('id')
                    listado.append(diccionario)
                    var=False
            if var:
                abort(404)
        return render_template("juegos.html", listado=listado, conf=conf, post=post, cadena=cadena)

@app.route ('/juegos/<identificador>', methods=["GET"])
def detalle(identificador):
    var=True
    for i in documento:
        if identificador == str(i.get('id')):
            nombre=i.get('nombre')
            distribuidor=i.get('distribuidor')
            anno=i.get('año')
            categoria=i.get('categoria')
            var=False
    if var:
        abort(404)
    return render_template("detalle.html", nombre=nombre, distribuidor=distribuidor, anno=anno, categoria=categoria)

# @app.route ('/listajuegos', methods=["POST"])
# def lista():
#     listado=[]
#     cadena= request.form.get("nombre_control").capitalize()
#     if cadena =="":
#         return render_template("listajuegos.html", documento=documento)
#     else:
#         var=True
#         for i in documento:
#             diccionario={}
#             if str(i.get('nombre')).startswith(cadena):
#                 conf=True
#                 diccionario['nombre']=i.get('nombre')
#                 diccionario['desarrollador']=i.get('desarrollador')
#                 diccionario['id']=i.get('id')
#                 listado.append(diccionario)
#                 var=False
#         if var:
#             abort(404)
#     return render_template("listajuegos.html", listado=listado, conf=conf)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)