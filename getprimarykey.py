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

           
            cursor = conn.cursor()

          
            cursor.execute("SELECT * from table")  
          
            primary_key = cursor.fetchone()[0]

            conn.close()

           
            return jsonify({'primary_key': primary_key})

        elif request.method == 'POST':
           
            return jsonify({'message': 'POST request handled'})

    except Exception as e:
        
        app.logger.error(str(e))
        print (e)
        
        return jsonify({'error': 'Internal Server Error'}), 500
    

if __name__ == '__main__':
    app.run(port=9994, debug=True)
