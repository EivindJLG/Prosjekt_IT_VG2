from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

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
        print("Could not connect to database.")
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

    return render_template('index.html', produkter=products)


if __name__ == '__main__':
    create_table()     # <-- makes sure table exists when starting Flask
    app.run(host="0.0.0.0", port=6767, debug=True)