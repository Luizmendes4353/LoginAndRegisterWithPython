# fazer as rotas
# estabelecer conexao com o banco de dados
# criar banco de dados
# funcao inser novos usuarios
# funcao de login(n sei como fazer)

from flask import Flask, render_template, url_for, redirect, request
import sqlite3
import os

app = Flask(__name__)

#conectando banco de dados
db_file = "Users.db"
#caso nao tiver o db Users ele cria mas se tiver ele usa o existente
if not os.path.exists(db_file):
    con = sqlite3.connect("Users.db")
    cursor = con.cursor()

    #create table
    cursor.execute('''CREATE TABLE User(
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE,
                password BLOB
    )''')

    print("User table created successfully")
    con.close()

else:
    print(f"The file '{db_file}' already exists. Using the existing database.")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        # Inserindo novo usuario no banco de dados
        cursor.execute("INSERT INTO User (email, password) VALUES (?, ?)",(email , password))
        con.commit()
        # redireciondo a pagina login 
        return redirect(url_for ("login"))
    
    return render_template('register.html')



@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug = True)



