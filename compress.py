# !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "implementation":   "😫",
    "practicality"  :   '😐',
    "better"        :   '🤔',
    "than"          :   '😘',
    "Although"      :   "😌",
}

def compress(content):
    """compress recibe una variable del tipo string que viene
    del archivo app.py, ya con el texto cargado del document.txt,
    a continuación se lee la cadena de texto y se reemplaza con cada
    valor del diccionario
    """
    for key, emoji in symbols.items():
        compressed_content = content.replace(key,emoji)
    print(compressed_content)
   
    return compressed_content