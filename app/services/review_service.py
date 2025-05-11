from app.models.review_model import ReviewRequest, FeedbackResponse
from app.ai_mock.ai_analyzer import AIMockAnalyzer


class ReviewService:
    """
    Service class to process product reviews and generate feedback.
    """

    def __init__(self):
        """
        Initializes the ReviewService with an AI mock analyzer.
        """
        self.ai_analyzer = AIMockAnalyzer()

    def process_review(self, review_request: ReviewRequest) -> FeedbackResponse:
        """
        Processes a review request and returns feedback using the AI mock analyzer.
        """
        text = review_request.text
        sentiment = self.ai_analyzer.analyze_sentiment(text)
        readability_score = self.ai_analyzer.calculate_readability(text)
        suggestions = self.ai_analyzer.suggest_improvements(text)
        return FeedbackResponse(
            sentiment=sentiment,
            readability_score=readability_score,
            suggestions=suggestions
        )
