def get_indices_of_item_weights(weights, length, limit):

    
    """
    YOUR CODE HERE
    """
    # Your code here
    
    cache = {}
    
    # loop through weights to get index and numbers
    for idx, number in enumerate(weights):
        # if numbers not in cache 
        if number not in cache:
            # add number and index to cache
            cache[number] = idx
    # loop through weights again
    for idx, number in enumerate(weights):
        # check if limit - number in cache
        if (limit - number) in cache:

            if idx == cache[(limit - number)]:
                # skip
                pass
            else:
                if idx > cache[(limit - number)]:
                    return (idx, cache[(limit - number)])
                    
                else:
                    # return 
                    return(cache[(limit - number)], idx)

