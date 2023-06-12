def some_func():
	print("Inside some_func")
	def some_inner_func():
		print("Inside inner function")
	some_inner_func()
	print("Try printing var")
some_func()
