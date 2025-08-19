from ybu import predict_price

def test_prediction_for_known_value():
    # For 1000 sq. ft, price should be ~100 (exact because data is linear)
    assert round(predict_price(1000)) == 100

def test_prediction_for_unseen_value():
    # For 3000 sq. ft, model should predict ~300
    assert round(predict_price(3000)) == 300
