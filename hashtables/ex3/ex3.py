def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    result = []
    # loop through arrays
    for array in arrays:
        # loop through subarray
        for num in array:
            # if num not in the cache
            if num not in cache:
                # add to cache and set value to 1
                cache[num] = 1
            else:
                # if already in cache, increment count by 1
                cache[num] += 1
    # loop through key, value pairs in cache
    for key, value in cache.items():
        # if the value is found in every array
        if value == len(arrays):
            # append key to results list
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
