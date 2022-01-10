from flask import Blueprint

views=Blueprint(__name__,"views")

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")
