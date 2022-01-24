def somefun():
    print("inside some func")
    def some_inner_fun():
        var1 = 10
        print("inside inner func var is : ",var1)
    some_inner_fun()
    print("outside inner func var is : ",var1)
somefun()