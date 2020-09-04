#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    cache = {}
    # loop through tickets
    for ticket in tickets:
        # if ticket not in cache
        if ticket not in cache:
            # add ticket to cache
            cache[ticket.source] = ticket.destination
        # if ticket source is none
        if ticket.source == "NONE":
            # append ticket to route
            route.append(ticket.destination)
    # while the last index in route not none
    while route[-1] != "NONE":
        # append the next cached route to the end of route
        route.append(cache[route[-1]])

    return route
