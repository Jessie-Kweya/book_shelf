from pickle import GET
from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2

app = Flask(__name__)
conn=psycopg2.connect(user="postgres",password="Have1m3t",host="localhost",port="5432")

cur = conn.cursor()
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/library")
def library_page():
    cur.execute("SELECT * from library;")
    records = cur.fetchall()
    print(records)
    return render_template("lib.html", library = records )

@app.route("/add_book", methods=["POST"])
def add_book():
    id= request.form["ID"]
    Title = request.form["Name"]
    Author=request.form["Author"]
    Serial=request.form["Serial"]
    

    cur.execute("INSERT INTO library (ID,Name,Author,Serial) VALUES (%s, %s, %s, %s)",(id,Title,Author,Serial))

    conn.commit()
    return redirect(url_for("library_page"))

@app.route("/delete/<int:ID>")
def delete(ID):
	cur.execute("DELETE FROM library WHERE ID=%s;",[ID])
	return redirect(url_for("library_page"))


if __name__ == "__main__":
    app.run()
