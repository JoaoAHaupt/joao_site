from flask import Flask, render_template

app = Flask(__name__)
lista_produtos = [
    {"id":0,"nome": "Sugar bombs", "descricao": "Marketed across the United States as having an explosive great taste, the Sugar Bombs contain no explosives, but an overabundance of sugar frosting on each of the uniquely shaped wheat cereals, resembling the Fat Man, or perhaps more relevantly, a mini nuke. Served with milk, it made for a breakfast full of carbohydrates and little else. It was marketed at children, with added promotions to increase sales, such as Captain Cosmos decoder rings", "preco":23},
    {"id":1,"nome": "Nuka Cola", "descricao": "Nuka-Cola entered the beverage market in 2044, with the invention of the soft drink by John-Caleb Bradberton after two years of experimentation. It contained 120% of the recommended daily allowance of sugar, and took the United States market by storm, and within a year could be purchased nationwide.", "preco":0.06},
    {"id": 2, "nome": "BlamCo Mac & Cheese", "descricao": "Mac & Cheese is a pre-packaged, highly processed food product found across the wasteland. BlamCo's instant version of the classic macaroni and cheese dish (elbow macaroni with white sauce and cheese) was packed with preservatives and sold in green or blue carton packages, with an EZ-Pull pour spout to make preparation easier. Like most pre-War packaged food, it doesn't have an expiration date, making it one of the choices for supplying troops on the frontlines the Brotherhood of Steel", "preco": 5},
    {"id": 3, "nome": "Cram", "descricao": "A commonplace element of pre-War cuisine in the United States, thanks to pervasive promotional campaigns, cram refers to a particular type of precooked, spiced, and highly preserved meat that can remain edible for centuries. Produced in vast quantities to remedy food shortages, supply school lunches, and provide protein to deployed soldiers, Cram comes in an easily openable can that's highly prized by survivalists and was used as a substitute for many meals before and after the War, including clam chowder. The ubiquitous nature led to it becoming a common expression among wastelanders, with cram opening referring to opening a particularly resistant can of food.", "preco": 0.5}
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/produtos")
def func_produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route("/produtos/<nome_produto>")
def detalhe_produto(nome_produto):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome_produto.lower():
            return render_template('produto.html', produto=produto)
    return 'Produto não encontrado'

if __name__ == "__main__":
    app.run(debug=True)
