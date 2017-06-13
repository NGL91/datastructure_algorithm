class Item():
	def name(self):
		pass

	def packing(self):
		pass

	def price(self):
		pass

class Packing():
	def packed(self):
		pass

class Wrapper(Packing):
	def packed(self):
		return 'packed by wrapper'

class Bottle(Packing):
	def packed(self):
		return 'packed in bottle'

class Burger(Item):
	def packing(self):
		return Wrapper().packed()

	


class BurgeVerge(Burger):
	def price(self):
		return 25

	def name(self):
		return 'BurgeVerge'

class BurgeChicken(Burger):
	def price(self):
		return 30

	def name(self):
		return 'BurgeChicken'


class Drink(Item):
	def packing(self):
		return Bottle().packed()

class ColdDrink(Drink):
	def name(self):
		return 'ColdDrink'

	def price(self):
		return 10

class HotDrink(Drink):
	def name(self):
		return 'HotDrink'

	def price(self):
		return 20

class Meal():
	items = []

	def addItem(self, item):
		self.items.append(item)

	def getCost(self):
		cost = 0
		for item in self.items:
			cost+= item.price()
		print 'Cost=',cost

	def showName(self):
		for item in self.items:
			print 'Name=',item.name()
			print 'Price=',item.price()
			print 'Packed=',item.packing()
			print '\n'

class MealPrepare():
	def prepareVergeMeal(self):
		meal = Meal()
		meal.addItem(BurgeVerge())
		meal.addItem(ColdDrink())
		return meal

	def prepareChickenMeal(self):
		meal = Meal()
		meal.addItem(BurgeChicken())
		meal.addItem(HotDrink())
		return meal 

if __name__ == '__main__':
	vergeMeal = MealPrepare().prepareVergeMeal()
	vergeMeal.showName()

	chickenMeal = MealPrepare().prepareChickenMeal()
	chickenMeal.showName()
