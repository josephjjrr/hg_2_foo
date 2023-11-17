"""
generic script

     //eliminar el último item
     [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600]
"""


def fn_hack_3():
    result = [100,200,300,400,500,600,700]
    del result[-1]
    return result
print(fn_hack_3())