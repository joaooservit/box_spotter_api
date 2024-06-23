from flask import Flask, request
from flask_restful import Resource, Api
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/spotter', methods=['POST'])
def spotter():
    try:
        data = request.get_json()
    except Exception as e:
        return f'Invalid payload: {e}', 400
    else:
        if data is None:
            return 'Empty payload', 400
    finally:
        company = data.get("Lead", {}).get("Company", "")
    
        data_str = json.dumps(data, ensure_ascii=False)  

        with open(f"spotter_{company}_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.json", "w") as file:
            file.write(data_str)
        
        return 'Payload saved successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

