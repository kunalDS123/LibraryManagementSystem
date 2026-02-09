def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[log] Running:{func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def generate_id(prefix , number):
    return f"{prefix}{number:03}"
