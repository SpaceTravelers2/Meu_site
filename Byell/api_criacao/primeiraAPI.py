from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def ola():
    return """
    Comidas Favoritas:
    <ul> 
        <li> Pizza </li>
        <li> Sushi </li>
        <li> Churrasco </li>
    </ul>
    
    """


@app.route('/banks/v1')
def bancos():
    return [{"nome": "Bradesco"},
            {"nome":"Santander"},
            {"nome": "Itaú"}]
@app.route('/byellstark')
def byellstark():
    return "Nice to meet you :)"

@app.route('/banks/v1/<int:numero_banco>')
def banco_codigo(numero_banco):
    return jsonify({"Código do banco": numero_banco,
            "Nome do banco":"Não cadastrado ainda"
    })
app.run(host="0.0.0.0", debug=True)