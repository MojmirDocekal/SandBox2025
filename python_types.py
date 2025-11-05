# Constant set containing entities who sleep
sleep: set[str] = {"Peter", "John", "Mary"}

# Constant set containing love relations (tuples of two entities)
love: set[tuple[str, str]] = {("Peter", "Mary"), ("John", "Mary")}


def is_sleeping(entity: str) -> bool:
    """
    Returns True if the entity is in the sleep set, otherwise returns False.
    
    Args:
        entity: Name of the entity to check
    
    Returns:
        True if entity is in the sleep set, False otherwise
    """
    return entity in sleep


def does_love(entity1: str, entity2: str) -> bool:
    """
    Returns True if the relation (entity1, entity2) is in the love set, otherwise returns False.
    
    Args:
        entity1: First entity in the relation
        entity2: Second entity in the relation
    
    Returns:
        True if (entity1, entity2) is in the love set, False otherwise
    """
    return (entity1, entity2) in love

def logical_and(a: bool, b: bool) -> bool:
    """
    Returns True if both a and b are True, otherwise returns False.
    
    Args:
        a: First boolean value
        b: Second boolean value
    
    Returns:
        True if both arguments are True, False otherwise
    """
    return a and b

# Demonstration of the logical_and function
if __name__ == "__main__":
    print("Demonstration of logical_and function:")
    print(f"logical_and(True, True) = {logical_and(True, True)}")
    print(f"logical_and(True, False) = {logical_and(True, False)}")
    print(f"logical_and(False, True) = {logical_and(False, True)}")
    print(f"logical_and(False, False) = {logical_and(False, False)}")

    print("Demonstration of is_sleeping function:")
    test_entities = ["Peter", "Alice", "John", "Bob", "Mary", "Eve"]
    for entity in test_entities:
        print(f"is_sleeping('{entity}') = {is_sleeping(entity)}")

    print("Demonstration of does_love function:")
    test_relations = [("Peter", "Mary"), ("John", "Mary"), ("Mary", "Peter"), ("Alice", "Bob")]
    for entity1, entity2 in test_relations:
        print(f"does_love('{entity1}', '{entity2}') = {does_love(entity1, entity2)}")