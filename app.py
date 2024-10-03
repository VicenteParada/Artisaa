from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template

app = Flask(__name__)

# CLASES DEL SISTEMA

# CONDUCTOR
class Conductor:
    def __init__(self, id_conductor, nombre_conductor, cantidad_excesos):
        self.id_conductor = id_conductor
        self.nombre_conductor = nombre_conductor
        self.cantidad_excesos = cantidad_excesos

# REINSTRUCTOR
class Reinstructor:
    def __init__(self, id_reinstructor, nombre_reinstructor, nivel_reinstructor, correo_reinstructor):
        self.id_reinstructor = id_reinstructor
        self.nombre_reinstructor = nombre_reinstructor
        self.nivel_reinstructor = nivel_reinstructor
        self.correo_reinstructor = correo_reinstructor

# REINSTRUCCION
class Reinstruccion:
    def __init__(self, id_reinstruccion, reinstructor, conductor, fecha_asignacion=None, realizado_bool=False):
        self.id_reinstruccion = id_reinstruccion
        self.reinstructor = reinstructor
        self.conductor = conductor
        self.fecha_asignacion = fecha_asignacion or datetime.now().strftime("%d/%m/%Y")
        self.realizado_bool = realizado_bool

    def generar_nombre(self):
        fecha_sin_barras = self.fecha_asignacion.replace("/", "")
        return f"{self.conductor.nombre_conductor}_{fecha_sin_barras}_{self.reinstructor.nombre_reinstructor}"

    def verificar_realizado(self):
        self.realizado_bool = False  # Simulación para este ejemplo

# Ruta principal
@app.route('/')
def index():
    # Crear algunos datos de ejemplo
    conductor = Conductor(1, "Jaime Lique Tinte", 5)
    reinstructor = Reinstructor(1, "Luis Trujillo", "Tipo 1", "luis.trujillo@example.com")
    reinstruccion = Reinstruccion(1, reinstructor, conductor)
    
    reinstrucciones = [reinstruccion]  # Lista de reinstrucciones para pasar a la plantilla
    return render_template('index.html', reinstrucciones=reinstrucciones)

# PRUEBAS UNITARIAS
import unittest

class TestReinstruccion(unittest.TestCase):
    def setUp(self):
        self.conductor = Conductor(1, "Jaime Lique Tinte", 5)
        self.reinstructor = Reinstructor(1, "Luis Trujillo", "Tipo 1", "luis.trujillo@example.com")
        self.reinstruccion = Reinstruccion(1, self.reinstructor, self.conductor)

    def test_generar_nombre(self):
        nombre = self.reinstruccion.generar_nombre()
        self.assertEqual(nombre, "Jaime Lique Tinte_26092024_Luis Trujillo")  # Cambia la fecha según sea necesario

    def test_verificar_realizado(self):
        self.reinstruccion.verificar_realizado()
        self.assertFalse(self.reinstruccion.realizado_bool)

    def test_imprimir(self):
        self.reinstruccion.imprimir()  # Verifica manualmente la salida en consola

# Ejecutar las pruebas al correr el archivo
if __name__ == "__main__":
    app.run(debug=True)  # Ejecutar el servidor Flask
    unittest.main()  # Ejecutar pruebas unitarias si se llama directamente
