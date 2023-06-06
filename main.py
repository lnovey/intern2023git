import sys 

def main() -> int:
    """print args"""
    print("beautiful")
    print(sys.argv)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
