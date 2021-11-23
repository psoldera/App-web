from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

filmes = [
    {"nome_filme": "Star Wars - A vingança dos Sith", "nota_publico": 60, "nota_critica": 80},
    {"nome_filme": "Doutor Estranho", "nota_publico": 85, "nota_critica": 89},
    {"nome_filme": "Aquaman", "nota_publico": 74, "nota_critica": 65},
    {"nome_filme": "Questão de Tempo", "nota_publico": 81, "nota_critica": 69},
    {"nome_filme": "As Vantagens de Ser Invisivel", "nota_publico": 89, "nota_critica": 85},
    {"nome_filme": "Projeto X", "nota_publico": 61, "nota_critica": 28},
]

@app.route('/')
def index():
    return render_template('index.html', lista=filmes)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome_filme = request.form['nome_filme']
    nota_publico = request.form['nota_publico']
    nota_critica = request.form['nota_critica']
    novos_filmes = {'nome_filme': nome_filme, 'nota_publico': nota_publico, 'nota_critica': nota_critica}

    filmes.append(novos_filmes)
    
    return redirect('https://5000-yellow-horse-ve3m6bqg.ws-us17.gitpod.io/')

@app.route('/buscar', methods=['POST'])
def buscar():
    lista_filme = []
    pesquisa = request.form['pesquisa']
    if pesquisa == "":
        return render_template('erro.html')
    for filme in filmes: 
        if pesquisa.lower() in filme['nome_filme'].lower():
            lista_filme.append(filme)
    return render_template('buscar.html', lista_filme=lista_filme)

@app.route('/deletar', methods=['POST'])
def deletar():
    deleta = request.form['deleta']
    if deleta == "":
        return render_template('erro.html')
    for filme in filmes:
        if filme['nome_filme'].lower() == deleta.lower() :
            filmes.remove(filme)
    return redirect('https://5000-yellow-horse-ve3m6bqg.ws-us17.gitpod.io/')

    
app.run(debug=True)