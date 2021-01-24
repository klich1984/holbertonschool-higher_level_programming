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
    i = 0
    for idx in txt:
        if i < len(txt) - 1:
            print(idx.lstrip())
            i += 1
    print(idx.lstrip(), end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")