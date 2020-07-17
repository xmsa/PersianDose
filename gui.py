def Display_Start():
	print('1-(User VS. User) or 2-(User VS. CPU)')
	mod=int(raw_input('Input Mod (Defalt: 1): '))
	Bead1=raw_input('Bead Player 1: ')
	Bead2=raw_input('Bead Player 2: ')
	
	if not mod ==1:
		mod=1
	return Bead1,Bead2 ,mod

def Display_Bord(loc):
	print('___________________________________________\n')
	print('{:2s}           {:2s}           {:2s}'.format(loc[25],loc[18],loc[19]))
	print('    {:2s}       {:2s}       {:2s}'.format(loc[17],loc[10],loc[11]))
	print('        {:2s}   {:2s}   {:2s}'.format(loc[9],loc[2],loc[3]))
	print('{:2s}  {:2s}  {:2s}   {:2s}   {:2s}  {:2s}  {:2s}'.format(loc[24],loc[16],loc[8],loc[1],loc[4],loc[12],loc[20]))
	print('        {:2s}   {:2s}   {:2s}'.format(loc[7],loc[6],loc[5]))
	print('    {:2s}       {:2s}       {:2s}'.format(loc[15],loc[14],loc[13]))
	print('{:2s}           {:2s}           {:2s}'.format(loc[23],loc[22],loc[21]))
	print('___________________________________________')