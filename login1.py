from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    try:
        _json = request.json
        _password = _json['password']
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5433", database="postgres")
        cursor = connection.cursor()
        sql = "SELECT * FROM register WHERE password=%s"
        sql_where = (_password,)  # Include comma to make it a tuple
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row:
            result = {'message': 'You are logged in'}
        else:
            result = {'error': 'Sorry, invalid username'}
        return jsonify(result)

    except Exception as error:
        return jsonify({'error': str(error)})

if __name__ == '__main__':
    app.run()
