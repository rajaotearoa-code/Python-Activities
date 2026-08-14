import os


class TextFileProcessor:
    """
    A class to read, analyze, modify, and save text files.
    Encapsulates file operations and text transformations into an OOP structure.
    """

    def __init__(self, file_path="junk.txt"):
        self.file_path = file_path
        self.lines = []

    def read_file(self):
        """Reads all lines from the specified file into memory."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' not found in the current directory.")

        with open(self.file_path, "r", encoding="utf-8") as file:
            self.lines = file.readlines()

    def get_line_count(self):
        """Calculates and returns the total number of lines in the file."""
        return len(self.lines)

    def append_line(self, new_text):
        """Appends a new line of text to the end of the lines list."""
        # Ensure previous line ends with a newline character (\n)
        if self.lines and not self.lines[-1].endswith("\n"):
            self.lines[-1] += "\n"
        
        self.lines.append(new_text + "\n")

    def convert_to_lowercase(self):
        """Converts all lines in the file to lowercase."""
        self.lines = [line.lower() for line in self.lines]

    def save_file(self):
        """Writes the updated lines back to the file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(self.lines)

    def process(self, text_to_add="text file nanalyssis"):
        """Orchestrates all required activity steps and prints results."""
        print("=" * 60)
        print("           TEXT FILE PROCESSING & ANALYSIS              ")
        print("=" * 60)

        # 1. Read file and report original line count
        self.read_file()
        original_count = self.get_line_count()
        print(f"1. Total lines in original file : {original_count}")

        # 2. Add the new line at the end
        self.append_line(text_to_add)
        print(f"2. Added new line to end       : '{text_to_add}'")

        # 3. Convert all text to lowercase
        self.convert_to_lowercase()
        print("3. Converted entire file        : All characters set to lowercase")

        # 4. Save the modified file
        self.save_file()
        print(f"4. File saved successfully      : '{self.file_path}'")
        print(f"   Updated total line count     : {self.get_line_count()}")
        print("=" * 60)


def main():
    processor = TextFileProcessor(file_path="junk.txt")
    processor.process(text_to_add="text file nanalyssis")


if __name__ == "__main__":
    main()