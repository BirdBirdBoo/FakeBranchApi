from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
offices = [
    {"id": 1, "city": "Kyiv", "rent": 15000},
    {"id": 2, "city": "Lviv", "rent": 12000},
    {"id": 3, "city": "Kharkiv", "rent": 20000},
    {"id": 4, "city": "Odessa", "rent": 18000},
    {"id": 5, "city": "Dnipro", "rent": 16000},
    {"id": 6, "city": "Zaporizhia", "rent": 14000},
    {"id": 7, "city": "Vinnytsia", "rent": 10000},
    {"id": 8, "city": "Poltava", "rent": 11000},
    {"id": 9, "city": "Chernivtsi", "rent": 13000},
    {"id": 10, "city": "Lutsk", "rent": 9000},
]


# Routes
@app.route('/branches')
def get_offices():
    return jsonify({"offices": offices})


if __name__ == '__main__':
    app.run(debug=False)
