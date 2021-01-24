#!/usr/bin/python3
"""Function that prints a text"""


def text_indentation(text):
    """Print text find the characteres ., ? and :

    Args:
        text (str): text for print
    """
    if type(text) is not str:
        raise TypeError("Text must be a string")
# busco en text el caracter y cuando lo encuentra lo cambia \n\n
    for i in ".?:":
        text = text.replace(i, i + "\n\n")
# convierte el string texto en una lista por el separador \n
    txt = text.split("\n")
# imprime la la lista eliminando el espacio ala izquierda
    for idx in txt:
        print(idx.lstrip())
