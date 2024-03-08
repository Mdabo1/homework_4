import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
from transformers import pipeline

class TestMain(unittest.TestCase):
    @patch("streamlit.text_input", return_value="This is a positive text.")
    @patch("streamlit.button", return_value=True)
    @patch("transformers.pipeline")
    def test_main(self, mock_pipeline, mock_button, mock_text_input):
        # Mock the pipeline
        mock_pipeline.return_value = MagicMock(return_value=[
            {"label": "Positive", "score": 0.9},
            {"label": "Negative", "score": 0.05},
            {"label": "Neutral", "score": 0.05},
        ])

        # Call the main function
        import main
        main.main()

        # Check if the output is correct
        self.assertTrue(mock_pipeline.called)
        self.assertTrue(mock_button.called)
        self.assertTrue(mock_text_input.called)
        self.assertTrue(st.subheader.called)
        self.assertTrue(st.write.called)

if __name__ == "__main__":
    unittest.main()
