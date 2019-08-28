import datetime


class Building:
    def __init__(self, address, stories):
        self.designer = "Jake Scott"
        self.date_constructed = str(datetime.datetime.now().strftime("%Y-%m-%d at %H:%M"))
        self.owner = "Sampson Simpson"
        self.address = ""
        self.stories = stories
    def construct(self, datetime):
        now = datetime.datetime.now()
        self.date_constructed = str(now)
    def purchase(self, owner):
        self.owner = owner
        print(f'New owner is {self.owner} designed by {self.designer} on {self.date_constructed} and has {self.stories} stories')

eight_hundred_eighth = Building("800 8th Street", 12)
ninteeth_time = Building("1900 19th ave North", 1088)
seventeeth_wow = Building("1092 17th St", 11)


eight_hundred_eighth.purchase("Susan Simpson")
ninteeth_time.purchase("Susan Simpson")
seventeeth_wow.purchase("Susan Simpson")











# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories
