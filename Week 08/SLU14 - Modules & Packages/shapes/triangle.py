
class Triangle:
    
    def __init__(self, base, height):
        
        self.base=base
        self.height=height
        self.description='this is a module named triangle'

    def get_area(self):
        
        return self.base*self.height/2


def is_equilateral(a_, b_, c_):
    if a_ == b_ and b_ == c_ and c_ == a_ :
        return True
    else:
        return False   
    
    
description='this is a module named triangle'    