from model import predict_sentiment

def test_predict_sentiment():
    assert predict_sentiment("I am so happy today!") == "positive"

def test_predict_sentiment_negative():
    assert predict_sentiment("I am feeling very sad.") == "negative"

def test_predict_sentiment_neutral():
    assert predict_sentiment("I am just here.") == "neutral"