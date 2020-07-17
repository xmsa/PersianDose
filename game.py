from gui import *

class Game:
	loc=list()
	def Start(self):
		self.player1,self.player2,self.mod =Display_Start()

		for i in range(26):
			self.loc.append(str(i))

		Display_Bord(self.loc)

		self.Play()
		

	def Play(self):
		if self.mod==1:
			self.Play_Uesr_VS_Uesr()
		else:
			self.Play_CPU_VS_Uesr()

	def Play_Uesr_VS_Uesr(self):
		for i in range (25):
			if i%2==0:
				self.SetBead(self.player1)
			elif i%2==1:
				self.SetBead(self.player2)
			Display_Bord(self.loc)
			if self.win():
				return
		print('The game draws')

	def Play_CPU_VS_Uesr(self):
		pass

	def SetBead(self, st):
		while True:
			try:
				inp=int(input("NO.: "))
				int(self.loc[inp])
				self.loc[inp]=st
				return
			except:
				print('try')
	def win(self):
		r=0 or self.check(25, 24, 23)
		r=r or self.check(17 ,16, 15 )

		r=r or self.check(9 ,8, 7 )
		r=r or self.check(3, 4 ,5 )
		r=r or self.check(11 ,12 ,13 )
		r=r or self.check(19, 20 ,21)

		r=r or self.check(25, 18, 19)
		r=r or self.check(17 ,10, 11 )
		r=r or self.check(9 ,2, 3 )
		r=r or self.check(7, 6, 5)
		r=r or self.check(15 ,14, 13 )
		r=r or self.check(23 ,22, 21)

		r=r or self.check(25 ,17, 9, 1)
		r=r or self.check(17, 9, 1 ,5)
		r=r or self.check(9, 1, 5 ,13 )
		r=r or self.check(1 ,5, 13 ,21)

		r=r or self.check(18 ,10, 2 ,1)
		r=r or self.check(10, 2, 1 ,6)
		r=r or self.check(2 ,1 ,6 ,14 )
		r=r or self.check(1 , 6 ,14, 22)

		r=r or self.check(19, 11 ,3, 1)
		r=r or self.check(11, 3 ,1 ,7)
		r=r or self.check(3 ,1, 7, 15 )
		r=r or self.check(1, 7 ,15 ,23)

		r=r or self.check(24, 16, 8 ,1)
		r=r or self.check(16, 8, 1 ,4 )
		r=r or self.check(8, 1, 4 ,12)
		r=r or self.check(4 ,1, 12 ,20)
		if r:
			return True

	def check(self,l1,l2,l3 ,l4=0):
		if l4==0:
			if self.loc[l1]==self.loc[l2] and self.loc[l2]==self.loc[l3]:
				print("win {:s}".format(self.loc[l2]))
				return True
			else:
				return False

		else:
			if self.loc[l1]==self.loc[l2] and self.loc[l2]==self.loc[l3] and self.loc[l2]==self.loc[l4]:
				print("win {:s}".format(self.loc[l2]))
				return True
			else:
				return False