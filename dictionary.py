dict_name = {'aman' : 12, 'priyam' : 30}
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# zipped = zip(numbers, alphabet)
# print(zipped)
#phone_no = dict([('aman',123), ('pri',456), ('savita',23456)])
phone_no1 = dict(zip(alphabet, numbers))
print(phone_no1)
phone_no1['e'] = 199999999999999999999
print(phone_no1)
phone_no1['madhav']={1111,2222,3333}
print(phone_no1)
data = {
    1:'jenny',
    2:'aman',
    0:'priyam'
}
print(data)
print(data[0])
# print(phone_no1.keys())
# print(phone_no1.values())
# print(phone_no1.items())
# for key, value in data.items():
#     print(key, value)
for i in phone_no1:
    print(i)
    print(phone_no1[i])
