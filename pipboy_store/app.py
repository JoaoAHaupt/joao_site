from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF,CNPJ

app = Flask(__name__)


def pegar_lista():
    with open('pipboy_store/produtos.csv', 'r') as file:
        lista_produtos = []
        for linha in file:
            id, nome, descricao, preco, tipo = linha.strip().split(",")
            produto = {
                "id": int(id),
                "nome": nome,
                "descricao": descricao,
                "preco": float(preco),
                "tipo": tipo
            }
            lista_produtos.append(produto)

        return lista_produtos


def registrar(nome, descricao, preco, tipo):
    lista_produtos = pegar_lista()
    with open("pipboy_store/produtos.csv", "a") as file:
        file.write("\n"+str(len(lista_produtos)+1)+","+nome +","+descricao+","+preco+","+tipo)       





@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cpf-validar", methods=['POST', 'GET'])
def cpf_validacao():
    if request.method == 'POST':
        cpf_obj = CPF()
        form_cpf = request.form['cpf']
        return render_template('cpf-validar.html', cpf = cpf_obj.validate(form_cpf))
    else:
        return render_template('cpf-validar.html', cpf = "")

@app.route("/cnpj-validar", methods=['POST', 'GET'])
def cnpj_validacao():
    if request.method == 'POST':
        cnpj_obj = CNPJ()
        form_cnpj = request.form['cnpj']
        return render_template('cnpj-validar.html', cnpj = cnpj_obj.validate(form_cnpj))
    else:
        return render_template('cnpj-validar.html', cnpj = "")

@app.route("/cnpj-gerador")
def cpf_gerador():
    cnpj_obj = CNPJ()
    return render_template('cnpj-gerador.html', cnpj = cnpj_obj.generate(mask=True))

@app.route("/cpf-gerador")
def cnpj_gerador():
    cpf_obj = CPF()
    return render_template('cpf-gerador.html', cpf = cpf_obj.generate(mask=True))

@app.route("/produtos/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/produtos", methods=['POST'])
def cadastrar_produto():
    nome = request.form['name']
    descricao = request.form['description']
    preco = request.form['price']
    tipo = request.form['type']

    registrar(nome, descricao, preco, tipo)
    return redirect(url_for("func_produtos"))


@app.route("/produtos", methods=["GET"])
def func_produtos():
    lista_produtos = pegar_lista()
    tipo = request.args.getlist('tipo')
    if tipo:
        produtos_filtrados = [produto for produto in lista_produtos if produto["tipo"].lower() in tipo]
    else:
        produtos_filtrados = lista_produtos
    return render_template('produtos.html', produtos=produtos_filtrados, tipos = tipo)

@app.route("/produtos/<nome_produto>")
def detalhe_produto(nome_produto):
    lista_produtos = pegar_lista()
    for produto in lista_produtos:
        if produto["nome"].lower() == nome_produto.lower() or str(produto["id"]) == nome_produto:
            return render_template('produto.html', produto=produto)
    return render_template('produto.html', produto=None)

@app.route("/produtos/tipo/<tipo_produto>")
def tipo_produto(tipo_produto):
    lista_produtos = pegar_lista()
    produtos_tipo = [produto for produto in lista_produtos if produto["tipo"].lower() == tipo_produto.lower()]
    return render_template('produtos.html', produtos=produtos_tipo)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
