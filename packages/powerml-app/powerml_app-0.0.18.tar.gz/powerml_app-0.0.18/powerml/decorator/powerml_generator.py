import functools
import csv
import os


def powerml_data(func):
    @functools.wraps(func)
    def wrapper():
        print("\nGenerating_data: " + func.__name__)
        result = func()
        return result
    wrapper.is_generator_function = True
    return wrapper
