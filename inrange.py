import sys

def main(text):
    final = []
    n = int(sys.argv[1])
    for i in range(3000, 5000):
        if i % n == 0 and i % (n+7) == 0 and i % n**2== 0:
            final.append(i)
    return(final)
    
    
print(main(sys.argv[1]))
