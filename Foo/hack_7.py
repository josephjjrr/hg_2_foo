"""
generic script

     //remplazar el item 300 
     //por tú alias
     [100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]
"""


def fn_hack_7():
    result = [100,200,300,400,500,600,700]
    for index, value in enumerate(result):
        if value == 300:
            result[index] = "Foo"
    return result
print(fn_hack_7())