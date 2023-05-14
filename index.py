from flask import Flask, render_template
from database import SupabaseDB


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    data = SupabaseDB.supabase.table("lifer_list").select("*").execute()
    return render_template("list.html", data=data.data)

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/2023")
def big_year():
    data = SupabaseDB.supabase.table("2023_herps").select("*").execute()
    return render_template("2023.html", data=data.data)
