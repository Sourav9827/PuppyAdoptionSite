from myproject import app
from flask import render_template

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

@app.errorhandler(Exception)
def page_not_found(e):
    return render_template('404.html')

if __name__=="__main__":
	app.run(debug=True)
