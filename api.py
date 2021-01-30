from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    info = {
        'mensaje': 'Bienvenido/a! Esta es la API del CV de Facundo Argaña.',
        'acciones': [
            'GET /curriculum',
            'POST /mensajes'
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + 'static/profile-pic.jpg'
    cv = {
        'nombre': 'Facundo',
        'apellido': 'Argaña',
        'residencia': 'Argentina',
        'experiencia': [{
            'posicion': 'Technical Solutions Engineer, Data',
            'empresa': 'MightyHive',
            'desde': 'marzo 2020',
            'hasta': 'actualmente trabajo aquí',
            'descripción': 'Diseñar, realizar y validar implementaciones de recolección de datos en sitios / apps, Diseñar y desarrollar aplicaciones de integraciones de datos en entornos Cloud, Coordinar y planificar proyectos de clientes, Desarrollar herramientas de uso interno / externo para validación, exploración y seguimiento de datos, Investigar nuevas herramientas y prácticas en torno a data analytics.'
        }],
        'educación': {
            'nivel': 'Universitario',
            'estado': 'incompleto',
            'titulo': 'Licenciatura en Ciencias de Datos',
            'institución': 'Universidad de Bunenos Aires',
            'facultad': 'Facultad de Ciencias Exactas y Naturales'
        },
        'intereses': ['Data Science', 'Machine Learning', 'Computer Science'],
        'redes': {
            'github': 'https://github.com/efacundoargana',
            'twitter': 'https://twitter.com/efacundoargana',
            'linkedin': 'https://www.linkedin.com/in/efacundoargana/',
            'email': 'efacundoargana@gmail.com'
        },
        'foto': url_imagen
    }
    return jsonify(cv)


@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description='Debe enviar el mensaje en el body del POST.')

    print('MENSAJE DE CONTACTO: ' + str(mensaje))
    return 'Gracias por tu mensaje!'


if __name__ == '__main__':
    app.run()
