def output_in_terminal(text):
    """
    This function write text in terminal.

    Args:
        text (str): The text that should be printed.

    Returns:
        None
    """
    print(text)


def output_to_file(file_path, text):
    """
    This function write text to the file.

    Args:
        file_path (str): The path to the file to write.
        text (str): The text to write

    Returns:
        None

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError("The file doesn't exist")
