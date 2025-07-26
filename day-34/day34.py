# Type Hint
age : int
name : str

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    
    return "They can drive" # wrong , expecting boolean

print(police_check("twelve")) # wrong , expecting integer