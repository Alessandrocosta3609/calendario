from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        data_str = request.form['data']
        data = datetime.strptime(data_str, "%Y-%m-%d")
        hoje = datetime.now()

        dias_semana = [
            "segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"
        ]

        diferenca = (data - hoje).days
        dia_semana = dias_semana[data.weekday()]
        semana_ano = data.isocalendar()[1]  # número da semana (1–52)

        if diferenca > 0:
            mensagem = f"Faltam {diferenca} dias para essa data."
        elif diferenca < 0:
            mensagem = f"Essa data foi há {-diferenca} dias."
        else:
            mensagem = "Essa data é hoje!"

        resultado = {
            "data": data.strftime("%d/%m/%Y"),
            "dia_semana": dia_semana,
            "mensagem": mensagem,
            "semana_ano": semana_ano
        }

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
