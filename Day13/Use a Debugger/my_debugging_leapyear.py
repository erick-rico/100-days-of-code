# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
                return True
        else:
            return False
    else:
        return False

print(is_leap(2000))