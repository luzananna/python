def sortNumbers(data, condition):  
    if condition == 'ASC':  
        for i in range(1, len(data)):  
            for j in range(1, len(data) - i + 1):  
                    if data[j - 1] > data[j]:  
                        data[j - 1], data[j] = data[j], data[j - 1]  
  
    if condition == 'DESC':  
        for i in range(1, len(data)):  
            for j in range(1, len(data) - i + 1):  
                if data[j - 1] < data[j]:  
                    data[j - 1], data[j] = data[j], data[j - 1]  
    return data  
  
  
def sortData(weights, data, condition):  
  
    if len(weights) != len(data):  
        raise ValueError('Invalid input data')  
  
    if condition == 'ASC':  
        for i in range(1, len(weights)):  
            for j in range(1, len(weights) - i + 1):  
                if weights[j - 1] > weights[j]:  
                    weights[j - 1], weights[j] = weights[j], weights[j - 1]  
                    data[j - 1], data[j] = data[j], data[j - 1]  
                      
    if condition == 'DESC':  
        for i in range(1, len(weights)):  
            for j in range(1, len(weights) - i + 1):  
                if weights[j - 1] < weights[j]:  
                    weights[j - 1], weights[j] = weights[j], weights[j - 1]  
                    data[j - 1], data[j] = data[j], data[j - 1]  
    return data