from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/activites", methods=["POST","GET"])
def activites():
    return render_template("activites.html")
      

# VOUCHER 

@app.route("/voucher", methods=["POST","GET"])
def voucher():
    return render_template("voucher.html")

# BLOGS

@app.route("/blogs", methods=["POST","GET"])
def blogs():
    return render_template("blogs.html")





#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)