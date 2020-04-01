import os

from BillSplit import getInputOutputFilename


def testValidFilenames(monkeypatch):
    """
    Given an array representing sys.argv.
    It tests whether the output filename is created as expected.
    """
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    args = ['sourceFile', 'input.txt']
    ip_file, op_file = getInputOutputFilename(args)
    assert ip_file == args[1]
    assert op_file == ip_file + '.out'


def testThrowExceptionFilenotfound():
    """
    Given an array representing sys.argv.
    It asserts the FileNotFoundError generated when filename in args is missing.
    """
    args = ['sourceFile', 'missing.txt']
    try:
        ip_file, ip_file = getInputOutputFilename(args)
    except Exception as e:
        assert type(e) == FileNotFoundError
        assert str(e) == f"Input file ${args[1]} is missing."


def testThrowExceptionArgMissing():
    """
    Given an array representing sys.argv.
    It asserts the Exception when filename is missing in the args.
    """
    args = ['sourceFile']
    try:
        ip_file, ip_file = getInputOutputFilename(args)
    except Exception as e:
        assert type(e) == Exception
        assert str(e) == 'Input filename as command line argument missing.'
