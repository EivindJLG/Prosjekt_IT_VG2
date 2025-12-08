from flask import Flask, render_template, url_for
import mysql.connector
import os

# Dir som leder til frontend mapper
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #Prosjektet
TEMPLATE_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'frontend', 'static')

# Flask app med dir som leder til template og static folder
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Database kobling
def get_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",    
            user="eivind",       
            password="eivind123",
            database="Prosjekt" 
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route('/')
def index():
    conn = get_db()
    if conn is None:
        return "Kunne ikke koble til databasen"
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produkter;")
    products = cursor.fetchall()
    cursor.close()
    conn.close()


    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767, debug=True)