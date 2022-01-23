import numpy as np 


def convert_to_floats(rows):
    """convert a list of string tuples to a  ndarray of floats"""

    # create a a result list ( later to be converted to np array matrix)
    result = []
    """
    for i in rows:
        result.append((float(i[0]), float(i[1]), float(i[2]),
                float(i[3]), float(i[4]), float(i[5]),
                float(i[6]))) 
    """
    # To-Do Loop through the list and convert row by row
    # a loop should be written 
    for i in rows:
       value = np.asarray(i) # fixed typo "i" instead of "row"
       value = value.astype(np.float)

       result.append(value)  # Vstack means we are adding a row

    return np.array(result)


