from internal import w_intern

@staticmethod
def w(f, equality=False, *texts):
	return w_intern(f, equality, *texts)
