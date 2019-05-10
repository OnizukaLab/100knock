from q_5 import *

if __name__ == '__main__':
	s1 = 'paraparaparadise'
	s2 = 'paragraph'
	X,Y = set(n_gram(s1, 2)),set(n_gram(s2, 2))
	print('X|Y : {}'.format(X|Y))
	print('X&Y : {}'.format(X&Y))
	print('X-Y : {}'.format(X-Y))
	print('Y-X : {}'.format(Y-X))
	print("'se' in X : {}".format('se' in X))
	print("'se' in Y : {}".format('se' in Y))
	
