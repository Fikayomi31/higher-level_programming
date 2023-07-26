#!/usr/bin/python3
import datetime

"""Defining class user"""
class User:

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]


    def age(self):

        today = datetime.date(2001, 5, 12)
        yy = int(self.birthday[0:4])
        mm = int(self.birthday[5:7])
        dd = int(self.birthday[8:10])
        dob = datetime.date(yy, mm, dd) #Date of birth
        ages_in_days = (today - dob).days
        ages_in_years = (ages_in_days / 365)
        return int(ages_in_years)

user = User("Dave Bowman", "1971-03-15")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())

help(User)
