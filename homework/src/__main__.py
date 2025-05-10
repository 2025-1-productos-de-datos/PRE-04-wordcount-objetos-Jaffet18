import argparse

from ._internals.file_reader import FileReader


class ArgumentParser:
    def __init__(self):

        self.input = None
        self.output = None
        self.parser = None
        self.crear_parser()

    def crear_parser(self):
        self.parser = argparse.ArgumentParser(description="Count words in files.")

        self.parser.add_argument(
            "input",
            type=str,
            help="Path to the input folder containing files to process",
        )
        self.parser.add_argument(
            "output",
            type=str,
            help="Path to the output folder for results",
        )

    def run(self):

        parsed_args = self.parser.parse_args()
        self.input = parsed_args.input
        self.output = parsed_args.output


def main():

    ArgumentParser = ArgumentParser().run()

    file_reader = FileReader(ArgumentParser.input)
    text_processor = text_processor()

    lines = file_reader.read_all_lines()
    preprocessed_lines = text_processor.preprocess(lines)
    word = text_processor.split_into_words(preprocessed_lines)
