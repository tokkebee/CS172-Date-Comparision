#Oliver (Ollie) Kim
#October 10, 2024

#CS172 HW02 The passage of time
#module for Date class

class Date():
    #constructor
    #takes month, day, and year
    #default is January 1, 1900
    def __init__(self, month = 1, day = 1, year = 1900):
        self.__month = month
        self.__day = day
        self.__year = year

    #getters
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day
    def getYear(self):
        return self.__year
    
    #setters
    #changes date by adding days
    def changeDate(self, days):
        self.__day += days
        oddMonths = {1, 3, 5, 7, 8, 10, 12}  #31 days
        evenMonths = {4, 6, 9, 11}            #30 days
        daysInFebruary = 28 
        while True:
            #days to months
            if self.__month in oddMonths:
                daysInMonth = 31
            elif self.__month == 2:
                daysInMonth = daysInFebruary
            else:
                daysInMonth = 30

            if self.__day <= daysInMonth:
                return

            self.__day -= daysInMonth
            self.__month += 1
            
            #months to years
            if self.__month > 12:
                self.__month = 1
                self.__year += 1
        # self.__day += days
        # oddMonths = {1, 3, 5, 8, 10, 12} #31 days
        # evenMonths = {2, 4, 6, 9, 11} #30 days
        
        # #carrying over days to months
        # if self.__month in oddMonths:
        #     if self.__day > 31:
        #         temp = self.__day // 31
        #         self.__day %= 31
        #         self.__month += temp
        # elif self.__month in evenMonths:
        #     if self.__month == 2:
        #         temp = self.__day // 28
        #         self.__day %= 28
        #         self.__month += temp
        #     else:
        #         temp = self.__day // 30
        #         self.__day %= 30
        #         self.__month += temp
        
        # #carrying over months to years
        # if self.__month > 12:
        #     temp = self.__month // 12
        #     self.__month %= 12
        #     self.__year += temp

    #string overload
    def __str__(self):
        return f'{self.__month:02d}/{self.__day:02d}/{self.__year:04d}'
    
    #comparisions overload
    def __eq__(self, other): #==
        if (self.__month==other.getMonth()) and (self.__day==other.getDay()) and (self.__year==other.getYear()):
            return True
        else:
            return False
    def __ne__(self, other): #!=
        if (self.__month==other.getMonth()) and (self.__day==other.getDay()) and (self.__year==other.getYear()):
            return False
        else:
            return True
    def __lt__(self,other): #<
        if self.__year <= other.getYear():
            if self.__month <= other.getMonth():
                if self.__day < other.getDay():
                    return True
        return False
    def __le__(self, other): #<=
        if self.__year <= other.getYear():
            if self.__month <= other.getMonth():
                if self.__day <= other.getDay():
                    return True
        return False
    def __gt__(self, other): #>
        if self.__year >= other.getYear():
            if self.__month >= other.getMonth():
                if self.__day > other.getDay():
                    return True
        return False
    def __ge__(self, other): #>=
        if self.__year >= other.getYear():
            if self.__month >= other.getMonth():
                if self.__day >= other.getDay():
                    return True
        return False
    
    #subscript overload, getitem
    def __getitem__(self, index):
        if index == 0:
            return self.__month
        elif index == 1:
            return self.__day
        elif index == 2:
            return self.__year
        else:
            raise IndexError("Index out  of Bounds")
        
# date1 = Date(12,24,2004)
# date2 = Date(9,17,2004)
# date3 = Date(9,17,2004)

# print(date1, date2)
# print(type(date1))
# print((date1 < date2))
# print((date1 > date2))
# print(date2 != date3)
# print( 1 != 1)

# if (date1 < date2) == True:
#     print(f"{date1} is before {date2}")
# elif (date1 > date2) == True:
#     print(f"{date1} is after {date2}")
# elif date1 == date2:
#     print("same fucking day")