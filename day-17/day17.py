# Creating Class
class User:
    def __init__(self, user_id, username): # Creating attributes (the thing that object has)
        self.id = user_id
        self.username = username
        self.followers = 0 # default value 
        self.following = 0

    # methods (the thing that the object does)
    
    def follow(self, user): # always need self parameter
        user.followers += 1
        user.following += 1

user_1 = User()