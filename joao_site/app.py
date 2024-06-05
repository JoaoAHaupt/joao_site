from flask import Flask, render_template

app = Flask(__name__)
app.run(debug=True)
produtos = [
        {"nome": "Sugar bombs", "descricao":"Marketed across the United States as having an explosive great taste, the Sugar Bombs contain no explosives, but an overabundance of sugar frosting on each of the uniquely shaped wheat cereals, resembling the Fat Man, or perhaps more relevantly, a mini nuke. Served with milk, it made for a breakfast full of carbohydrates and little else. It was marketed at children, with added promotions to increase sales, such as Captain Cosmos decoder rings"},
        {"nome" : "Nuka Cola", "descricao": "Nuka-Cola entered the beverage market in 2044, with the invention of the soft drink by John-Caleb Bradberton after two years of experimentation.[1] It contained 120% of the recommended daily allowance of sugar, and took the United States market by storm, and within a year could be purchased nationwide.[2][3]"}
    
]

@app.route("/")
def lepo():
    return "<p>Hello, nome!</p>"

@app.route("/produtos")
def template():
    return render_template('produtos.html', produtos = produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return f'<h2>{produto["nome"]}</h2> <br> <p>{produto["descricao"]}</p>'
    return 'produto nao cadastrado'
