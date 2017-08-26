class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    
    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    
    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.all_tents = [tent_loc]
    
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        far_enough = [new_tent_loc.dist_from(tent_) < 0.5 for tent_ in self.all_tents]
        far_enough = not bool(sum(far_enough))
        if far_enough:
            self.all_tents.append(new_tent_loc)
        return far_enough
        
    
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        tent_present = ([tent_loc == tent_ for tent_ in self.all_tents])
        tent_present = bool(sum(tent_present))
        self.all_tents.remove(tent_loc)

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        return sorted([tent_.__str__() for tent_ in self.all_tents])
        
def check_mod():
    c = MITCampus(Location(1, 2))
    print(
        c.add_tent(Location(2, 3)) == True,
        c.add_tent(Location(1, 2)) == True,
        c.add_tent(Location(0, 0)) == False,
        c.add_tent(Location(2, 3)) == False,
        c.get_tents() == ['<0,0>', '<1,2>', '<2,3>'],
        # c.get_tents(),
        c.remove_tent(Location(2, 3)),
        # c.get_tents(),
        # c.remove_tent(Location(12, 3)),
        )
def check2():
    """
    check if add_tent allows adding a tent closer than 0.5
    """
    c = MITCampus(Location(1,2), Location(3,1))
    # print(c.get_tents())
    print(c.add_tent(Location(2.5,1)))
    # print(c.get_tents())
    c = MITCampus(Location(1,2), Location(3,1))
    print(c.add_tent(Location(2.49,1)))
    c = MITCampus(Location(1,2), Location(3,1))
    print(c.add_tent(Location(2.51,1)))
    # print(Location(2.5, 1).dist_from(Location(3,1)))

    # print(
    #     c.add_tent(Location(2, 3)),
    #     c.add_tent(Location(1, 2)),
    #     c.add_tent(Location(0, 0)),
    #     c.add_tent(Location(2, 3)),
    #     c.get_tents(),
    #     )


if __name__ == '__main__':
    # check_mod()
    check2()
