def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    result = []
    # loop through a
    for num in a:
        # if num is a positive int and not in cache
        if num > 0 and num not in cache:
            # add to cache and set to false
            cache[num] = False
    # loop through a again
    for num in a:
        # if num negative int and in already in cache
        if x < 0 and abs(num) in cache:
            # add to cache and set to true
            cache[abs(num)] = True
    # loop through cache
    for key, value in cache.items():
        # if value is true append to result
        if value is True:
            result.append(key)

        


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
