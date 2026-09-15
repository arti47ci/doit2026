def equilateral(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    return  a > 0 and b > 0 and c > 0 and a==b==c
            


def isosceles(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    return (a > 0 and b > 0 and c > 0) and (a+b > c and b+c > a and a+c>b) and (a == b or b == c or a == c )
            
def scalene(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    return  (a  > 0 and b > 0 and c > 0) and  (a+b > c and b+c > a and a+c > b) and (a!= b and b!= c and c!= a)
equilateral([1,1,3])  
isosceles([1,2,3])
scalene([4,5,6])
            
    
