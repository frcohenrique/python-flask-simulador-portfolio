from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def calcular():
    nubr33 = 0.2
    mxrf11 = 0.4
    hash11 = 0.9
    itub3 = 0.3
    resposta_nubr33 = ''
    resposta_mxrf11 = ''
    resposta_hash11 = ''
    resposta_itub3 = ''
    input_nubr33 = request.form.get('input-nubr33')
    try:

        if request.method=='POST' and 'input-nubr33' in request.form:
            qtd_investir = float(request.form.get('input-qtd-investir'))
            resposta_nubr33 = round(qtd_investir*nubr33,2)
        if request.method=='POST' and 'input-mxrf11' in request.form:
            qtd_investir = float(request.form.get('input-qtd-investir'))
            resposta_mxrf11 = round(qtd_investir*mxrf11,2)
        if request.method=='POST' and 'input-hash11' in request.form:
            qtd_investir = float(request.form.get('input-qtd-investir'))
            resposta_hash11 = round(qtd_investir*hash11,2)
        if request.method=='POST' and 'input-itub3' in request.form:
            qtd_investir = float(request.form.get('input-qtd-investir'))
            resposta_itub3 = round(qtd_investir*itub3,2)
    except:
        print("Erro")
    return render_template('index.html', resposta_nubr33 = resposta_nubr33, resposta_mxrf11 = resposta_mxrf11, resposta_hash11 = resposta_hash11, resposta_itub3 = resposta_itub3)
if __name__ == "__main__":
  app.run()
