from flask import Flask, request, jsonify
from vedis import Vedis

app = Flask(__name__)

# Функция для получения параметров из базы данных Vedis
def get_device_params(device_id):
    with Vedis() as db:
        wifi = db.Get(f"wifi_{device_id}").decode()
        wifipass = db.Get(f"wifipass_{device_id}").decode()
        device_name = db.Get(f"device_name_{device_id}").decode()
        poll_period = db.Get(f"poll_period_{device_id}").decode()
        chat_number = db.Get(f"chat_number_{device_id}").decode()
        return wifi, wifipass, device_name, poll_period, chat_number

@app.route('/get_device_params', methods=['POST'])
def get_device_params_route():
    device_id = request.form.get('device_id')
    if device_id:
        try:
            wifi, wifipass, device_name, poll_period, chat_number = get_device_params(device_id)
            return jsonify({
                'wifi': wifi,
                'wifipass': wifipass,
                'device_name': device_name,
                'poll_period': poll_period,
                'chat_number': chat_number
            })
        except:
            return jsonify({'error': 'Не удалось получить параметры устройства'}), 404
    else:
        return jsonify({'error': 'Не указан deviceid'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
