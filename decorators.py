# Suppose we want to divide 2 numbers but, if i pass (2,4) and (4,2) the answer should be 2, the bigger number should be on the numerator and the smaller on the denominator. to make this change in logic the existing code is not available with us so here comes into picture of decorators. In decorators we create a new block of code which accepts the original function and our required logic can be applied in the new code.This is called as decorators.


def div(a,b):
    return a/b

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
print(div1(2,4))