from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    # Here you would typically fetch data from your database or another source
    data = {
        "nodes": [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 15},
            {"id": 4, "value": 12},
            {"id": 5, "value": 12},
            {"id": 6, "value": 12},
            {"id": 7, "value": 13},
            # Add more nodes as needed
        ],
        "links": [
            {"source": 1, "target": 2}
            # Add more links as needed
        ]
    }
    return jsonify(data)


@app.route('/api/data2')
def get_data2():
    # Generar datos para el gráfico de red
    num_nodes = 10
    num_links = 15

    # Generar nodos aleatorios con identificadores únicos
    nodes = [{'id': i} for i in range(num_nodes)]

    # Generar enlaces aleatorios entre los nodos
    links = [{'source': random.randint(0, num_nodes - 1), 'target': random.randint(0, num_nodes - 1)} for _ in range(num_links)]

    data = {
        'nodes': nodes,
        'links': links
    }

    return jsonify(data)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='127.0.0.1', port=5000, debug=True)
