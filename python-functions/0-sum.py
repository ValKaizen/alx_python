cat 0-main.py
#!/usr/bin/python3
add = __import__('0-sum').add
if __name__ == "__main__":
    
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))