from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():

    mensagem = ""   #Variável para o print

    x = 1
    while x < 100:
        if x % 2 == 0:
            mensagem += ' - ' + str(x)  #Print
        x += 1
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
        app.run(debug=True)