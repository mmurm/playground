from flask import Flask, render_template    # Import Flask to allow us to create our app AND use render template
app = Flask(__name__)                       # Create a new instance of the Flask class called "app"
# @app.rout("/")                              # Directory Structure
# def function_name_here()                    #function AND variables brought in
#     print("send to console")
#     return render_template("index.html")    # Ensure you have render_template on line 1.  can pull in values by adding ("index.html", htmlValue=pythonValue), all values will be brought in as strings if want as value use int(x)


@app.route('/play')
def play():
    return render_template("index.html", times=3)	

@app.route("/play/<x>")
def play_x(x):
    return render_template("index.html", times=int(x))	

@app.route("/play/<x>/<color>")
def play_x_color(x, color):
    return render_template("index.html", times=int(x), color=color)	

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module       
    app.run(debug=True)    # Run the app in debug mode which keeps console open