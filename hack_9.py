"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    output = []
    i = 0
    while i < len(result):
        output.append(result[i])
        output.append('@')
        i += 1
    return output