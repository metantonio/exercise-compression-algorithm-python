# !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "implementation":   '21',
    "practicality"  :   '22',
    "better"        :   '23',
    "than"          :   '34',
    "Although"      :   '56',
}

def compress(content):
    """compress recibe una variable del tipo string que viene
    del archivo app.py, ya con el texto cargado del document.txt,
    a continuación se lee la cadena de texto y se reemplaza con cada
    valor del diccionario
    """

    compressed_content=content
    for key, emoji in symbols.items():
        compressed_content = compressed_content.replace(key,emoji)
    #print(compressed_content)
   
    return compressed_content