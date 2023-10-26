"""
understanding walrus opertor: Supported in  python 3.8+
"""

s='hellooooooo world'

if(len(s)>10):
    print(f" too long {len(s)} elements")

#with walrus opertor
if((n:=len(s)) > 10):
    print(f" too long {n} elements")