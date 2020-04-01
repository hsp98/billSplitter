"""
If the participant owes money to the group, then the amount is positive. If
the participant should collect money from the group, then the amount is negative.
"""
import sys
import os


def readAndParseInput(filename) -> dict:
    """ Processes the file line by line. O(n)
    Reads input file and makes dictonary of trips
    input: name of the file
    return: dict type object
    """
    input_data = {}
    _counter = 0
    with open(filename, 'r') as ip_file:
        ip = ip_file.readline() 
        while(ip != '0'):
            _participants = int(ip)
            if input_data.get(_counter) is None:
                input_data[_counter] = []
            for _ in range(_participants):
                ip = ip_file.readline()
                _num_of_tx = int(ip)
                _tx_sum = 0
                for __ in range(_num_of_tx):
                    ip = ip_file.readline()
                    _tx_sum += float(ip)
                input_data[_counter].append(round(_tx_sum, 3))
            ip = ip_file.readline()
            _counter += 1
    return input_data


def processInPlace(tx_data) -> None:
    """
    Calculated the individual contribution of the participants in the trip
    input: transaction data
    returns: None 
    """
    for _trip, tx_array in enumerate(tx_data.values()):
        _trip_total = sum(tx_array)
        cost_to_each = round(_trip_total/len(tx_array), 3)
        for i, expend_by_participant in enumerate(tx_array):
            tx_array[i] = round(expend_by_participant - cost_to_each, 3)


def printOutput(data, fp) -> None:
    """
    Prints output in mentioned format.
    input: transaction data and outfile name
    returns: None
    """
    for trip in data.values():
        for split_bill in trip:
            if split_bill < 0:
                print(f"(${abs(split_bill)})", file=fp)
            else:
                print(f"${split_bill}", file=fp)
        print(file=fp)


def getInputOutputFilename(args):
    """
    Gets name of the input file from arguement passed 
    input: command line arguement
    returns: name of input along with name of output file
    """
    if len(args) == 1:
        raise Exception('Input filename as command line argument missing.')
    if not os.path.exists(args[1]):
        raise FileNotFoundError(f"Input file ${args[1]} is missing.")
    return args[1], args[1] + '.out'


def main():
    """
    Function to handle execution of program
    """
    input_file, output_file = getInputOutputFilename(sys.argv)
    transaction_data = readAndParseInput(input_file)
    processInPlace(transaction_data)
    with open(output_file, 'w') as op_file:
        printOutput(transaction_data, op_file)
    


if __name__ == "__main__":
    main()
