from flask import Flask 
from controller.HomeController import blueprint_home  # Corrección: punto en lugar de espacio

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_home, url_prefix='/api/v1')
    
    @app.route('/')
    def home():
        return {'msj': 'hola mundo'}
    
    return app  # Asegurar indentación correcta

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')