import csv, sys

if len(sys.argv) < 3:
	print(f'Usage: {sys.argv[0]} [uF] [V] <esr>')
	sys.exit(1)

row = []
with open('machinist-esr.tsv', 'r') as f:
	rd = csv.reader(f, delimiter='\t')
	for r in rd:
		row.append(r)
		print(r)

capacitance = int(sys.argv[1])
voltage = int(sys.argv[2])

if(len(sys.argv) > 3):
	esr = float(sys.argv[3])
else:
	esr = -1

print('Searching for C =', capacitance,'V =', voltage)
if(esr > 0):
	print('Judging ESR=', esr)

# find the column for voltage
for i in range(0, len(row[0])):
	if str(voltage) in row[0][i]:
		print('Found voltage', row[0][i])
		voltage_column = i
		break
else:
	print('Could not find voltage value', voltage, 'in this ESR table. It cannot yet interpolate.')
	sys.exit(2)

# find the row for capacitance
for i in range(0, len(row) - 1):
	if str(capacitance) in row[i + 1][0]:
		print('Found capacitance', row[i+1][0])
		maximum_esr = row[i + 1][voltage_column]
		if(len(maximum_esr) < 1):
			print('No idea what the ESR for this pair is. Table is missing data...')
		else:
			maximum_esr = float(maximum_esr)
			print('Max ESR=',maximum_esr)
			if(esr > 0):
				# judgment mode
				if maximum_esr < esr:
					print(f'Bad (max {maximum_esr})')
				elif abs(maximum_esr - esr) < 0.3:
					print(f'Marginal (max {maximum_esr})')
				else:
					print(f'Good (max {maximum_esr})')
		break
else:
	print('Could not find capacitance value', capacitance, 'in this ESR table. It cannot yet interpolate.')
	sys.exit(3)