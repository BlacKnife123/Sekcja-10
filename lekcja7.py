"""
Agumenty kluczowe i pozycyjne
kluczowy - w postaci: klucz - wartość (domyślny)
pozycyjne - takich, których liczy się kolejność przy wywołaniu
"""

def greet(name,message="Jak się masz",seperator=" "):
    print(message,name,sep=seperator)

greet("Arek","Witojcie","!!!!!")
greet("Olek","Heja")
greet("Piotrek",seperator="\n")



