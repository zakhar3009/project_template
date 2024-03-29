import pandas as pd


def read_from_terminal():
    """
    This function reads text input from the terminal.

    Returns:
        str: The string entered by the user from the console.
    """
    result = input("Please enter some text: ")
    return result


def read_from_file_standard(file_path):
    """
    This function reads text from a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            result = file.read()
        return result
    except FileNotFoundError:
        raise FileNotFoundError("The file doesn't exist")


def read_from_file_pandas(file_path):
    """
    This function reads text from a file using pandas.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: The content of the file as a data frame.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        EmptyDataError:If the file specified by file_path is empty.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The file doesn't exist")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("The file is empty")
