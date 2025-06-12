from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'product_db'
}

@app.route('/', methods=['GET', 'POST'])
def product_form():
    if request.method == 'POST':
        # Get data from form
        product_name = request.form['productName']
        price = float(request.form['price'])
        mfg_date = request.form['mfgDate']
        category = request.form['category']
        recyclable = request.form['recyclable'] == 'yes'

        try:
            # Connect to database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insert data
            sql = """
                INSERT INTO products (product_name, price, mfg_date, category, recyclable)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (product_name, price, mfg_date, category, recyclable)
            cursor.execute(sql, values)
            conn.commit()

            cursor.close()
            conn.close()

            return "✅ Product added successfully!"
        except Exception as e:
            return f"❌ Error: {e}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
