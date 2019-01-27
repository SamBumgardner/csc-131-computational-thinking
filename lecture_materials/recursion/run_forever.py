def runForever(n):
    if n == 0:
        return 0
    else:
        return runForever(n)

def main():
    print(runForever(10))

main()
        
