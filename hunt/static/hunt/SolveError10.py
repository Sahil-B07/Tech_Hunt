#Don't change code only try to Stop the infinite Recursive call by adding your own code

def fun(num):

	for i in range(2):
		fun(num*i)
		
fun(1)


