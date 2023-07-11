from flask import Flask, jsonify, request
import pymssql

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/primary_key', methods=['GET', 'POST'])
def get_primary_key():
    try:
        if request.method == 'GET':
            # Connect to the SQL Server database
            conn = pymssql.connect(
                host='hostname',
                user='name',
                password='123',
                database='db'
            )

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Execute a SELECT query to retrieve the primary key
            cursor.execute("SELECT * from table")  # Replace 'your_table' with your actual table name

            # Fetch the primary key value
            primary_key = cursor.fetchone()[0]

            # Close the database connection
            conn.close()

            # Return the primary key as JSON response
            return jsonify({'primary_key': primary_key})

        elif request.method == 'POST':
            # Handle the POST request if needed
            # Add your POST request handling code here
            return jsonify({'message': 'POST request handled'})

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(str(e))
        print (e)
        # Return a JSON response with the error message
        return jsonify({'error': 'Internal Server Error'}), 500
    

if __name__ == '__main__':
    app.run(port=9994, debug=True)
