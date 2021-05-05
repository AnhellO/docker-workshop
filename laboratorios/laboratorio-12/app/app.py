from flask import Flask, request, render_template, jsonify, abort
from models import MyCats
from peewee import DoesNotExist

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.form['name'] if request.method == 'POST' and 'name' in request.form else 'Anonymous'
    return render_template('hello.html', name=name)

@app.route('/my-cats', methods=['GET', 'POST'])
def cats():
    if request.method == 'POST':
        cat = MyCats(nombre=request.form['nombre'], imagen=request.form['imagen'])
        cat.save()
        return {'ID': cat.id, 'nombre': cat.nombre, 'apellido': cat.apellido, 'imagen': cat.imagen}

    return jsonify([{'ID': cat.id, 'nombre': cat.nombre, 'apellido': cat.apellido, 'imagen': cat.imagen} for cat in MyCats.select()])

@app.route('/my-cats/<cat_id>')
def kitten(cat_id):
    try:
        cat = MyCats.get(MyCats.id == cat_id)
        return render_template('cat.html', id=cat.id, nombre=cat.nombre, apellido=cat.apellido, imagen=cat.imagen)
        # Use this in case you want to serve as JSON
        # return {'ID': cat.id, 'nombre': cat.nombre, 'imagen': cat.imagen}
    except DoesNotExist:
        abort(404)
    except:
        abort(500)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404