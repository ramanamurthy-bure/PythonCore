s = """Hello my name is Ramana
I am from India
"""
print(s)
t = "My name is Ståle"
s = 'Ramana'
s1 = ' ramnana murthy,bure '
s2 = ' Murthy123'
s3 = 'Bure '
s4 = '1234'
s5 = '1234##@21'
print(s1.upper())
print(s1.lower())
print(s1.replace('a', 'I'))
print(s1.strip())
print(s2.lstrip())
print(s3.rstrip())
print(s1.isalnum())
print(s1.strip().isalnum())
print(s4.isdigit())
print(s1.strip().capitalize())
print(s.center(20))
print(s.center(20, '_'))
print(s1.find(','))
print(s1.rfind(','))
print(s.encode())
print(t.isidentifier())
print(s.isidentifier())
print(s3.isidentifier())
print(s1.strip().title())
print(t.index('a', 1))
print(t.endswith("le"))
print(t.startswith("My"))
print(type(t))
print(isinstance(t, str))




