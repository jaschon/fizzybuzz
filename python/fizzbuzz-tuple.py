#!/usr/bin/env python3
for i in range(1,101):
    match (i%3, i%5):
        case (0,0):
            print("FIZZBUZZ")
        case (0, _):
            print("FIZZ")
        case (_,0):
            print("BUZZ")
        case _:
            print(i)
