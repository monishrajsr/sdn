from sklearn.linear_model import LinearRegression

# Training data
X = [[500], [1000], [1500], [2000], [2500]]
y = [50, 100, 150, 200, 250]

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_price(size: int) -> float:
    """Predict house price given size in sq. ft."""
    return model.predict([[size]])[0]

if _name_ == "_main_":
    print("Predicted price for 3000 sq. ft house:", predict_price(3000), "lakhs")
