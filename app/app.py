from flask import Flask, jsonify
import cx_Oracle
import os

app = Flask(__name__)

# Set Oracle Database connection information
oracle_user = "appuser"
oracle_password = "123456"
oracle_pdb_service = "xepdb1"  # Replace with your pluggable database service name
oracle_dsn = cx_Oracle.makedsn("192.168.1.3", "1521", service_name=oracle_pdb_service)

# Define a route to execute the select query
@app.route('/')
def execute_query():
    try:
        # Establish Oracle Database connection
        connection = cx_Oracle.connect(oracle_user, oracle_password, oracle_dsn)

        # Create a cursor
        cursor = connection.cursor()

        # Sample select query, replace with your query
        query = "SELECT * FROM v$instance;"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries for JSON response
        result = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Return the result as JSON
        return jsonify(result)

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Database Error: {error.message}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)

