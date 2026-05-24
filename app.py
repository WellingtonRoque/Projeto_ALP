from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <html>

        <head>

            <title>Sistema Comercial</title>

            <style>

                body {

                    font-family: Arial;
                    background-color: #f4f4f4;
                    padding: 40px;
                    text-align: center;

                }

                h1 {

                    color: #2c3e50;

                }

                .container {

                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    width: 60%;
                    margin: auto;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);

                }

                ul {

                    list-style: none;
                    padding: 0;

                }

                li {

                    padding: 10px;

                }

            </style>

        </head>

        <body>

            <div class="container">

                <h1>🚀 Sistema de Gestão Comercial</h1>

                <p>
                    Projeto desenvolvido na disciplina de
                    Algoritmos e Lógica de Programação.
                </p>

                <h2>✅ Funcionalidades</h2>

                <ul>

                    <li>📦 Cadastro de Produtos</li>

                    <li>👥 Cadastro de Clientes</li>

                    <li>💾 Persistência em Arquivos</li>

                    <li>🛡 Tratamento de Erros</li>

                    <li>🔎 Busca de Produtos</li>

                    <li>🗑 Remoção de Produtos</li>

                </ul>

                <h2>🛠 Tecnologias</h2>

                <p>
                    Python • Flask • Git • GitHub • Render
                </p>

                <h2>☁ Deploy</h2>

                <p>
                    Sistema publicado utilizando Flask + Render
                </p>

            </div>

        </body>

    </html>
    """


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)