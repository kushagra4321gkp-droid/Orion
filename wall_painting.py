#from networkx.algorithms.isomorphism.isomorph import could_be_isomorphic
import math

# def wall_paint(Height,Width,Coverage):
#     can_required = (height*width)/coverage
#
#     print(f"can_required = {can_required}")
# wall_paint(height,width,coverage)


# height = int(input("enter height of the wall : "))
# width = int(input("enter width of the wall : "))
# coverage = int(input("enter coverage of the wall : "))
# def wall_paint(Height,Width,Coverage):
#     can_required = (Height*Width)/Coverage
#
#     print(f"can_required = {can_required}")
# wall_paint(Height=height,Width=width,Coverage=coverage)


#wrong
# height = int(input("enter height of the wall : "))
# width = int(input("enter width of the wall : "))
# coverage = int(input("enter coverage of the wall : "))
# def wall_paint(**kwargs):
#     for key, value in kwargs.items():
#         can_required = (Height*Width)/Coverage
#
#     # print(f"can_required = {can_required}")
# wall_paint(Height=height,Width=width,Coverage=coverage)

#instead do this
def wall_paint(**kwargs):
    height = kwargs["Height"]
    width = kwargs["Width"]
    coverage = kwargs["Coverage"]
    can_required = (height * width) / coverage
    print(f"can_required = {can_required}")
    can_req = math.ceil(can_required)
    print(f"can_req = {can_req}, which is a round figure")
height = int(input("enter height of the wall : "))
width = int(input("enter width of the wall : "))
coverage = int(input("enter coverage of the wall : "))
wall_paint(Height=height,Width=width,Coverage=coverage)
