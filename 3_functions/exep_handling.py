def spam(dividedby) -> int:
    try:  # start this with a try
        return 42 / dividedby
    except ZeroDivisionError:  #work like else
        print ("invalid args" )

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

