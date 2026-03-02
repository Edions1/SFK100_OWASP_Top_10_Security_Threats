from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    nome = request.args.get("nome", "")
    # VULNERÁVEL: insere input direto no HTML sem sanitizar
    return f"""
    <html>
        <body>
            <h1>Olá {nome}</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)