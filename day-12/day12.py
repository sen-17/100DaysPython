# Local vs Global Scope

enemies = 1 # Global Scope

def increase_enemies():
    enemies = 2 # Local Scope
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(enemies)

# Does python has a block scope?
# No , Python doesn't has a block scope

# Modifying Global Scope
def increase_enemies():
    # global enemies Prones to Error, instead just use return 
    print(f"Enemies inside function: {enemies}")
    return enemies + 1