# d1 = {
#     'one': 2001,
#     'two': 2002,
#     'three': 2003
# }
# d2 = {
#     'four': 2004,
#     'five': 2005,
#     'six': 2006
# }
#
# d3 = {
#     'seven': 2007,
#     'eight': 2008,
#     'nine': 2009
# }
#
#
# d2.update(d1)
# d2.update(d3)
#
# print(d2)


# d1 = {
#     'one': 2001,
#     'two': 2002,
#     'three': 2003
# }
# d2 = {
#     'four': 2004,
#     'five': 2005,
#     'six': 2006
# }
#
# d3 = {
#     'seven': 2007,
#     'eight': 2008,
#     'nine': 2009
# }
#
#
# d4 = d1 | d2 | d3
#
# print(d4)




# d1 = {
#     'one': 2001,
#     'two': 2002,
#     'three': 2003
# }
# d2 = {
#     'four': 2004,
#     'five': 2005,
#     'six': 2006
# }
#
# d3 = {
#     'seven': 2007,
#     'eight': 2008,
#     'nine': 2009
# }
#
#
# d4 = {**d1, **d2, **d3}
#
# print(d4)
import operator


my_dict = {'a':500, 'b':5874, 'c': 560, 'd':400, 'e':5874, 'f': 20}

my_dict2 = my_dict.items()

print(sorted(my_dict2, key = operator.itemgetter(1), reverse=True)[:3])

print(my_dict.get('a'))

print "Hello git111"