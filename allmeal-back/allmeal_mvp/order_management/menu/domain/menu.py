from datetime import date


class Menu:
    def __init__(self, starter: str, main_course: str, dessert: str, menu_date: date):
        self.starter = starter
        self.main_course = main_course
        self.dessert = dessert
        self.date = menu_date

    
