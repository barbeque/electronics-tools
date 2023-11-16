import csv, sys

if len(sys.argv) < 3:
	print(f'Usage: {sys.argv[0]} [uF] [V]')
	sys.exit(1)

row = []
with open('machinist-esr.tsv', 'r') as f:
	rd = csv.reader(f, delimiter='\t')
	for r in rd:
		row.append(r)
		print(r)

capacitance = int(sys.argv[1])
voltage = int(sys.argv[2])

print('Searching for C =', capacitance,'V =', voltage)

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
			print('Max ESR=',maximum_esr)
		break
else:
	print('Could not find capacitance value', capacitance, 'in this ESR table. It cannot yet interpolate.')
	sys.exit(3)