# class Anton:
#     location = "Новосибирск"
#
#
#     def __init__(self, rost=1, ves=2):
#         self.height = rost
#         self.height = ves
#         self.otkuda = Anton.location
#
#     def __private(self):
#         pass
#
#     def __public(self):
#         pass
#
#
# chelovek = Anton(10)
# chelovek = Anton(15)
# print(chelovek.height)


class Human:
    default_name = "human"
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 5
        self.__hose = None

    def __make_deal(self, dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True
        else:
            return False


    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__house = dom
            return "купили по кайфу"
        else:
            return f"денег не хватило, нужоно еще {dom.final_price() - self.__money}"

class House:
    def final_price(self):
        return 50

chelovek = Human("Anton")
dom1 = House()
dom15 = House()

print(chelovek.buy_house(dom1))



