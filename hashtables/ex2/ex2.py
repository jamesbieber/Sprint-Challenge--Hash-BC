#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    source_airport = "NONE"

    for x in tickets:
        # inserts every ticket into HT
        hash_table_insert(ht, x.source, x.destination)

    for x in range(length):
        # using NONE as the first 'source', retrieve first ticket
        route[x] = hash_table_retrieve(ht, source_airport)
        # changes 'source' to the 'destination' of previous ticket
        source_airport = route[x]
    return route
