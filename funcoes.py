# Função calcular_imc
def calcular_imc(peso,altura):
    return peso/altura**2
# Função categoria_imc
def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso\n Se alimente mais 😉"
    elif imc < 24.9:
        return "Peso Normal 😊"
    elif imc < 29.9:
        return "Acima do peso ☹️"
    elif imc < 34.9:
        return "Obesidade I"
    elif imc < 39.9:
        return "Obesidade II"
    else:
        return "Obesidade III"