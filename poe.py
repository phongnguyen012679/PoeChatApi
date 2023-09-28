from flask import Flask, request, jsonify
from poe_api_wrapper import PoeApi

app = Flask(__name__)

@app.route('/PostMessage', methods=['POST'])
def PostMessage():
    try:
        data = request.get_json()
        message = data['message']

        client = PoeApi("E9Bf8qdjlnm0VEU5QlhasA%3D%3D")

        bot = "a2"

        response_str = ""

        for chunk in client.send_message(bot, message, chatCode="2l5bfgfwybj71bow43c"):
            response_str += chunk["response"]

        return jsonify({"response": response_str})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
