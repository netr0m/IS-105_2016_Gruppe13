import timeit

number_List = []
number_List.append([1, 2, 4, 8 ,16, 32, 64])

name_List = []
name_List.append(["Marius", "Morten", "Nora", "Joakim", "Erlend"])

charachter_List = []
charachter_List.append(['U', 'I', 'A', 'K', 'R', 'S', 'N', 'O', 'R'])

def search_fast(name_List, ("Marius")):
    for item in name_List:
        if item == "Marius":
            return True
        return False
    
    
def search_slow(name_List):
    return_value = False
    for item in haystack:
        if item == "Marius":
            return_value = True
            print "Marius"
        return return_value