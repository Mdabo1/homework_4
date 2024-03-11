import main


def test_main_function_runs_without_errors():
    try:
        main.main()
    except Exception as e:
        assert False, f"Test failed with exception: {str(e)}"
