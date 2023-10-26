
class Project:

    def __init__(self, name, title="", description="", background_color="black"):
        self.name = name
        self.title = title
        self.description = description
        self.background_color = background_color

    def get_next(self):
        for i, project in enumerate(PROJECT_LIST):
            if project == self:
                return PROJECT_LIST[(i + 1) % len(PROJECT_LIST)]


PROJECT_LIST = [
    Project("spooky_dude", title="Spooky Dude", description="Look at this spooky motherfucker.",
            background_color="rgb(150, 150, 150)"),
    Project("bald_guy", title="Bald Guy"),
    Project("beb", background_color="rgb(77, 71, 69)"),
    Project("lady2", title="Lady #2", background_color="rgb(60, 61, 71)"),
]
