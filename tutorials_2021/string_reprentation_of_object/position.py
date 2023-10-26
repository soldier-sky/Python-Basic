class Position:
    
    def __init__(self, latitude, longitude):
        if not(-90 <=latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not(-180 <= longitude <=+180):
            raise ValueError(f"Longitude {longitude} out of range")
        
        self._latitude = latitude
        self._longitude= longitude
    
    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __repr__(self):
        ''' repr is intended for developers for debgging class etc to quick look
           at constructed obj
        '''
        #return f"{self.__class__} (latitude ={self.latitude}, longitude={self.longitude}"
        return f"{typename(self)} (latitude ={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        ''' str representaion of obj is for users who do not necssarly
            require debugging details like us developers
        '''
        return(f"{typename(self)}={abs(self.latitude)}* {self.longitude}*")


def typename(obj):
    return type(obj).__name__

class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass

