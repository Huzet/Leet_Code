# def romanToInt(s: str) -> int:
#         rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
#         integer = 0
#         prev = 0
#         for char in s:
#             value = rom[char]
#             if prev != 0 and prev < value:
#                 integer += value - 2 * prev
                
#             else:
#                 prev = value
#                 integer += value
        
#         print(integer)

# romanToInt('MCMXCIV')

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
