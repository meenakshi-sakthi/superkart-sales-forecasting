from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import joblib
model = joblib.load(
	"superkart_model.joblib"
)
superkart_api = Flask(__name__)
@superkart_api.post("/v1/predict")
def predict_sales():
	payload = request.get_json()
	input_df = pd.DataFrame([payload])
	prediction = model.predict(input_df)
	return jsonify({
    	"predicted_sales":
    	float(prediction[0])
	})
@superkart_api.post("/v1/predictbatch")
def predict_batch():
	uploaded_file = request.files["file"]
	batch_df = pd.read_csv(
    	uploaded_file
	)
	predictions = model.predict(
    	batch_df
	)
	return jsonify({
    	str(i): float(pred)
    	for i, pred in enumerate(
        	predictions
    	)
	})
if __name__ == "__main__":
	superkart_api.run(
    	host="0.0.0.0",
    	port=7860
	)

