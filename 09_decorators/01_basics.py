from functools import wraps

def my_decorator(fun):
    @wraps(fun)
    def wrapper():
        print("Before function run")
        fun()
        print("After funtion run")
        
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chai code")
    
greet()
print(greet.__name__)