def greet(name, subject, dept="CS"):
    print(f"HI {name}!")
    print(f"do you teach {subject}?")
    print(f"are from {dept} department?")


# greet("jenny",'python')

# dept is a default parameter. #default parameter only comes after non-default parameters.
# keyword arguments only comes after positional arguments.
# #if you provide default argument in fun_call, it will be overwritten as in default parameter in fun_definition.

# what if?
greet("python", "jenny")  # this problem is solved by keyword arguments
