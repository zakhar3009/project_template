import os
import pandas as pd

import pytest
from app.io.input import read_from_file_standard
from app.io.input import read_from_file_pandas


def test_read_from_existing_file_standard():
    content = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    with open("test_for_reading.txt", 'w') as file:
        file.write(content)
    assert content == read_from_file_standard("test_for_reading.txt")
    os.remove("test_for_reading.txt")


def test_read_from_nonexistent_file_standard():
    with pytest.raises(FileNotFoundError):
        read_from_file_standard("some_file.txt")


def test_read_from_empty_file_standard():
    with open("test_for_reading.txt", "w") as file:
        file.write("")
    result = read_from_file_standard("test_for_reading.txt")
    assert result == ""
    os.remove("test_for_reading.txt")


def test_read_from_existing_file_pandas():
    df = pd.DataFrame({
        "key1": ["value11", "value12", "value13"],
        "key2": ["value21", "value22", "value23"]
    })
    df.to_csv("test_for_reading_pandas", index=False)
    assert df.to_string(index=False) == read_from_file_pandas("test_for_reading_pandas")
    os.remove("test_for_reading_pandas")


def test_read_from_nonexistent_file_pandas():
    with pytest.raises(FileNotFoundError):
        read_from_file_pandas("some_file.txt")


def test_read_from_empty_file_pandas():
    with open("test_for_reading_pandas.csv", "w"):
        with pytest.raises(pd.errors.EmptyDataError):
            read_from_file_pandas("test_for_reading_pandas.csv")
    os.remove("test_for_reading_pandas.csv")
