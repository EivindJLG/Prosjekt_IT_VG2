from flask import Flask, render_template, url_for
import mysql.connector
import os

# Dir som leder til frontend mapper
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project/
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

def create_table():
    conn = get_db()
    if conn is None:
        print("Kunne ikke koble til") 
        return

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produkter (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(100),
            price DECIMAL(10,2),
            description TEXT,
            image_url VARCHAR(255),
            stock INT DEFAULT 0
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

create_table()

@app.route('/')
def index():
    conn = get_db()
    if conn is None:
        return "Kunne ikke koble til databasen"
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produkter;")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', products=products)


if __name__ == '__main__':
    create_table()     # <-- makes sure table exists when starting Flask
    app.run(host="0.0.0.0", port=6767, debug=True)