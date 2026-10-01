def water_jug(a=0, b=0, target=2, visited=None):
    if visited is None: 
        visited = set()

    print(f"Jug A: {a}L | Jug B: {b}L")

    if a == target or b == target:
        print("Target Reached!")
        return True

    if (a, b) in visited:
        return False
    visited.add((a, b))

    # Try standard actions in sequence
    return (
        water_jug(4, b, target, visited) or  # Fill A
        water_jug(a, 3, target, visited) or  # Fill B
        water_jug(0, b, target, visited) or  # Empty A
        water_jug(a, 0, target, visited) or  # Empty B
        water_jug(a - min(a, 3 - b), b + min(a, 3 - b), target, visited) or  # Pour A -> B
        water_jug(a + min(b, 4 - a), b - min(b, 4 - a), target, visited)     # Pour B -> A
    )

water_jug()
