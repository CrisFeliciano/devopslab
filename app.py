from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test</title>
    </head>
    <body style="background-color: #1e3c72; color: white; text-align: center; padding: 20px;">
        <h1>Cloud & DevOps</h1>
        <p>Bem-vindo ao portfólio de Cristiano Feliciano da Silva.</p>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)
