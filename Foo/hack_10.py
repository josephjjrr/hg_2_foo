"""
     //agregar después del item 500
     //los alias qux y thud
     [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]
"""


def fn_hack_10():
    result = [100,200,300,400,500,600,700]
    for index, value in enumerate(result):
        if index == 5:
            result.insert(index,"qux")
        elif index == 6:
            result.insert(index, "thud")
    return result
print(fn_hack_10())