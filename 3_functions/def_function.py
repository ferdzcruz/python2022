#simplest way
def hello():
    print ("Hello World!")

hello()


#with parameters

def message(name,msg):
    return f"Hi {name}! {msg}!"

print(message("ferdie","Goodmorning"))


def count_char(word) -> str:
    return len(word)

username = input("enter username: ")
print(count_char(username))