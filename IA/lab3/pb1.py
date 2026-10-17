import math
import scipy

def softMax(array) : 
    result = []
    for index,value in enumerate(array):
        upper_bound = math.exp(value)
        lower_bound = sum([math.exp(x) for x in array])
        result.append(upper_bound/lower_bound)

    return result

array = [-0.4,0,0.2,0.2,0.4]
print(softMax(array))
    
