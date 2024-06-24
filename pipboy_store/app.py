from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF,CNPJ

app = Flask(__name__)
lista_produtos = [
    {
        "id": 0,
        "nome": "Sugar Bombs",
        "descricao": "Marketed across the United States as having an explosive great taste, the Sugar Bombs contain no explosives, but an overabundance of sugar frosting on each of the uniquely shaped wheat cereals, resembling the Fat Man, or perhaps more relevantly, a mini nuke. Served with milk, it made for a breakfast full of carbohydrates and little else. It was marketed at children, with added promotions to increase sales, such as Captain Cosmos decoder rings",
        "preco": 23,
        "tipo": "food"
    },
    {
        "id": 1,
        "nome": "Nuka Cola",
        "descricao": "Nuka-Cola entered the beverage market in 2044, with the invention of the soft drink by John-Caleb Bradberton after two years of experimentation. It contained 120% of the recommended daily allowance of sugar, and took the United States market by storm, and within a year could be purchased nationwide.",
        "preco": 0.06,
        "tipo": "food"
    },
    {
        "id": 2,
        "nome": "BlamCo Mac & Cheese",
        "descricao": "Mac & Cheese is a pre-packaged, highly processed food product found across the wasteland. BlamCo's instant version of the classic macaroni and cheese dish (elbow macaroni with white sauce and cheese) was packed with preservatives and sold in green or blue carton packages, with an EZ-Pull pour spout to make preparation easier. Like most pre-War packaged food, it doesn't have an expiration date, making it one of the choices for supplying troops on the frontlines the Brotherhood of Steel",
        "preco": 5,
        "tipo": "food"
    },
    {
        "id": 3,
        "nome": "Cram",
        "descricao": "A commonplace element of pre-War cuisine in the United States, thanks to pervasive promotional campaigns, cram refers to a particular type of precooked, spiced, and highly preserved meat that can remain edible for centuries. Produced in vast quantities to remedy food shortages, supply school lunches, and provide protein to deployed soldiers, Cram comes in an easily openable can that's highly prized by survivalists and was used as a substitute for many meals before and after the War, including clam chowder. The ubiquitous nature led to it becoming a common expression among wastelanders, with cram opening referring to opening a particularly resistant can of food.",
        "preco": 0.5,
        "tipo": "food"
    },
    {"id": 4, "nome": "Fat Man", "descricao": "First entering service in September 2077 with the U.S. Army, the Fat Man is a shoulder-mounted mini nuke launcher. There is no longer a handle on the right side of the launcher, and instead two straight handles on the bottom. It also appears to be larger, with a rusted silver paint job.", "preco": 254, "tipo": "gun"},
    {"id": 5, "nome": "T-51", "descricao": "Formally designated Powered Infantry Armor Model T-51, it was created by West Tek under contract from the United States government, and represented the company's single largest contract. Following a ten year development cycle, the T-51 finally entered service in June 2076, after final testing at Fort Strong. The newly equipped units proved incredibly effective against People's Liberation Army force, and were instrumental to the success of Battle of Anchorage, commonly thought to be the series' debut on the battlefield. In particular, their use minimized casualties sustained by the military in the attack. It remains prized after the Great War for its protective qualities. A power armor frame is required to mount T-51 power armor, and pieces spawned can vary from A to F models.", "preco": 570, "tipo": "armor"}
]


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

    produto = {"id":len(lista_produtos), "nome": nome, "descricao": descricao, "preco":preco, "tipo":tipo}
    lista_produtos.append(produto)
    return redirect(url_for("func_produtos"))


@app.route("/produtos", methods=["GET"])
def func_produtos():
    tipo = request.args.getlist('tipo')
    if tipo:
        produtos_filtrados = [produto for produto in lista_produtos if produto["tipo"].lower() in tipo]
    else:
        produtos_filtrados = lista_produtos
    return render_template('produtos.html', produtos=produtos_filtrados, tipos = tipo)

@app.route("/produtos/<nome_produto>")
def detalhe_produto(nome_produto):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome_produto.lower() or str(produto["id"]) == nome_produto:
            return render_template('produto.html', produto=produto)
    return render_template('produto.html', produto=None)

@app.route("/produtos/tipo/<tipo_produto>")
def tipo_produto(tipo_produto):
    produtos_tipo = [produto for produto in lista_produtos if produto["tipo"].lower() == tipo_produto.lower()]
    return render_template('produtos.html', produtos=produtos_tipo)

if __name__ == "__main__":
    app.run(debug=True, port=8001)
