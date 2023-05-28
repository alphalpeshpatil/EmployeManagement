from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5433", database="postgres")
cursor = connection.cursor()
@app.route('/register', methods=['POST'])
def register():
    try:
        _json = request.json
        _username = _json['username']
        _email = _json['email']
        _password = _json['password']

        sql = """INSERT INTO register (first_name, email, password) VALUES (%s, %s, %s)"""
        cursor.execute(sql, (_username, _email, _password))  # Pass values as the second argument
        connection.commit()
        result = {'message': 'registration done successfully'}
        return jsonify(result)

    except Exception as error:
        return jsonify({'error': str(error)})

if __name__ == '__main__':
    app.run()
