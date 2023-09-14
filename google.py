"""
example:
input:['A','B','C','C']
output:['A','C','B','C']

"""
input:['A','B','C','C']

def google_move(input):
    for s in input:
        if s[0] == s[1]:
            s[1] == s[3]

print(google_move(input))