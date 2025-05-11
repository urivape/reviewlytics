from pydantic import BaseModel


class ReviewRequest(BaseModel):
    """
    Model for the review analytics request
    """
    text: str


class FeedbackResponse(BaseModel):
    """
    Model for the review feedback response
    """
    sentiment: str
    readability_score: float
    suggestions: list[str]
