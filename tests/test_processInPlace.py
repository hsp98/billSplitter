from BillSplit import processInPlace


def testTransactionDataProcessing():
    """
    Given a sample input Data.
    It asserts the result whether it is evaluated properly.
    """
    sample_correct_input_data = {0: [42.0, 42.02, 83.0], 1: [18.01, 16.7]}
    expected_output = {0: [-13.673, -13.653, 27.327], 1: [0.655, -0.655]}
    processInPlace(sample_correct_input_data)
    assert sample_correct_input_data == expected_output
