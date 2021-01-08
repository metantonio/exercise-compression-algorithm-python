# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):

    decompressed_content = compressed_content
    for (key, symbol) in symbols.items():
        #content=content.replace(key,symbol)
        decompressed_content = decompressed_content.replace(symbol,key)
    #print(decompressed_content)
    
    return decompressed_content
    