#!/usr/bin/python3

from flask import Flask, request, render_template, url_for
import os

#from LED import *



project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')



app=Flask(__name__, template_folder=template_path)
#app.debug = True   # Not for production


#HomeLEDController application
@app.route("/", methods=["GET", "POST"])
def homeLEDController():

	if request.method == "POST":
	    return render_template("homeLEDController.html")

	else:
		return render_template("homeLEDController.html")


if __name__=="__main__":
	app.run(debug=True, host='0.0.0.0')
