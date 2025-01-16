from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Libera o acesso ao bot por outros programas (como o frontend)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    if "horário de funcionamento" in user_message.lower():
        response = "Estamos abertos de segunda a sexta, das 8h às 18h."
    elif "suporte" in user_message.lower():
        response = "Você pode falar com o suporte pelo email suporte@empresa.com."
    else:
        response = "Desculpe, não entendi sua pergunta."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
