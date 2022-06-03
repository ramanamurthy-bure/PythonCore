# __name__ and __main__
# An often confusing part of the Python is a mysterious line of code:
# Sometimes when you are importing from a module, you would like to know whether a modules function is being
# used as an import,or if you are using the origional.py file of that module

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    print('ONE.PY is being run directly')
else:
    print('ONE.PY has been imported!')