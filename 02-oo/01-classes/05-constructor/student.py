#Add a constructor to our Wall class. It should take depth, height and width as parameters, in that order,
#and set them as properties. It should also compute an additional property called volume. 
#Volume is the width times height times depth.

class wall:
    def __init__(self, depth, height, width):
        self.height = height
        self.depth = depth
        self.width = width
        self.volume = depth * height * width
        

