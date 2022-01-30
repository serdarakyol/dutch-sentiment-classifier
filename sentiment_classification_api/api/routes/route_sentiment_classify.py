from fastapi import APIRouter, Depends
from starlette.requests import Request

from sentiment_classification_api.core import security
from sentiment_classification_api.models.model_sentiment_classify import SentimentClassifyRequest, SentimentClassifyResponse
from sentiment_classification_api.services.service_sentiment_classify import SentimentClassify

router_classify = APIRouter()

@router_classify.post("/sentiment_classify", response_model=SentimentClassifyResponse, name="classifier")
def post_recommend(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    request_data: SentimentClassifyRequest = None,
) -> SentimentClassifyResponse:

    classifier = SentimentClassify()
    response_data = classifier.classify(request_data)

    return response_data