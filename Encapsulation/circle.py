class Circle:
    def __init__(self, radius:int):
        self._radius:int = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value:int):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value