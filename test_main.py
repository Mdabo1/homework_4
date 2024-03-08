import pytest

@patch("streamlit.st", new_callable=pytest.Mock)
def test_main(self, mock_st):
    # Set up the mocks
    mock_button = MagicMock(return_value=True)
    mock_text_input = MagicMock(return_value="This is a positive text.")
    mock_pipeline = MagicMock(return_value=[
        {"label": "Positive", "score": 0.9},
        {"label": "Negative", "score": 0.05},
        {"label": "Neutral", "score": 0.05},
    ])

    # Call the main function
    main.main()

    # Check if the output is correct
    self.assertTrue(mock_pipeline.called)
    self.assertTrue(mock_button.called)
    self.assertTrue(mock_text_input.called)
    self.assertTrue(mock_st.subheader.called)

if __name__ == "__main__":
    pytest.main([__file__])
