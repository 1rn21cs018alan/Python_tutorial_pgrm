#single line even list

a=[2,323,345,2345567,37356,5236,24,12,1334,123,23414,153212,52,5413,45334,34]
b=[]
b=[x for x in a if x%2==0]
print(b)
