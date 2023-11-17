"""
generic script

     //eliminar los items 300 y 500
     [100,200,300,400,500,600,700]  result >  [100,200,400,600,700]
"""


def fn_hack_5():
    result = [100,200,300,400,500,600,700]
    for index, valor in enumerate(result):
        if (valor == 300) or (valor == 500):
            del result[index]
    return result
print(fn_hack_5())