import __name__and__main__1
print("TOP LEVEL IN TWO.PY")
__name__and__main__1.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly')
else:
    print('TWO.PY has been imported!')