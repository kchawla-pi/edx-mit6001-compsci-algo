class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        common = set(self.vals).intersection(other.vals)
        common = sorted(common)
        temp_intSet = intSet()
        try:
            [temp_intSet.insert(val) for val in common]
        except TypeError:
            return temp_intSet
        else:
            return temp_intSet
            
    def __len__(self):
        return len(self.vals)

if __name__ == '__main__':
    iSet1 = intSet()
    iSet2 = intSet()
    iSet3 = intSet()
    iSet4 = intSet()
    
    [iSet1.insert(val) for val in {1, 2, 3}]
    [iSet2.insert(val) for val in {3, 4}]
    [iSet3.insert(val) for val in {3, 2, 4}]
    [iSet4.insert(val) for val in {-1, 5}]
    
    # [print(int_set_.vals) for int_set_ in (iSet1, iSet2, iSet3)]
    
    # print(iSet1.intersect(iSet2))
    # print(set(iSet1.vals).intersection(iSet2.vals))
    # print(iSet1.intersect(iSet3))
    
    
    setA = intSet()
    setB = intSet()
    setC = intSet()
    setD = intSet()
    setE = intSet()
    
    [setA.insert(value) for value in {-17,-12,-7,-5,-4,-2,3,12,15,20}]
    [setB.insert(value) for value in {-17,-5,5,6,10,12,14,16,18}]
    [setC.insert(value) for value in {99, -78, 81}]
    
    print(setA)
    print(setB)
    print(setA.intersect(setB))
    print(setB.intersect(setC))
    print(setA.intersect(setC))
    print(type(setA.intersect(setD)))
    print(setD.intersect(setE))
    
    print({-17,-12,-7,-5,-4,-2,3,12,15,20}.intersection({99, -78, 81}))
