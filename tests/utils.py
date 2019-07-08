"""In this module helper functions, etc. for testing are defined."""

def compare_np_arrays(x, y):
    """checks if 2 numpy arrays are identical"""
    return (x == y).all()
    