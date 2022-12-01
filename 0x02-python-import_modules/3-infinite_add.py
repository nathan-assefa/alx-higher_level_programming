#!/usr/bin/python3
#!/usr/bin/python3
from sys import argv

def main():
    _sum = 0;
    i = 1
    while (i < len(argv)):
        _sum += int(argv[i])
        i += 1

    print(_sum)
if __name__ == "__main__":
    main()
