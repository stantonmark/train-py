

class TrainingCourse:
    def __init__(self, title, duration, pricePerPerson, delegates=None):
        self.title = title
        self.duration = duration
        self.pricePerPerson = pricePerPerson
        self.delegates = delegates or []
    
    def addDelegates(self, name):
        self.delegates.append(name)
        
    def getTotalRevenue(self):
        return len(self.delegates) * self.pricePerPerson

    
# Create training course object 
course = TrainingCourse(
    title="Python Programming 1",
    duration=4,
    pricePerPerson=1600,
)
    