n = 9
m = 27
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

print(('.|.'*1).center(14,'+'))
print(('.|.'*1).ljust(14,'+'))
print(('WELCOME').center(13,'+'))
print(('.|.'*1).rjust(14,'+'))

l =[6,5,4,3,2,1]
print(l[::-1])
