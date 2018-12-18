"""
这是“nester.py”模块，提供了一个名为 print_lol()的函数，这个作用是打印列表，其中有可能包吃住（也有可能不包含）嵌套列表	
"""
def print_lol(the_list,level=0):
    """This function takes one positional argument called "the_list", which is any python list (of - possibly - nestted lists). Each data item in the provided list is (recursively) printed to the screen on it's own line."""
    for each_item in the_list:
        if isinstance(each_item, list):
             print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)