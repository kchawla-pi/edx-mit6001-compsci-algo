class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except KeyError:
            pass
        

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        return self.vals.get(e, 0)
    
    def __add__(self, other):
        """
        Overloaded '+' operator.
        Returns: union(self.vals, Bag().vals)
        """
        combo_dict = self.vals.copy()
        combo_dict.update({key: combo_dict.get(key, 0) + val for key, val in other.vals.items()})
        new_bag = Bag()
        new_bag.vals = combo_dict
        return new_bag

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            self.vals.pop(e)
        except KeyError:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in list(self.vals.keys())

def check_output():
    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    print(d1, '\t', 'expected: 4:2')
    d1.remove(2)
    print(d1, '\t', 'expected: 4:2')

    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    d1.insert(4)
    print(d1.count(2), '\texpected: 0')
    print(d1.count(4), '\texpected: 3')

    a = Bag()
    a.insert(4)
    a.insert(3)
    b = Bag()
    b.insert(4)
    # b.insert(5)
    print(a + b)
    print('expected:\n', '3:1\n', '4:2')
    
    c = a + b
    print(c)

    d1 = ASet()
    d1.insert(4)
    d1.insert(4)

    d1.remove(2)
    print(d1, 'expected: 4:2')

    d1.remove(4)
    print(d1, 'expected: ', '')

    d1 = ASet()
    d1.insert(4)
    print(d1.is_in(4), 'expected: ', True)
    d1.insert(5)
    print(d1.is_in(5), 'expected: ', True)
    d1.remove(5)
    print(d1.is_in(5), 'expected: ', False)
    
        
if __name__ == '__main__':
    pass
    check_output()
