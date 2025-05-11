import unittest
from app.services.review_service import ReviewService
from app.models.review_model import ReviewRequest


class TestReviewService(unittest.TestCase):
    """
    Unit tests for the ReviewService class.
    """

    def setUp(self):
        """
        Set up method to create a ReviewService instance before each test.
        """
        self.review_service = ReviewService()

    def test_process_positive_review(self):
        """
        Tests processing a positive review.
        """
        review = ReviewRequest(
            text="This product is excellent, I really loved it!")
        feedback = self.review_service.process_review(review)
        self.assertEqual(feedback.sentiment, "positive")

    def test_process_negative_review(self):
        """
        Tests processing a negative review.
        """
        review = ReviewRequest(
            text="What a terrible product, it didn't work at all.")
        feedback = self.review_service.process_review(review)
        self.assertEqual(feedback.sentiment, "negative")

    def test_process_neutral_review(self):
        """
        Tests processing a neutral review.
        """
        review = ReviewRequest(text="This is an average product.")
        feedback = self.review_service.process_review(review)
        self.assertEqual(feedback.sentiment, "neutral")

    def test_process_short_review(self):
        """
        Tests processing a short review to ensure suggestions are provided.
        """
        review = ReviewRequest(text="I liked it.")
        feedback = self.review_service.process_review(review)
        self.assertIn("Consider adding more details to your review.", feedback.suggestions)

    def test_readability_calculation(self):
        """
        Tests the readability calculation for a moderately long review.
        """
        review = ReviewRequest(
            text="This is a review of moderate length to test the readability score calculation.")
        feedback = self.review_service.process_review(review)
        self.assertGreater(feedback.readability_score, 3.0)
        # Adjust upper bound based on your logic
        self.assertLessEqual(feedback.readability_score, 7.0)

    def test_suggestion_for_uncertainty(self):
        """
        Tests if a suggestion is given for uncertain language.
        """
        review = ReviewRequest(text="I think this might be a good product.")
        feedback = self.review_service.process_review(review)
        self.assertIn("Try to be more direct in your opinions.", feedback.suggestions)

if __name__ == '__main__':
    unittest.main()
