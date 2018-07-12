#####################
# IMPORT DEPENDENCIES
######################

# flask (server)
from flask import(
    Flask, 
    render_template, 
    jsonify, 
    request,
    redirect)

#######################
# FLASK SET-UP
#######################
app = Flask(__name__)

#######################
# FLASK ROUTES
#######################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def charts():
    return render_template("1pg.html")

@app.route("/2")
def elements():
    return render_template("2pg.html")
    
@app.route("/3")
def login():
    return render_template("3pg.html")

if __name__ == "__main__":
    app.run(debug = True)