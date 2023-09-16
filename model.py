from sklearn import tree

def train_decision_tree(df):
    # Prepare data and train the decision tree model
    inputs = df.drop('Success category', axis=1)
    target = df['Success category']

    inputs_n = inputs.drop(['name', 'State', 'City', 'Type', 'lattitude', 'address', 'longitude',
                            'area (mÂ²)', 'storage', 'Public Transport', 'Public parking', 'rating',
                            'Number of reviews', 'Success Score '], axis=1)

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)

    return model

def predict_score(model, areaCategory, Floor, Storage, publicTransport, publicParking):
    prediction = model.predict([[areaCategory, Floor, Storage, publicTransport, publicParking]])
    return prediction
