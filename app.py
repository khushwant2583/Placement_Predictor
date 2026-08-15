import os
import numpy as np
import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")  # optional, only if you scaled features during training

# ---- Load your trained model once at startup ----
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH) if os.path.exists(SCALER_PATH) else None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True) or {}

    try:
        iq = float(data["iq"])
        cgpa = float(data["cgpa"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Send JSON like {'iq': 110, 'cgpa': 7.5}"}), 400

    # IMPORTANT: feature order here must match the order used when you
    # trained the model. Your notebook builds X from df.iloc[:, 0:2] where
    # df's columns are (cgpa, iq, placement), so the trained order is
    # [cgpa, iq] -- NOT [iq, cgpa]. If you change how X is built, update this.
    features = np.array([[cgpa, iq]])

    if scaler is not None:
        features = scaler.transform(features)

    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(features)[0][1])
    elif hasattr(model, "decision_function"):
        raw_score = float(model.decision_function(features)[0])
        probability = float(1 / (1 + np.exp(-raw_score)))
    else:
        # Model only supports hard predict() (0/1) — no real probability available
        probability = float(model.predict(features)[0])

    return jsonify({
        "probability": probability,
        "placed": probability >= 0.5
    })


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
