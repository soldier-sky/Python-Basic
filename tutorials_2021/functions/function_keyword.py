#understanding how to invoke function via passing value through keyword

def func(a, b=30,c=10):
    print('a is', a, ' and b is ', b, 'and c is ',c)

func(3,7)
func (25, c=24)
func(c=50, a=100)
