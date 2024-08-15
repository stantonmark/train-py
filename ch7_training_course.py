# ch7_training_course.py

class TrainingCourse:
    def __init__(self, title, duration, pricePerPerson, delegates=None):
        self.title = title
        self.duration = duration
        self.pricePerPerson = pricePerPerson
        self.delegates = delegates or []  # Initialize delegates to an empty list if None is provided

    def addDelegates(self, name):
        self.delegates.append(name)

    def getTotalRevenue(self):
        return len(self.delegates) * self.pricePerPerson


# Create a TrainingCourse object
course = TrainingCourse(
    title="Python Programming 1",
    duration=4,
    pricePerPerson=1600,
)

# Add some delegates
course.addDelegates("Alice")
course.addDelegates("Bob")
course.addDelegates("Charlie")

# Display the total revenue
total_revenue = course.getTotalRevenue()
print("Total Revenue:", total_revenue)