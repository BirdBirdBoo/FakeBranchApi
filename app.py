from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
offices = [
    {"id": 1, "city": "Kyiv", "rent": 15000},
    {"id": 2, "city": "Lviv", "rent": 8000},
    {"id": 3, "city": "Odesa", "rent": 6000},
    {"id": 4, "city": "Kyiv", "rent": 20000},
    {"id": 5, "city": "Kharkiv", "rent": 9000},
    {"id": 6, "city": "Dnipro", "rent": 12000},
    {"id": 7, "city": "Kyiv", "rent": 25000},
    {"id": 8, "city": "Lviv", "rent": 10000},
    {"id": 9, "city": "Kyiv", "rent": 18000},
    {"id": 10, "city": "Odesa", "rent": 7000},
    {"id": 11, "city": "Kharkiv", "rent": 8000},
    {"id": 12, "city": "Dnipro", "rent": 15000},
    {"id": 13, "city": "Kyiv", "rent": 22000},
    {"id": 14, "city": "Lviv", "rent": 12000},
    {"id": 15, "city": "Kyiv", "rent": 28000}
]


# Routes
@app.route('/branches')
def get_offices():
    return jsonify({"offices": offices})


if __name__ == '__main__':
    app.run(debug=False)
