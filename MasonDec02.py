from functools import wraps

user_permissions = {"admin": True, "user": False}

def authorization_decorator(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_permissions.get(user_role, False):
            return func(*args, **kwargs)
        
        else:
            print("Unauthorized access. Permission denied")
            return None
    return wrapper
    
@authorization_decorator
def greet():
    return "Hello, authorized user!"

print(greet("admin"))
print(greet("user"))