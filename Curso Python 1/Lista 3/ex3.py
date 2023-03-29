n = int(input("Digite um número inteiro:"))

s = 0

while n != 0:
	resto = n % 10
	n = (n - resto)// 10
	s += resto
	
print(s)
		