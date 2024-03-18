from app.io import input
from app.io import output


def main():
    file_for_writing_1 = "data/file_for_writing_1"
    file_for_writing_2 = "data/file_for_writing_2"
    file_for_writing_pandas = "data/file_for_writing_pandas"
    file_for_reading_standard = "data/file_for_reading_standard"
    file_for_reading_pandas = "data/file_for_reading_pandas"
    output.output_in_terminal(f"Text from terminal input: {input.read_from_terminal()}\n")
    output.output_in_terminal(
        f"Text from {file_for_reading_standard} (standard python): \n"
        f"{input.read_from_file_standard(file_for_reading_standard)}\n")
    output.output_in_terminal(
        f"Text from {file_for_reading_pandas} (pandas): "
        f"\n{input.read_from_file_pandas(file_for_reading_pandas).to_string(index=False)}\n"
    )

    output.output_to_file_standard(file_for_writing_1, input.read_from_terminal())
    output.output_to_file_standard(file_for_writing_2, input.read_from_file_standard(file_for_reading_standard))
    output.output_to_file_pandas(file_for_writing_pandas, input.read_from_file_pandas(file_for_reading_pandas))


if __name__ == '__main__':
    main()
