from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aquí deberías obtener las reinstrucciones de alguna fuente (base de datos, etc.)
    reinstrucciones = []  # Agrega aquí la lógica para obtener las reinstrucciones.
    return render_template('index.html', reinstrucciones=reinstrucciones)

if __name__ == "__main__":
    app.run()
