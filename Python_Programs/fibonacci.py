#fibonacci using for loop
ft = 0
st = 1
nt = ft + st
print(ft)
print(st)
for i in range(10):
    print(nt)
    ft = st
    st = nt
    nt = ft + st
