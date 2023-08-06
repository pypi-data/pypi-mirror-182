class Person:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

class Instructor(Person):
    def __init__(self, name, hours="Not Specified", comm="Not Specified"):
        Person.__init__(self,name)
        self.__teaches = []
        self.__hours = hours
        self.__comm = comm
    
    @property
    def teaches(self):
        return self.__teaches

    @property
    def hours(self):
        return self.__hours

    @property
    def comm(self):
        return self.__comm

    @teaches.setter
    def teaches(self, teach):
        self.__teaches.append(teach)
    
    @hours.setter
    def hours(self, hours):
        self.__hours = hours
    
    @comm.setter
    def comm(self, comm):
        self.__comm = comm
    
    @teaches.deleter
    def teaches(self):
        del self.__teaches

    @hours.deleter
    def hours(self):
        del self.__hours

    @comm.deleter
    def comm(self):
        del self.__comm

class Student(Person):
    def __init__(self, name, sID):
        Person.__init__(self,name)
        self.__sID = sID
        self.__courses = []
    
    @property
    def sID(self):
        return self.__sID
   
    @property
    def courses(self):
        return self.__courses

    @sID.setter
    def sID(self, sID):
        self.__sID = sID
    
    @courses.setter
    def courses(self, course):
        self.__courses.append(course) 
    
    @sID.deleter
    def sID(self):
        del self.__sID

    @courses.deleter
    def courses(self):
        del self.__courses