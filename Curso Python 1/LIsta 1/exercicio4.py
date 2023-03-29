segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dia = segundos // 86400
diatotal = segundos % 86400

hora = diatotal // 3600
hrtotal = diatotal % 3600

minutos = hrtotal // 60
mintotal = hrtotal % 60

segundos = mintotal


print(dia,"dias,", hora, "horas,", minutos, "minutos e", segundos,"segundos.")

