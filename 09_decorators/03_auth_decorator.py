from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied: Admin only area")
            return None
        else:
            return func(user_role)
        
    return wrapper


@require_admin
def access_tea_inventary(role):
    print("Access Granted enter to  inventory")
    
access_tea_inventary("user")
access_tea_inventary("admin")
