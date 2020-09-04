# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    
    result = []
    # iterate through files
    for file in files:
        # split the files into a list by "/"
        dirs = file.split("/")[-1]
        # if dirs not in cache
        if dirs not in cache:
            # add to cache
            cache[dirs] = [file]
        else:
            cache[dirs].append(file)
    # loop through queries
    for query in queries:
        # if query in cache
        if query in cache:
            # add all elements in query to results (use extend because of nested lists)
            result.extend(cache[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
