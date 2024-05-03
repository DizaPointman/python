def help(sides):
    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])

def equilateral(sides):
    return len(set(sides)) == 1 and 0 not in sides


def isosceles(sides):
    return (len(set(sides)) < 3) and help(sides) == True


def scalene(sides):
    return (len(set(sides)) == 3) and help(sides) == True
