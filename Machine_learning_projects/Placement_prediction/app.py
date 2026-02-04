from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# absolute path handling (VERY IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pipeline = pickle.load(open(os.path.join(BASE_DIR, "placement_pipeline.pkl"), "rb"))
label_encoder = pickle.load(open(os.path.join(BASE_DIR, "label_encoder.pkl"), "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "gender": request.form["gender"],
        "ssc_p": float(request.form["ssc_p"]),
        "ssc_b": request.form["ssc_b"],
        "hsc_p": float(request.form["hsc_p"]),
        "hsc_b": request.form["hsc_b"],
        "hsc_s": request.form["hsc_s"],
        "degree_p": float(request.form["degree_p"]),
        "degree_t": request.form["degree_t"],
        "workex": request.form["workex"],
        "etest_p": float(request.form["etest_p"]),
        "specialisation": request.form["specialisation"],
        "mba_p": float(request.form["mba_p"])
    }

    input_df = pd.DataFrame([data])

    prediction = pipeline.predict(input_df)
    result = label_encoder.inverse_transform(prediction)[0]

    return render_template(
        "index.html",
        prediction_text=f"Placement Status: {result}"
    )

if __name__ == "__main__":
    app.run(debug=True)
    