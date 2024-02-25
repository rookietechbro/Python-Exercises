# class ZeroDivisionError:
#     pass
# try:
#     age = int(input("Enter your age: "))
#     result = 10 / age
#     print(result)
# except ZeroDivisionError:
#  # except (ZeroDivisionError, ValueError)
#     pass
# except ValueError:
#     print("ur age cannot be string literal")
# finally:
#     print("finally block runs either there's an exception or not")

def age_check(n):
    if n < 0:
        raise ValueError("age cannot be less than or equal to zero")
    return f'you are {n} years old '


print(age_check(-2))
