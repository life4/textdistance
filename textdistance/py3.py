from textdistance.internal import w_intern

@staticmethod
def w(f, *texts, equality=False):
	return w_intern(f, equality, *texts)
