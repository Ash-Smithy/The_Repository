#variable length argument
def func(name,*fav_subject):
    print("\n",name," likes to read ",)
    for sub in fav_subject:
        print(sub,end = " ")
func("Goransh","A","B")
func("Smitha","C","D","E")
func("Nayan")