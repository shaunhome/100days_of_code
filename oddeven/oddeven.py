

def FloatOrNot(num):
    if type(userType)==float:
        return "FLOAT"
    else:
        return "NOT"
        
def test(num):
    if type(num)//2==float:
        return "odd"
    else:
        return "even"

test1 = test(1)
test2 = test(2)
test3 = test(3)

print(test1,test2,test3)
