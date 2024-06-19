from tasks import add, hallo

result1 = add.delay(2, 3)
# for i in range(50):
#     print(result1.ready())
#     print(result1.ready())
print(result1.get())
# print(result1.ready())

# result2 = add.delay(2, 4)
# print(result2.ready())
# print(result2.get())

# result3 = add.delay(3, 4)
# print(result3.ready())
# print(result3.get())

result_h = hallo.delay()
print(result_h.get())