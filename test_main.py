import pytest
from unittest.mock import MagicMock

# Import the main module
import main

def test_main():
    # Set up the mocks
    mock_button = MagicMock(return_value=True)
    mock_text_input = MagicMock(return_value="This is a positive text.")
    mock_pipeline = MagicMock(return_value=[
        {"label": "Positive", "score": 0.9},
        {"label": "Negative", "score": 0.05},
        {"label": "Neutral", "score": 0.05},
    ])

    # Mock the st module
    mock_st = MagicMock()
    main.st = mock_st

    # Call the main function
    main.main()

    # Check if the output is correct
    assert mock_pipeline.called
    assert mock_button.called
    assert mock_text_input.called
    assert mock_st.subheader.called
    assert mock_st.write.called

if __name__ == "__main__":
    pytest.main([__file__])
