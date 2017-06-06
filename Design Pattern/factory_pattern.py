class Shape():
	def draw():
		pass


class Circle(Shape):
	def draw(self):
		print 'draw circle'


class Square(Shape):
	def draw(self):
		print 'draw Square'

class Rectangle(Shape):
	def draw(self):
		print 'draw Rectangle'


class shapeFactory():
	def getShape(self, shape):
		if shape == 'cirle':
			return Circle()
		elif shape == 'square':
			return Square()
		elif shape == 'rect':
			return Rectangle()

		return False


if __name__ == '__main__':
	cirle = shapeFactory().getShape('cirle')
	cirle.draw()

	square = shapeFactory().getShape('square')
	square.draw()
