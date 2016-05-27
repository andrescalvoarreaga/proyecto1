def prob_1(n1):
	if n1 % 2 == 0 :
		return ("True")
	else:
		return ("False")


def prob_2(f):
	c = (f-32)*(5/9)
	return(c)

def prob_3(base, potencia):
	resul = 1
	i = 0
	for i in range(potencia):
		resul = resul * base 
	return (resul)
