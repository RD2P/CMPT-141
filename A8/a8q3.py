# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

def read_data(filename):
    """ reads in data about treasures.
    Each treasure has a name, value, and weight
    
    filename: string. Name of a CSV file where treasures
        are listed 1 per line.
    return: a list of records (dictionaries). Each record
        has the keys "name", "value", and "weight"
    """
    f = open(filename, 'r')
    L = []
    for line in f:
        line = line.rstrip().split(",")
        treasure = {"name": line[0],
                    "value": int(line[1][1:]),
                    "weight": int(line[2]) }
        L.append(treasure)
    return L

file = "room3.txt"    
treasures = read_data(file)

def best_value(List, limit):
    '''
    Takes a list of records with value and weights, and gives the highest value under a given weight limit
    Input: 
        List - a list of item records in the form { "name": string, "value": int, "weight": int }
        limit - max capacity in kg
    Output: the maximum total value ($) of items within the max capacity '''

    # no items left
    if len(List) == 0:
        return 0
    # no capacity left in bag
    if limit <= 0:
        return 0

    # grab the value and weight from the last item in the list
    val = List[-1]['value']
    weight = List[-1]['weight']

    # if there's no room in the bag for the last item, don't include the item
    if weight > limit:
        return best_value(List[:-1], limit)
    # else, the item could be included or not included in the final list, find which gives the bigger value
    else:    
        included = val + best_value(List[:-1], limit - weight) 
        not_included = best_value(List[:-1], limit)
        return max(included, not_included)


print(best_value(treasures, 300))