def makestr(x, y, z):
	return '{}時の{}は{}'.format(x,y,z)

if __name__ == '__main__':
	print(makestr(x=12, y='気温', z=22.4))
