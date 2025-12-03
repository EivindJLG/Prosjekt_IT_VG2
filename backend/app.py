from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MariaDB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'eivind'
app.config['MYSQL_PASSWORD'] = 'deeznuts'
app.config['MYSQL_DB'] = 'Prosjekt'

mysql = MySQL(app)