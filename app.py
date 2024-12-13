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
        <title>DevOps Portfolio</title>
        <style>
            body {
                background-color: #333; /* Cinza escuro */
                color: white;
                text-align: center;
                padding: 20px;
            }
            .content {
                margin-top: 20px;
                text-align: left;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    </head>
    <body>
        <h1>Cloud & DevOps</h1>
        <p>Bem-vindo ao portfólio de Cristiano Feliciano da Silva.</p>

        <div class="content">
            <h2>A Importância de Ter um Profissional DevOps na Sua Empresa</h2>
            <p>Em um mundo digital cada vez mais acelerado, as empresas precisam entregar produtos e serviços com rapidez e qualidade. Isso não seria possível sem a implementação de práticas eficientes de desenvolvimento e operações. E é exatamente nesse cenário que a figura do profissional <strong>DevOps</strong> se torna essencial.</p>
            <p>O papel de um DevOps vai além da simples automação de processos. Ele é responsável por integrar as equipes de desenvolvimento e operações, criando uma cultura colaborativa que visa a agilidade, a eficiência e a redução de erros durante todo o ciclo de vida do software. Por meio de práticas como automação de pipelines, monitoramento contínuo, integração e entrega contínua (CI/CD), o DevOps garante que a infraestrutura, o código e as operações estejam sempre alinhados.</p>
            <p>Quando uma empresa conta com um profissional DevOps, ela é capaz de:</p>
            <ul>
                <li><strong>Acelerar o Time-to-Market:</strong> A automação de processos e a integração contínua permitem que novas funcionalidades sejam entregues com mais rapidez e sem comprometer a qualidade.</li>
                <li><strong>Reduzir Custos:</strong> Com a automação de tarefas repetitivas e a otimização de recursos, as empresas conseguem reduzir custos operacionais e melhorar a utilização de infraestrutura.</li>
                <li><strong>Garantir Qualidade e Segurança:</strong> DevOps não é apenas sobre velocidade, mas também sobre garantir que as entregas estejam seguras e livres de falhas. O monitoramento contínuo e as práticas de testes automatizados ajudam a detectar e corrigir problemas antes que eles impactem o usuário final.</li>
                <li><strong>Melhorar a Colaboração:</strong> A eliminação de silos entre as equipes de desenvolvimento e operações promove um ambiente de trabalho mais colaborativo e eficiente.</li>
            </ul>
            <p>Se você busca otimizar a infraestrutura da sua empresa, acelerar o desenvolvimento de software e garantir maior qualidade e segurança nas entregas, ter um profissional DevOps é o caminho certo. Ao investir em DevOps, você investe em inovação, agilidade e eficiência.</p>
            <p>Para mais informações sobre como transformar sua infraestrutura e processos com práticas DevOps, fique à vontade para conectar-se comigo no <a href="https://github.com/CrisFeliciano/" style="color: #f8f9fa;">LinkedIn</a>.</p>
        </div>

        <div class="gifs" style="margin-top: 20px; display: flex; justify-content: center; gap: 20px;">
            <img src="https://media.giphy.com/media/3o7TKP9lnC9eIngjDq/giphy.gif" alt="DevOps Gif 1" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" alt="DevOps Gif 2" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            <img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" alt="DevOps Gif 3" style="width: 150px; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)
