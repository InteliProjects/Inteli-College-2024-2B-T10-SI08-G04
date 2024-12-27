table_fns = {}

def add_table_fn(fn_type, table_name):
    def decorator(func):
        if not table_fns.get(fn_type):
            table_fns[fn_type] = {}
        table_fns[fn_type][table_name] = func
    return decorator