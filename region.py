class Region:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def __hash__(self):  
        return hash(self.name)  # hash based on Region name

    def __eq__(self, other):  
        return isinstance(other, Region) and self.name == other.name # equality comparison