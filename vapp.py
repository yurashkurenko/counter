from flask import Flask, request, jsonify
from vedis import Vedis
from iddevdb import getdevparajsonfromid
app = Flask(__name__)

# Функция для получения параметров из базы данных Vedis

@app.route('/get_device_params', methods=['POST'])
def get_device_params_route():
    device_id = request.form.get('device_id')
    getdevparajsonfromid(device_id)
    if device_id:
        try:
        getdevparajsonfromid(device_id)
            return getdevparajsonfromid(device_id)
        except:
            return jsonify({'error': 'Не удалось получить параметры устройства'}), 404
    else:
        return jsonify({'error': 'Не указан deviceid'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)