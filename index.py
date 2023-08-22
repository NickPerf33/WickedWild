from flask import Flask, render_template
from database import SupabaseDB


app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = "wickedwild.life"

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

@app.route("/", subdomain="shadow")
def shadow():
    return render_template("shadow.html")

@app.route("/reapers", subdomain="shadow")
def reapers():
    #data = SupabaseDB.supabase.table("reapers").select("*").execute()
    #return render_template("team.html", data=data.data)
    return render_template("team.html")
    
@app.route("/nor-easters", subdomain="shadow")
def nor_easters():
    #data = SupabaseDB.supabase.table("nor_easters").select("*").execute()
    #return render_template("team.html", data=data.data)
    return render_template("team.html")

@app.route("/black-squirrels", subdomain="shadow")
def black_squirrels():
    #data = SupabaseDB.supabase.table("black_squirrels").select("*").execute()
    #return render_template("team.html", data=data.data)
    return render_template("team.html")

@app.route("/free-agents", subdomain="shadow")
def free_agents():
    #data = SupabaseDB.supabase.table("free_agents").select("*").execute()
    #return render_template("team.html", data=data.data)
    return render_template("team.html")
