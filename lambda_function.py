b = 30                                  
def display():                          
    print("I am one")
    global a
    a = 20
    b = 25
    print(b)
def dispaly2():
    print("I am two")
print(b)
if __name__ == '__main__':
    display()
print(a)
print(b)
