#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count, 
    # turn_page
    ):
        self.title = title
        self.page_count = page_count
        # self.turn_page = turn_page

    # turn_page = "Flipping the page...wow, you read fast!"

    def get_page(self):
        return self._page_count
    def set_page(self, value):
        if type(value) is int:
            self._page_count = value
        else:
            print("page_count must be an integer")    
    page_count = property(get_page, set_page)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # turn_page(Book)

    # def get_turn(self):
    #     return self._turn_page
    # def set_turn(self, value):
    #     if type(value) is str:
    #         self._turn_page = value
    #         print("Flipping the page...wow, you read fast!")
       
    # turn_page= property(get_turn, set_turn)