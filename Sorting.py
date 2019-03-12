def SortProperly(Listo,SortType):
    if(SortType == "Price"):
        return(SortByPrice(Listo))
    elif (SortType == "Ingredient"):
        return(SortByIngredient(Listo))
    else:
        return Listo


def SortByPrice(Listo):
    """
    Listo = [ [Link,Ingredient,Price],[],[]]
    """
    NewReturnArray = sorted(Listo, key=lambda x: x[2])
    return NewReturnArray


def SortByIngredient(Listo):
    return sorted(Listo,key =lambda x: len(x[1]))
