#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    url_cv_pdf = request.host_url + 'static/cv_facundo_argana.pdf'
    info = {
        'mensaje': 'Bienvenido/a! Esta es la API del CV de Facundo Argaña.',
        'PDF': url_cv_pdf,
        'acciones': [
            'GET /curriculum',
            'POST /mensajes'
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_picture = request.host_url + 'static/profile-pic.jpg'
    url_certificate = request.host_url + 'static/facundo-argana-ds-certiificate.pdf'

    cv = {
        'basics': {
            'name': 'Facundo Argaña',
            'label': 'Programador',
            'picture': url_picture,
            'email': 'efacundoargana@gmail.com',
            'phone': '+54 9 11 6536 6254',
            'summary': 'Curious and enthusiastic. Interested in the construction of computational models to explain and predict complex behaviors from data analysis. I am currently studying for a degree in Data Science at the University of Buenos Aires. I would like to work in a creative and interdisciplinary place. But above all, I like to work with complex problems that allow me to continue learning.',
            'location': {
                'address': 'Pareja 2470',
                'postalCode': '1419',
                'city': 'Ciudad Autónoma de Buenos Aires'
            },
            'profiles': [
                {
                    'network': 'GitHub',
                    'username': 'efacundoargana',
                    'url': 'https://github.com/efacundoargana'
                },
                {
                    'network': 'LinkedIn',
                    'username': 'efacundoargana',
                    'url': 'https://www.linkedin.com/in/efacundoargana/'
                },
                {
                    'network': 'Twitter',
                    'username': 'efacundoargana',
                    'url': 'https://twitter.com/efacundoargana'
                },
            ],
        },
        'work': [
            {
                'name': 'MightyHive',
                'location': 'Ciudad Autónoma de Buenos Aires',
                'description': 'MightyHive is a new breed of media consultancy that partners with global brands and agencies seeking transformative marketing results in a time of massive disruption and opportunity. Recognized as a global leader in advanced marketing and advertising technologies, MightyHive provides consulting and services in the areas of media operations and training, data strategy and analytics. The company is headquartered in San Francisco, with teams in 19 countries and 24 cities around the world. In 2018, MightyHive merged with S4Capital plc (SFOR.L), a new age/new era digital advertising and marketing services company established by Sir Martin Sorrell in 2018.',
                'url': 'https://mightyhive.com/',
                'position': 'Technical Solutions Engineer, Data',
                'startDate': '2019-12-01',
                'endDate': 'Present',
                'description': [
                    'Design, perform and validate data collection implementations on sites / apps',
                    'Design and develop data integration applications in Cloud environments',
                    'Coordinate and plan client projects',
                    'Develop internal / external use tools for data validation, exploration and monitoring',
                    'Investigate new tools and practices around data analytics'
                ],
            }
        ],
        'education': [
            {
                'institution': 'Universidad de Buenos Aires',
                'faculty': 'Facultad de Ciencias Exactas y Naturales',
                'degree': 'Licenciatura en Ciencia de Datos',
                'url': 'https://lcd.exactas.uba.ar/',
                'startDate': '2020-03-21',
                'endDate': 'In progress'
            },
            {
                'certifications': [
                    {
                        'institution': 'Acámica',
                        'title': 'Data Science Certification',
                        'url': 'https://www.acamica.com/data-science',
                        'certificate': url_certificate
                    }
                ]
            }
        ],
        'skills': [
            {
                'name': 'Programming',
                'languages': [
                    'Pyhon',
                    'SQL',
                    'Javascript'
                ]
            }
        ],
        'languages': [
            {
                'language': 'English',
                'fluency': 'advanced'
            },
            {
                'language': 'Spanish',
                'fluency': 'Native Speaker'
            }
        ],
        'interests': [
            'Data Science',
            'Machine Learning',
            'Computer Science'
        ]
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
