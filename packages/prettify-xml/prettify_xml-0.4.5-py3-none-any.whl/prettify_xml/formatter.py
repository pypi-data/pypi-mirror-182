"""
Module for a command-line application formatting XML
files

:author: Julian M. Kleber
"""
import xml.dom.minidom
import click


@click.command()
@click.option("-i", help="Input file")
@click.option("-o", help="output file.")
def format_xml(i: str, o: str) -> None:
    """
    The format function takes an input file and writes the output to a specified location.
    The function also returns the number of characters in the new file.

    :param i: Specify the input file
    :param o: Specify the output file
    :return: A string representation of the xml document
    :doc-author: Trelent
    """

    with open(i) as original_xml:
        temp = xml.dom.minidom.parseString(original_xml.read())
        new_xml = temp.toprettyxml()

    with open(o, "w") as output_xml:
        output_xml.write(new_xml)


if __name__ == "__main__":
    format_xml()
