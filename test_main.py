import pytest
from unittest.mock import patch, MagicMock
from main import distilled_student_sentiment_classifier

# Mock the distilled_student_sentiment_classifier from transformers
@patch('main.distilled_student_sentiment_classifier', return_value=[{'label': 'POSITIVE', 'score': 0.9}])
def test_sentiment_classification(mocked_pipeline):
    # Given
    test_text = "This is a test text."

    # When
    result = distilled_student_sentiment_classifier(test_text)

    # Then
    mocked_pipeline.assert_called_once_with(test_text)
    assert result == [{'label': 'POSITIVE', 'score': 0.9}]

if __name__ == "__main__":
    pytest.main()
