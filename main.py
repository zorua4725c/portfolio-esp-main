# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_db=button_db, button_python=button_python, button_discord=button_discord, button_html=button_html)

@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variables para la recogida de datos
    text = request.form['text']
    email = request.form['email']
    with open('form.txt', 'a') as f:
        f.write(f'Text: {text}, Email: {email}\n')

    # Aquí puedes devolver una respuesta, redireccionar, etc.
    return f'Formulario enviado con éxito <br><a class="project__link" href="/">Volver</a>'

if __name__ == "__main__":
    app.run(debug=True)
