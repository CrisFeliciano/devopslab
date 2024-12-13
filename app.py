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
        <div class="gifs" style="margin-top: 20px; display: flex; justify-content: center; gap: 20px;">
            <img src="https://media.giphy.com/media/3o7TKP9lnC9eIngjDq/giphy.gif" alt="DevOps Gif 1" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" alt="DevOps Gif 2" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            <img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" alt="DevOps Gif 3" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
