from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        return "Cliente cadastrado com sucesso!"
    else:
        return "Erro"

if __name__ == '__main__':
    app.run(debug=True)
