from flask import Flask, request, jsonify
import data
import model

app = Flask(__name__)

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    try:
        data_dict = request.get_json()
        areaCategory = data_dict['areaCategory']
        Floor = data_dict['Floor']
        Storage = data_dict['Storage']
        publicTransport = data_dict['publicTransport']
        publicParking = data_dict['publicParking']

        df = data.load_data()
        df = data.preprocess_data(df)
        trained_model = model.train_decision_tree(df)

        prediction = model.predict_score(trained_model, areaCategory, Floor, Storage, publicTransport, publicParking)

        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
