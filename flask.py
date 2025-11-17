from flask import Flask
import random
import string

app = Flask(__name__)

factlists = [
    "La mayoría de las personas con adicción tecnológica sienten estrés lejos de sus dispositivos.",
    "Más del 50% de los jóvenes se consideran dependientes de sus smartphones.",
    "La dependencia tecnológica es un tema importante en la investigación moderna.",
    "Más del 60% de personas responden mensajes de trabajo minutos después de salir.",
    "Hacer ejercicio o meditar ayuda a reducir la dependencia tecnológica."
]

imagenes = [
    "https://i.imgur.com/5cX1B.jpg",
    "https://i.imgur.com/Z7a7p.jpg",
    "https://i.imgur.com/9QjxY.jpg"
]

adivinanzas = [
    ("Vuelo sin alas, lloro sin ojos. ¿Qué soy?", "Las nubes."),
    ("Tengo agujas pero no hilo. ¿Qué soy?", "Un reloj."),
    ("Mientras más grande soy, menos se ve. ¿Qué soy?", "La oscuridad.")
]

def generar_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

@app.route("/")
def home():
    return """
        <h1>Bienvenido</h1>
        <p>Elige una opción:</p>
        <a href="/random-facts">Dato aleatorio</a><br>
        <a href="/moneda">Lanzar moneda</a><br>
        <a href="/password">Generar contraseña</a><br>
        <a href="/imagen">Imagen aleatoria</a><br>
        <a href="/adivinanza">Adivinanza</a><br>
    """

@app.route("/random-facts")
def random_facts():
    return random.choice(factlists)

@app.route("/moneda")
def moneda():
    return random.choice(["Cara", "Cruz"])

@app.route("/password")
def password():
    return generar_password()

@app.route("/imagen")
def imagen():
    return f'<img src="{random.choice(imagenes)}" width="300">'

@app.route("/adivinanza")
def adivinanza():
    q, a = random.choice(adivinanzas)
    return f"{q}<br><br>Respuesta: {a}"

app.run(debug=True)
