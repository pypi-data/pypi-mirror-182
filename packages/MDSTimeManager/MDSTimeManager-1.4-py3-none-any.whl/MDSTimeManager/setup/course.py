class Course:
    def __init__(self, cname, instructor, block, rank=1):
        self.__cname = cname
        self.__instructor = instructor
        self.__block = block
        self.__rank = rank
        self.__deliverables = []
    
    @property
    def cname(self):    
        return self.__cname
    
    @property
    def instructor(self):    
        return self.__instructor
    
    @property
    def block(self):    
        return self.__block
    
    @property
    def rank(self):    
        return self.__rank
    
    @property
    def deliverables(self):    
        return self.__deliverables
        
    @cname.setter
    def cname(self, cname):
        self.__cname = cname
        
    @instructor.setter
    def instructor(self, instructor):
        self.__instructor = instructor
    
    @block.setter
    def block(self, block):
        self.__block = block
        
    @rank.setter
    def rank(self, rank):
        self.__rank = rank
        
    @deliverables.setter
    def deliverables(self, deliverable):
        self.__deliverables.append(deliverable)

    @cname.deleter
    def cname(self):
        del self.__cname
        
    @instructor.deleter
    def instructor(self):
        del self.__instructor
        
    @block.deleter
    def block(self):
        del self.__block
        
    @rank.deleter
    def rank(self):
        del self.__rank
    
    @deliverables.deleter
    def deliverables(self):
        del self.__deliverables
        
    def __str__(self):
        return self.__cname
         
class Deliverable:
    def __init__(self, dname, date, status):
        self.__dname = dname
        self.__date = date
        self.__status = status
        
    @property
    def dname(self):    
        return self.__dname
    
    @property
    def date(self):    
        return self.__date
    
    @property
    def status(self):    
        return self.__status
    
    @dname.setter
    def dname(self, dname):
        self.__dname = dname
        
    @date.setter
    def date(self, date):
        self.__date = date
    
    @status.setter
    def status(self, status):
        self.__status = status
        
    @dname.deleter
    def dname(self):
        del self.__dname
        
    @date.deleter
    def date(self):
        del self.__date
        
    @status.deleter
    def status(self):
        del self.__status
        
    def __str__(self):
        return f"{self.__dname:31} due on: {self.__date} MM-DD"
        
class Quiz(Deliverable):
    def __init__(self, dname, date, status="Incomplete", topics="", qtype=""):
        Deliverable.__init__(self,dname,date,status)
        self.__topics = topics
        self.__qtype = qtype

    @property
    def topics(self):    
        return self.__topics
    
    @property
    def qtype(self):    
        return self.__qtype
    
    @topics.setter
    def topics(self, topics):
        self.__topics = topics
        
    @qtype.setter
    def qtype(self, qtype):
        self.__qtype = qtype

    @topics.deleter
    def topics(self):
        del self.__topics
        
    @qtype.deleter
    def qtype(self):
        del self.__qtype

class AssignLab(Deliverable):
    def __init__(self, dname, date, status="Incomplete", dur=1, durleft="", subloc=""):
        Deliverable.__init__(self,dname,date,status)

        self.__date = date
        self.__dur = dur
        self.__durleft = durleft
        self.__subloc = subloc

    @property
    def date(self):    
        return self.__date

        self.__dur = dur
        self.__durleft = durleft
        self.__subloc = subloc
    
    @property
    def dur(self):    
        return self.__dur
    
    @property
    def durleft(self):    
        return self.__durleft
    
    @property
    def subloc(self):    
        return self.__subloc
    
    @date.setter
    def date(self, date):
        self.__date = date
        
    @dur.setter
    def dur(self, dur):
        self.__dur = dur
    
    @durleft.setter
    def durleft(self, durleft):
        self.__durleft = durleft
        
    @subloc.setter
    def subloc(self, subloc):
        self.__subloc = subloc

    @date.deleter
    def date(self):
        del self.__date
        
    @dur.deleter
    def dur(self):
        del self.__dur
        
    @durleft.deleter
    def durleft(self):
        del self.__durleft
    
    @subloc.deleter
    def subloc(self):
        del self.__subloc

class Project(Deliverable):
    def __init__(self, dname, date, status="Incomplete", milestones="", dur=1, durleft="", repo=""):
        Deliverable.__init__(self,dname,date,status)
        self.__milestones = milestones
        self.__dur = dur
        self.__durleft = durleft
        self.__repo = repo
    
    @property
    def milestones(self):    
        return self.__milestones
    
    @property
    def dur(self):    
        return self.__dur
    
    @property
    def durleft(self):    
        return self.__durleft
    
    @property
    def repo(self):    
        return self.__repo
    
    @milestones.setter
    def milestones(self, milestones):
        self.__milestones = milestones
        
    @dur.setter
    def dur(self, dur):
        self.__dur = dur
    
    @durleft.setter
    def durleft(self, durleft):
        self.__durleft = durleft
        
    @repo.setter
    def repo(self, repo):
        self.__repo = repo

    @milestones.deleter
    def milestones(self):
        del self.__milestones
        
    @dur.deleter
    def dur(self):
        del self.__dur
        
    @durleft.deleter
    def durleft(self):
        del self.__durleft
    
    @repo.deleter
    def repo(self):
        del self.__repo