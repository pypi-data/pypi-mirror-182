
from timeit import timeit
import rich

def optimus_compare(unoptimized_function, optimized_function, unoptimized_args = (), optimized_args = (), iterations = 1000, multiplier = 1000,  verbose = False):
    unoptimized_time = timeit(f'{unoptimized_function}(*{unoptimized_args})', f"from __main__ import {unoptimized_function}", number = iterations)
    optimized_time = timeit(f'{optimized_function}(*{optimized_args})', f"from __main__ import {optimized_function}", number = iterations)    

    if verbose:
        rich.print(f"Time comparision between {unoptimized_function} and {optimized_function}:")

    tabbed_space = "\t" if verbose else ""
    rich.print(f"[red bold]{tabbed_space}Unoptimized code:[/red bold]", end = " ")
    print(unoptimized_time * multiplier)
    rich.print(f"[green bold]{tabbed_space}Optimized code:[/green bold]", end = " ")
    print(optimized_time * multiplier)

