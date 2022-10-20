from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "key_here"


@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def submit_word():
    session["Name"]=request.form["Name"]
    session["Dojo_Location"]=request.form["Dojo_Location"]
    session["Favorite_Language"]=request.form["Favorite_Language"]
    session["Comments"]=request.form["Comments"]

    return redirect("/results")


@app.route("/results")
def results_page():
    return render_template("results.html")

# @app.route("/process", methods=["POST"])
# def process_page():

#     print(request.form["name"])
#     print("Dojo_Location:" + request.form["Dojo_Location"])
#     print("Favorite_Language:" + request.form["Favorite_Language"])
#     print("Comments:" + request.form["Comments"])
#     return redirect("/")


# @app.route("/repeat/<word>/<int:times>")
# def repeater(word, times):
#     return render_template("marquee.html", display=word, times=times)

if __name__ == "__main__":
    app.run(debug=True)