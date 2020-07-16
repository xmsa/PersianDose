def Display():
	print('1-(User VS. User) or 2-(User VS. CPU)')
	mod=int(input('Input Mod (Defalt: 2): '))
	XO=int(input('1- X or 2- O (Defalt: X): '))
	if not XO ==2:
		XO=1
	if not mod ==1:
		mod=2
	return XO ,mod

def DisplayPage(loc):
	print('___________________________________________\n')
	print('{:2s}           {:2s}           {:2s}'.format(loc[25],loc[18],loc[19]))
	print('    {:2s}       {:2s}       {:2s}'.format(loc[17],loc[10],loc[11]))
	print('        {:2s}   {:2s}   {:2s}'.format(loc[9],loc[2],loc[3]))
	print('{:2s}  {:2s}  {:2s}   {:2s}   {:2s}  {:2s}  {:2s}'.format(loc[24],loc[16],loc[8],loc[1],loc[4],loc[12],loc[20]))
	print('        {:2s}   {:2s}   {:2s}'.format(loc[7],loc[6],loc[5]))
	print('    {:2s}       {:2s}       {:2s}'.format(loc[15],loc[14],loc[13]))
	print('{:2s}           {:2s}           {:2s}'.format(loc[23],loc[22],loc[21]))
	print('___________________________________________')

def win():
	r=check(25,18, 19)
	r=r or check(17 ,10, 11 )
	r=r or check(15 ,14, 13 )
	r=r or check(23 ,22, 21 )
	r=r or check(12 ,20 ,4 )
	r=r or check(24 ,15, 8)
	r=r or check(12 ,1 , 4  )
	r=r or check(16 ,8 , 1)
	r=r or check(8  ,1  ,4 )
	r=r or check(7 , 6  ,5 )
	r=r or check(9  ,2,  3 )
	r=r or check(17 ,16, 15 )
	r=r or check(25 ,24, 23 )
	r=r or check(7, 9, 8)
	r=r or check(18 ,10, 2)
	r=r or check(10 ,2 ,1 )
	r=r or check(1, 6 ,14)
	r=r or check(2 ,1 ,6 )
	r=r or check(6 ,14, 22 )
	r=r or check(3 ,4 ,5 )
	r=r or check(11 ,12, 13 )
	r=r or check(19, 20 ,21)
	r=r or check(25 ,17, 9)
	r=r or check(17, 9, 1)
	r=r or check(9  ,1 ,5 )
	r=r or check(1  ,5 ,13)
	r=r or check(5 , 13 ,21)
	r=r or check(19 ,11 ,3 )
	r=r or check(11, 3, 1)
	r=r or check(3 , 1 ,7 )
	r=r or check(17 , 1,5 )
	r=r or check(7 , 15 ,23)
	if r:
		return True
def SetBead(st):
	while True:
		try:
			inp=int(input("NO.: "))
			int(loc[inp])
			loc[inp]=st
			return
		except:
			print('try')
	
def check(l1,l2,l3):
	if loc[l1]==loc[l2] and loc[l2]==loc[l3]:
		print("win {:s}".format(loc[l2]))
		return True
	else:
		return False

#mod , XO =Display()
loc=list()
for i in range(0,26):
	loc.append(str(i))

DisplayPage(loc)
for i in range(1,27):
	if i%2==0:
		SetBead('XX')
	else :
		SetBead('OO')
	DisplayPage(loc)
	if win():
		break