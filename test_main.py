import main  # Importing the main.py file to test
import streamlit as st

def test_title_displayed(capfd):
    # Redirect stdout to capture print statements
    import sys
    sys.stdout = capfd

    # Call the main function
    main.main()

    # Get the captured output
    captured = capfd.readouterr()

    # Check if the title is displayed correctly
    assert "Про-классифицируй текст\n" in captured.out, "Test Failed: Title is not displayed correctly."
