from fastapi import APIRouter, Depends
from app.models.review_model import ReviewRequest, FeedbackResponse
from app.services.review_service import ReviewService

router = APIRouter()


@router.post("/reviews", response_model=FeedbackResponse)
async def analyze_review(review_request: ReviewRequest, review_service: ReviewService = Depends()):
    """
    Endpoint to receive a product review and return AI-generated (simulated) feedback.
    """
    feedback = review_service.process_review(review_request)
    return feedback
