

class Shape():
	def draw(self):
		pass


class Square(Shape):
	def draw(self):
		print 'draw square'

class Circle(Shape):
	def draw(self):
		print 'draw circle'

class Rectangle(Shape):
	def draw(self):
		print 'draw rectangle'


class Color():
	def fill(self):
		pass

class Red(Color):
	def fill(self):
		print 'fill Red'

class Green(Color):
	def fill(self):
		print 'fill Green'

class Blue(Color):
	def fill(self):
		print 'fill Blue'

#This class only need in language need to specify type of variable
class AbstractFactory():
	def getShape(self, shape):
		pass

	def getColor(self, color):
		pass	

class ShapeFactory(AbstractFactory):
	def getShape(self, shape):
		if shape == 'circle':
			return Circle()
		elif shape == 'rect':
			return Rectangle()
		elif shape == 'square':
			return Square()
		return False

class ColorFactory(AbstractFactory):
	def getColor(self, color):
		if color == 'red':
			return Red()
		elif color == 'green':
			return Green()
		elif color == 'blue':
			return Blue()
		return False


class FactoryProduce():
	def getFactory(self, name):
		if name == 'shape':
			return ShapeFactory()
		elif name == 'color':
			return ColorFactory()


if __name__ == '__main__':
	shapeFactory = FactoryProduce().getFactory('shape')
	circle = shapeFactory.getShape('circle')
	circle.draw()



	colorFactory = FactoryProduce().getFactory('color')
	red = colorFactory.getColor('red')
	red.fill()


