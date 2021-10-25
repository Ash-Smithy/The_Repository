try:
    print("Raising exception")
    raise ValueError
except:
    print("Exception caught - - - - - - ")
finally:
    print("Performing clean up in finally .....")