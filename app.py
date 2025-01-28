import matplotlib

matplotlib.use("Agg")

from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("action") == "Histogram":
            hist_data = request.form.get("hist_data")
            data = list(map(float, hist_data.split(",")))

            plt.figure()
            plt.hist(data, bins=10, color="blue", alpha=0.7, edgecolor="black")
            plt.title("Histogram")
            plt.xlabel("Value")
            plt.ylabel("Frequency")

            image_path = os.path.join("static", "histogram.png")
            plt.savefig(image_path)
            plt.close()

            return redirect(url_for("histogram"))

        function = request.form.get("function")
        x_from = float(request.form.get("x_from"))
        x_to = float(request.form.get("x_to"))
        color = request.form.get("color")

        x = np.linspace(x_from, x_to, 100)

        if function == "sin":
            y = np.sin(x)
        elif function == "cos":
            y = np.cos(x)
        elif function == "x^2":
            y = x**2
        elif function == "sqrt":
            y = np.sqrt(x)

        plt.figure()
        plt.plot(x, y, color=color)
        plt.title(f"Plot of {function} from {x_from} to {x_to}")
        plt.xlabel("x")
        plt.ylabel(function)

        image_path = os.path.join("static", "plot.png")
        plt.savefig(image_path)
        plt.close()

        return redirect(url_for("plot"))

    return render_template("index.html")


@app.route("/plot")
def plot():
    return render_template("plot.html")


@app.route("/histogram")
def histogram():
    return render_template("histogram.html")


if __name__ == "__main__":
    app.run(debug=True)
