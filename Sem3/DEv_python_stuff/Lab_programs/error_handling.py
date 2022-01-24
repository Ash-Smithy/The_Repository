def first():
    try:
        a = 5
        b = 0
        c = a/b
    except ZeroDivisionError:
        print("The denominator cannot be 0")
try:
    raise  Exception('hello','world')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    arg1, arg2 = errorObj.args
    print("Arguemnt 1 : ",arg1)
    print("Argument 2 : ",arg2)
    