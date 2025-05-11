from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_positive_review_endpoint():
    """
    Tests the /reviews endpoint with a positive review.
    """
    response = client.post(
        "/reviews",
        json={"text": "This product is absolutely fantastic! I highly recommend it."}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_analyze_negative_review_endpoint():
    """
    Tests the /reviews endpoint with a negative review.
    """
    response = client.post(
        "/reviews",
        json={"text": "This is the worst product I have ever used. Do not buy it!"}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"

def test_analyze_neutral_review_endpoint():
    """
    Tests the /reviews endpoint with a neutral review.
    """
    response = client.post(
        "/reviews",
        json={"text": "This product is okay, nothing too special."}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"

def test_analyze_short_review_endpoint():
    """
    Tests the /reviews endpoint with a short review to check for suggestions.
    """
    response = client.post(
        "/reviews",
        json={"text": "Good."},
    )
    assert response.status_code == 200
    assert "Consider adding more details to your review." in response.json()["suggestions"]

def test_readability_score_is_present():
    """
    Tests if the readability score is included in the response.
    """
    response = client.post(
        "/reviews",
        json={"text": "A moderately lengthy review to test the presence of the readability score."}
    )
    assert response.status_code == 200
    assert "readability_score" in response.json()
    assert isinstance(response.json()["readability_score"], float)