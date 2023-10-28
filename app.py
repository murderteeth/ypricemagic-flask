import os
os.environ['BROWNIE_NETWORK_ID'] = 'mainnet'
os.environ['WEB3_INFURA_PROJECT_ID'] = '********'
os.environ['ETHERSCAN_TOKEN'] = '********'

print('Ahoy 1')

from flask import Flask, request, jsonify
from y import get_price

app = Flask(__name__)

@app.route('/yprice', methods=['GET'])
def price():
    token = request.args.get('token')
    block = request.args.get('block')
    
    if not token or not block:
        return jsonify({"error": "Missing parameters"}), 400
    
    try:
        price = get_price(token, block)
        return jsonify({"price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
