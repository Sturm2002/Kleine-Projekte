import turtle
from time import sleep
import os
import random


# Window setting
wn = turtle.Screen()
wn.title("Python Tetris")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)


Possible_Blocks = ["Rev_T", "1x4", "2x2", "Z", "Rev_Z","L","Rev_L"]
Comming_Blocks = []
Moving_Block = []
Placed_Blocks = []
hold_block = []
Clearing_Blocks_Cache = []

timer = 0
intervall = 30
showing = "Up"

Amount_Temp_Hold = 0

dgshowing = None
dgplaced = len(Placed_Blocks)
dgvar1 = None
dgvar2 = None
dgvar3 = None
debugarray = [dgplaced,dgshowing,dgvar1,dgvar2,dgvar3]

# Left Hold Border
Border_Hold_Left = turtle.Turtle()
Border_Hold_Left.shape("square")
Border_Hold_Left.color("white")
Border_Hold_Left.shapesize(5,0.2,0)
Border_Hold_Left.penup()
Border_Hold_Left.speed(0)

# Right Hold Border
Border_Hold_Right = turtle.Turtle()
Border_Hold_Right.shape("square")
Border_Hold_Right.color("white")
Border_Hold_Right.shapesize(5,0.2,0)
Border_Hold_Right.penup()
Border_Hold_Right.speed(0)

# Top Hold Border
Border_Hold_Top = turtle.Turtle()
Border_Hold_Top.shape("square")
Border_Hold_Top.color("white")
Border_Hold_Top.shapesize(0.2,5,0)
Border_Hold_Top.penup()
Border_Hold_Top.speed(0)

# Bottom Hold Border
Border_Hold_Bottom = turtle.Turtle()
Border_Hold_Bottom.shape("square")
Border_Hold_Bottom.color("white")
Border_Hold_Bottom.shapesize(0.2,5,0)
Border_Hold_Bottom.penup()
Border_Hold_Bottom.speed(0)


Border_Playfield_Left = turtle.Turtle()
Border_Playfield_Left.shape("square")
Border_Playfield_Left.color("white")
Border_Playfield_Left.shapesize(40,0.2,0)
Border_Playfield_Left.penup()
Border_Playfield_Left.speed(0)

Border_Playfield_Right = turtle.Turtle()
Border_Playfield_Right.shape("square")
Border_Playfield_Right.color("white")
Border_Playfield_Right.shapesize(40,0.2,0)
Border_Playfield_Right.penup()
Border_Playfield_Right.speed(0)

# Setting Border Positions ##########################################################

# Hold Borders
Border_Hold_Top.goto(-300,350)
Border_Hold_Left.goto(-350,300)
Border_Hold_Right.goto(-250,300)
Border_Hold_Bottom.goto(-300,250)

# Playfield Borders
Border_Playfield_Left.goto(-180,0)
Border_Playfield_Right.goto(180,0)

DebugTurtle = turtle.Turtle()
DebugTurtle.shape("square")
DebugTurtle.color("grey")
DebugTurtle.shapesize(0.2,0.2,0)
DebugTurtle.penup()
DebugTurtle.speed(0)



def Clear_Full_Lines():
	global Clearing_Blocks_Cache
	Lowest_CheckLine = -370
	Highest_CheckLine = 280
	Blocks_Found = 0
	for Line in range(Lowest_CheckLine,Highest_CheckLine, + 40):
		for FBlock in range(len(Placed_Blocks)):
			for PBlock in range(len(Placed_Blocks[FBlock]) -1):
				PBlock += 1

				if Placed_Blocks[FBlock][PBlock].ycor() < Line + 10 and Placed_Blocks[FBlock][PBlock].ycor() > Line - 10:
					Clearing_Blocks_Cache.append([FBlock,PBlock])
					Blocks_Found += 1
					#print("Found Block")
					
				DebugTurtle.goto(0,Line)
				wn.update()
				#sleep(0.1)
		if Blocks_Found == 0:
			Clearing_Blocks_Cache.clear()
			return

		elif Blocks_Found == 9:
			print("Full Line")
			for ClearF in range(len(Clearing_Blocks_Cache) -1):
				DeleteFBlock = Clearing_Blocks_Cache[ClearF][0]
				DeletePBlock = Clearing_Blocks_Cache[ClearF][1]
				Placed_Blocks[DeleteFBlock][DeletePBlock].color("white")
				#del Placed_Blocks[DeleteFBlock]#[DeletePBlock]
				#del Clearing_Blocks_Cache[ClearF]
				wn.update()


		print(Blocks_Found)
		Blocks_Found = 0
		

					

# Generating Block
lastblock = None
def GenNewBlock():
	global lastblock
	RanBlockSelecter = random.randint(0,6)
	if RanBlockSelecter == lastblock:
			GenNewBlock()
	else:
		CurCreatedBlock = []
		SelectedBlock = Possible_Blocks[RanBlockSelecter]
		lastblock = SelectedBlock
		
		for i in range(4):
			NewBlock = turtle.Turtle()
			NewBlock.penup()
			NewBlock.speed(0)
			NewBlock.shape("square")
			NewBlock.shapesize(2,2,0.1)
			NewBlock.goto(900,900)
			CurCreatedBlock.append(NewBlock)


		if SelectedBlock == "Rev_T":
			CurCreatedBlock.insert(0,"Rev_T")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("pink")
			

		if SelectedBlock == "1x4":
			CurCreatedBlock.insert(0,"1x4")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("blue")

		if SelectedBlock == "L":
			CurCreatedBlock.insert(0,"L")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("red")

		if SelectedBlock == "Rev_L":
			CurCreatedBlock.insert(0,"Rev_L")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("cyan")

		if SelectedBlock == "2x2":
			CurCreatedBlock.insert(0,"2x2")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("orange")

			

		if SelectedBlock == "Z":
			CurCreatedBlock.insert(0,"Z")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("green")
			

		if SelectedBlock == "Rev_Z":
			CurCreatedBlock.insert(0,"Rev_Z")
			for i in range(4):
				CurCreatedBlock[i+1].fillcolor("yellow")
			
		

		Comming_Blocks.append(CurCreatedBlock)


def Turn():
	global showing
	global dgshowing
	if showing == "Up":
		showing = "Right"
		dgshowing = "Right"
		SyncPos()

		if len(Placed_Blocks) == 0:
			for k in range(4):
				SyncPos()
				if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160):
					showing = "Up"
					dgshowing = "Up"
					SyncPos()
		else:
			for i in range(len(Placed_Blocks)):
				for j in range(4):
					j += 1
					for k in range(4):
						SyncPos()
						if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160) or (Moving_Block[0][k+1].xcor() < Placed_Blocks[i][j].xcor() + 20 and Moving_Block[0][k+1].xcor() > Placed_Blocks[i][j].xcor() - 20 and Moving_Block[0][k+1].ycor() < Placed_Blocks[i][j].ycor() + 20 and Moving_Block[0][k+1].ycor() > Placed_Blocks[i][j].ycor() - 20 ):
							showing = "Up"
							dgshowing = "Up"
							SyncPos()
		SyncPos()
		wn.update()
		return None

	if showing == "Right":
		showing = "Down"
		dgshowing = "Down"

		if len(Placed_Blocks) == 0:
			for k in range(4):
				SyncPos()
				if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160):
					showing = "Right"
					dgshowing = "Right"
					SyncPos()
		else:
			for i in range(len(Placed_Blocks)):
				for j in range(4):
					j += 1
					for k in range(4):
						SyncPos()
						if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160) or (Moving_Block[0][k+1].xcor() < Placed_Blocks[i][j].xcor() + 20 and Moving_Block[0][k+1].xcor() > Placed_Blocks[i][j].xcor() - 20 and Moving_Block[0][k+1].ycor() < Placed_Blocks[i][j].ycor() + 20 and Moving_Block[0][k+1].ycor() > Placed_Blocks[i][j].ycor() - 20 ):
							showing = "Right"
							dgshowing = "Right"
							SyncPos()

		return None
	
	if showing == "Down":
		showing = "Left"
		dgshowing = "Left"
		if len(Placed_Blocks) == 0:
			for k in range(4):
				SyncPos()
				if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160):
					showing = "Down"
					dgshowing = "Down"
					SyncPos()
		else:
			for i in range(len(Placed_Blocks)):
				for j in range(4):
					j += 1
					for k in range(4):
						SyncPos()
						if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160) or (Moving_Block[0][k+1].xcor() < Placed_Blocks[i][j].xcor() + 20 and Moving_Block[0][k+1].xcor() > Placed_Blocks[i][j].xcor() - 20 and Moving_Block[0][k+1].ycor() < Placed_Blocks[i][j].ycor() + 20 and Moving_Block[0][k+1].ycor() > Placed_Blocks[i][j].ycor() - 20 ):
							showing = "Down"
							dgshowing = "Down"
							SyncPos()


		return None

	if showing == "Left":
		showing = "Up"
		dgshowing = "Up"

		if len(Placed_Blocks) == 0:
			for k in range(4):
				SyncPos()
				if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160):
					showing = "Left"
					dgshowing = "Left"
					SyncPos()
		else:
			for i in range(len(Placed_Blocks)):
				for j in range(4):
					j += 1
					for k in range(4):
						SyncPos()
						if (Moving_Block[0][k+1].xcor() < -160) or (Moving_Block[0][k+1].xcor() > 160) or (Moving_Block[0][k+1].xcor() < Placed_Blocks[i][j].xcor() + 20 and Moving_Block[0][k+1].xcor() > Placed_Blocks[i][j].xcor() - 20 and Moving_Block[0][k+1].ycor() < Placed_Blocks[i][j].ycor() + 20 and Moving_Block[0][k+1].ycor() > Placed_Blocks[i][j].ycor() - 20 ):
							showing = "Left"
							dgshowing = "Left"
							SyncPos()


		return None

def Place_Hold_block1():
	hold_block[0][1].goto(-300,300)

def SyncPos():
	for syncblock in range(len(Comming_Blocks)):
		xpos = Comming_Blocks[syncblock][1].xcor()
		ypos = Comming_Blocks[syncblock][1].ycor()

		mvxpos = Moving_Block[0][1].xcor()
		mvypos = Moving_Block[0][1].ycor()

		if len(hold_block) == 0:
			pass
		else:
			holdposx = hold_block[0][1].xcor()
			holdposy = hold_block[0][1].ycor()

#  Comming Blocks Sy

		if Comming_Blocks[syncblock][0] == "Rev_T":
		
			Comming_Blocks[syncblock][2].goto((xpos + 40),ypos)
			Comming_Blocks[syncblock][3].goto((xpos - 40),ypos)
			Comming_Blocks[syncblock][4].goto(xpos,(ypos-40))


		if Comming_Blocks[syncblock][0] == "1x4":

			Comming_Blocks[syncblock][2].goto(xpos,(ypos + 40))
			Comming_Blocks[syncblock][3].goto(xpos,(ypos - 40))
			Comming_Blocks[syncblock][4].goto(xpos,(ypos - 80))


		if Comming_Blocks[syncblock][0] == "2x2":
			Comming_Blocks[syncblock][2].goto((xpos + 40),ypos)
			Comming_Blocks[syncblock][3].goto((xpos + 40),(ypos + 40))
			Comming_Blocks[syncblock][4].goto(xpos,(ypos + 40))

		if Comming_Blocks[syncblock][0] == "Rev_Z":
			Comming_Blocks[syncblock][2].goto((xpos + 40),(ypos+40))
			Comming_Blocks[syncblock][3].goto(xpos,(ypos+40))
			Comming_Blocks[syncblock][4].goto((xpos - 40),ypos)

		if Comming_Blocks[syncblock][0] == "Z":
			Comming_Blocks[syncblock][2].goto((xpos - 40),(ypos+40))
			Comming_Blocks[syncblock][3].goto(xpos,(ypos+40))
			Comming_Blocks[syncblock][4].goto((xpos + 40),ypos)

		if Comming_Blocks[syncblock][0] == "L":
			Comming_Blocks[syncblock][2].goto((xpos),(ypos+40))
			Comming_Blocks[syncblock][3].goto(xpos,(ypos-40))
			Comming_Blocks[syncblock][4].goto((xpos + 40),ypos - 40)

		if Comming_Blocks[syncblock][0] == "Rev_L":
			Comming_Blocks[syncblock][2].goto(xpos,(ypos+40))
			Comming_Blocks[syncblock][3].goto(xpos,(ypos-40))
			Comming_Blocks[syncblock][4].goto((xpos - 40),ypos - 40)

# Moving Block Sync

	if Moving_Block[0][0] == "Rev_T":
		if showing == "Up":
			Moving_Block[0][2].goto(mvxpos,(mvypos - 40))
			Moving_Block[0][3].goto((mvxpos - 40),mvypos)
			Moving_Block[0][4].goto((mvxpos + 40),mvypos)

		if showing == "Right":
			Moving_Block[0][2].goto(mvxpos,(mvypos - 40))
			Moving_Block[0][3].goto((mvxpos - 40),mvypos)
			Moving_Block[0][4].goto(mvxpos,mvypos + 40)

		if showing == "Down":
			Moving_Block[0][2].goto(mvxpos,(mvypos + 40))
			Moving_Block[0][3].goto((mvxpos - 40),mvypos)
			Moving_Block[0][4].goto((mvxpos + 40),mvypos)

		if showing == "Left":
			Moving_Block[0][2].goto(mvxpos,(mvypos - 40))
			Moving_Block[0][3].goto((mvxpos + 40),mvypos)
			Moving_Block[0][4].goto(mvxpos,mvypos + 40)

	if Moving_Block[0][0] == "1x4":
		if showing == "Up":
			Moving_Block[0][2].goto(mvxpos,mvypos - 40)
			Moving_Block[0][3].goto(mvxpos,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos,mvypos + 80)

		if showing == "Right":
			Moving_Block[0][2].goto(mvxpos - 40,mvypos)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos)
			Moving_Block[0][4].goto(mvxpos + 80,mvypos)

		if showing == "Down":
			Moving_Block[0][2].goto(mvxpos,mvypos + 40)
			Moving_Block[0][3].goto(mvxpos,mvypos - 40)
			Moving_Block[0][4].goto(mvxpos,mvypos - 80)

		if showing == "Left":
			Moving_Block[0][2].goto(mvxpos + 40,mvypos)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos)
			Moving_Block[0][4].goto(mvxpos - 80,mvypos)

	if Moving_Block[0][0] == "2x2":
		Moving_Block[0][2].goto(mvxpos,mvypos + 40)
		Moving_Block[0][3].goto(mvxpos + 40,mvypos + 40)
		Moving_Block[0][4].goto(mvxpos+ 40,mvypos)

	if Moving_Block[0][0] == "Rev_Z":
		if showing == "Up" or showing == "Down":
			Moving_Block[0][2].goto(mvxpos,mvypos - 40)	
			Moving_Block[0][3].goto(mvxpos - 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos- 40,mvypos)

		if showing == "Right" or showing == "Left":
			Moving_Block[0][2].goto(mvxpos,mvypos + 40)	
			Moving_Block[0][3].goto(mvxpos + 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos- 40,mvypos)

	if Moving_Block[0][0] == "Z":
		if showing == "Up" or showing == "Down":
			Moving_Block[0][2].goto(mvxpos,mvypos + 40)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos + 40,mvypos)

		if showing == "Right" or showing == "Left":
			Moving_Block[0][2].goto(mvxpos + 40,mvypos + 40)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos)
			Moving_Block[0][4].goto(mvxpos,mvypos - 40)

	if Moving_Block[0][0] == "L":
		if showing == "Up":
			Moving_Block[0][2].goto(mvxpos,mvypos - 40)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos - 40)
			Moving_Block[0][4].goto(mvxpos,mvypos + 40)

		if showing == "Right":
			Moving_Block[0][2].goto(mvxpos - 40,mvypos)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos -40)
			Moving_Block[0][4].goto(mvxpos + 40,mvypos)

		if showing == "Down":
			Moving_Block[0][2].goto(mvxpos,mvypos + 40)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos,mvypos - 40)

		if showing == "Left":
			Moving_Block[0][2].goto(mvxpos + 40,mvypos)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos - 40,mvypos)

	if Moving_Block[0][0] == "Rev_L":
		if showing == "Up":
			Moving_Block[0][2].goto(mvxpos,mvypos - 40)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos - 40)
			Moving_Block[0][4].goto(mvxpos,mvypos + 40)

		if showing == "Right":
			Moving_Block[0][2].goto(mvxpos - 40,mvypos)
			Moving_Block[0][3].goto(mvxpos - 40,mvypos +40)
			Moving_Block[0][4].goto(mvxpos + 40,mvypos)

		if showing == "Down":
			Moving_Block[0][2].goto(mvxpos,mvypos + 40)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos + 40)
			Moving_Block[0][4].goto(mvxpos,mvypos - 40)

		if showing == "Left":
			Moving_Block[0][2].goto(mvxpos + 40,mvypos)
			Moving_Block[0][3].goto(mvxpos + 40,mvypos - 40)
			Moving_Block[0][4].goto(mvxpos - 40,mvypos)

	Comming_Blocks[0][1].goto(320,200)
	Comming_Blocks[1][1].goto(320,100)
	Comming_Blocks[2][1].goto(320,-100)

# Hold Block Sync
	if len(hold_block) == 0:
		pass
	else:
		if hold_block[0][0] == "Rev_T":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,(holdposy - 40))
			hold_block[0][3].goto((holdposx - 40),holdposy)
			hold_block[0][4].goto((holdposx + 40),holdposy)

		if hold_block[0][0] == "1x4":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy - 40)
			hold_block[0][3].goto(holdposx,holdposy + 40)
			hold_block[0][4].goto(holdposx,holdposy + 80)
		
		if hold_block[0][0] == "2x2":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy + 40)
			hold_block[0][3].goto(holdposx + 40,holdposy + 40)
			hold_block[0][4].goto(holdposx+ 40,holdposy)

		if hold_block[0][0] == "Rev_Z":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy - 40)	
			hold_block[0][3].goto(holdposx - 40,holdposy + 40)
			hold_block[0][4].goto(holdposx- 40,holdposy)

		if hold_block[0][0] == "Z":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy + 40)
			hold_block[0][3].goto(holdposx - 40,holdposy + 40)
			hold_block[0][4].goto(holdposx + 40,holdposy)

		if hold_block[0][0] == "L":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy - 40)
			hold_block[0][3].goto(holdposx + 40,holdposy - 40)
			hold_block[0][4].goto(holdposx,holdposy + 40)

		if hold_block[0][0] == "Rev_L":
			Place_Hold_block1()
			hold_block[0][2].goto(holdposx,holdposy - 40)
			hold_block[0][3].goto(holdposx - 40,holdposy - 40)
			hold_block[0][4].goto(holdposx,holdposy + 40)
	

def GetNewBlock():
	global showing
	global Amount_Temp_Hold
	GenNewBlock()
	Moving_Block.append(Comming_Blocks[0])
	Moving_Block[0][1].sety(350)
	Moving_Block[0][1].setx(0)
	Comming_Blocks.pop(0)
	Amount_Temp_Hold = 0
	showing = "Up"
	Clear_Full_Lines()
	SyncPos()

# Defintions of keypresses

def key_down():
	owny = Moving_Block[0][1].ycor()
	ownx = Moving_Block[0][1].xcor()
	Moving_Block[0][1].goto(ownx,owny - 40)
	SyncPos()

def key_left():
	global dgvar1
	global dgvar2
	global dgvar3


	owny = Moving_Block[0][1].ycor()
	ownx = Moving_Block[0][1].xcor()

	if Moving_Block[0][1].xcor() > -160:
		if Moving_Block[0][2].xcor() > -160:
			if Moving_Block[0][3].xcor() > -160:
				if Moving_Block[0][4].xcor() > -160:
					
					if len(Placed_Blocks) == 0:
						Moving_Block[0][1].goto(ownx - 40,owny)


					elif len(Placed_Blocks) == 1:
						for j in range(4):
							j += 1

							for k in range(4):
								k += 1

								if Moving_Block[0][k].xcor() - 40 < Placed_Blocks[0][j].xcor() + 20 and Moving_Block[0][k].xcor() - 40 > Placed_Blocks[0][j].xcor() - 20 and Moving_Block[0][k].ycor() < Placed_Blocks[0][j].ycor() + 20 and Moving_Block[0][k].ycor() > Placed_Blocks[0][j].ycor() - 20 :
									Moving_Block[0][1].goto(ownx,owny)
									return None
							
					else:
						for i in range(len(Placed_Blocks)):

							for j in range(4):
								j += 1

								for k in range(4):
									k += 1

									if Moving_Block[0][k].xcor() - 40 < Placed_Blocks[i-1][j].xcor() + 20 and Moving_Block[0][k].xcor() - 40 > Placed_Blocks[i-1][j].xcor() - 20 and Moving_Block[0][k].ycor() < Placed_Blocks[i-1][j].ycor() + 20 and Moving_Block[0][k].ycor() > Placed_Blocks[i-1][j].ycor() - 20 :
										Moving_Block[0][1].goto(ownx,owny)
										return

					Moving_Block[0][1].goto(ownx - 40,owny)
	SyncPos()

def key_right():


	owny = Moving_Block[0][1].ycor()
	ownx = Moving_Block[0][1].xcor()

	if Moving_Block[0][1].xcor() < 160:
		if Moving_Block[0][2].xcor() < 160:
			if Moving_Block[0][3].xcor() < 160:
				if Moving_Block[0][4].xcor() < 160:
					
					if len(Placed_Blocks) == 0:
						Moving_Block[0][1].goto(ownx + 40,owny)


					elif len(Placed_Blocks) == 1:
						for j in range(4):
							j += 1

							for k in range(4):
								k += 1

								if Moving_Block[0][k].xcor() + 40 < Placed_Blocks[0][j].xcor() + 20 and Moving_Block[0][k].xcor() + 40 > Placed_Blocks[0][j].xcor() - 20 and Moving_Block[0][k].ycor() < Placed_Blocks[0][j].ycor() + 20 and Moving_Block[0][k].ycor() > Placed_Blocks[0][j].ycor() - 20 :
									Moving_Block[0][1].goto(ownx,owny)
									return None
							
					else:
						for i in range(len(Placed_Blocks)):

							for j in range(4):
								j += 1

								for k in range(4):
									k += 1

									if Moving_Block[0][k].xcor() + 40 < Placed_Blocks[i-1][j].xcor() + 20 and Moving_Block[0][k].xcor() + 40 > Placed_Blocks[i-1][j].xcor() - 20 and Moving_Block[0][k].ycor() < Placed_Blocks[i-1][j].ycor() + 20 and Moving_Block[0][k].ycor() > Placed_Blocks[i-1][j].ycor() - 20 :
										Moving_Block[0][1].goto(ownx,owny)
										return

					Moving_Block[0][1].goto(ownx + 40,owny)
	SyncPos()
			
def hold():
	global Amount_Temp_Hold
	global showing
	
	if Amount_Temp_Hold == 0:
		if len(hold_block) == 0:
			hold_block.append(Moving_Block[0])
			Moving_Block.pop(0)
			GenNewBlock()
			Amount_Temp_Hold += 1
			

		else:
			Moving_Block.append(hold_block[0])
			hold_block.append(Moving_Block[0])
			hold_block.pop(0)
			Moving_Block.pop(0)
			Moving_Block[0][1].goto(0,350)
			Amount_Temp_Hold += 1
		showing = "Up"
		SyncPos()
	else:
		pass


# Listening for keypresses
wn.listen()
wn.onkeypress(Turn,"Up")
wn.onkeypress(key_down,"Down")
wn.onkeypress(key_left,"Left")
wn.onkeypress(key_right,"Right")
wn.onkeypress(hold,"space")

#4 Blöcke generieren
for i in range(4):
	GenNewBlock()

def RefDebug():
	print(debugarray)
	dgplaced = len(Placed_Blocks)
	debugarray[0] = dgplaced
	debugarray[1] = dgshowing
	debugarray[2] = len(hold_block)
	debugarray[3] = len(Moving_Block)
	debugarray[4] = len(Clearing_Blocks_Cache)




while True:

	while len(Moving_Block) == 1:
		
		
		#RefDebug()
		y = Moving_Block[0][1].ycor()
		x = Moving_Block[0][1].xcor()

		if timer == intervall:
			Moving_Block[0][1].sety(y-40)
			timer = 0
			SyncPos()
			


		
		timer += 1

		for i in range(len(Placed_Blocks)):
			for j in range(len(Placed_Blocks[i])-1):
				j += 1

				if ((Moving_Block[0][1].xcor() < (Placed_Blocks[i][j].xcor() + 20)) and (Moving_Block[0][1].xcor() > (Placed_Blocks[i][j].xcor() - 20)) and (Moving_Block[0][1].ycor() < (Placed_Blocks[i][j].ycor() + 60)) and (Moving_Block[0][1].ycor() > (Placed_Blocks[i][j].ycor() - 60))):
					Placed_Blocks.append(Moving_Block[0])
					Moving_Block.pop(0)
					GetNewBlock()
					pass
					break
						

				elif ((Moving_Block[0][2].xcor() < (Placed_Blocks[i][j].xcor() + 20)) and (Moving_Block[0][2].xcor() > (Placed_Blocks[i][j].xcor() - 20)) and (Moving_Block[0][2].ycor() < (Placed_Blocks[i][j].ycor() + 60)) and (Moving_Block[0][2].ycor() > (Placed_Blocks[i][j].ycor() - 60))):
					Placed_Blocks.append(Moving_Block[0])
					Moving_Block.pop(0)
					GetNewBlock()
					pass
					break

				elif ((Moving_Block[0][3].xcor() < (Placed_Blocks[i][j].xcor() + 20)) and (Moving_Block[0][3].xcor() > (Placed_Blocks[i][j].xcor() - 20)) and (Moving_Block[0][3].ycor() < (Placed_Blocks[i][j].ycor() + 60)) and (Moving_Block[0][3].ycor() > (Placed_Blocks[i][j].ycor() - 60))):
					Placed_Blocks.append(Moving_Block[0])
					Moving_Block.pop(0)
					GetNewBlock()
					pass
					break

				elif ((Moving_Block[0][4].xcor() < (Placed_Blocks[i][j].xcor() + 20)) and (Moving_Block[0][4].xcor() > (Placed_Blocks[i][j].xcor() - 20)) and (Moving_Block[0][4].ycor() < (Placed_Blocks[i][j].ycor() + 60)) and (Moving_Block[0][4].ycor() > (Placed_Blocks[i][j].ycor() - 60))):
					Placed_Blocks.append(Moving_Block[0])
					Moving_Block.pop(0)
					GetNewBlock()
					pass
					break

		if Moving_Block[0][1].ycor() < -360 or Moving_Block[0][2].ycor() < -360 or Moving_Block[0][3].ycor() < -360 or Moving_Block[0][4].ycor() < -360:
			Placed_Blocks.append(Moving_Block[0])
			Moving_Block.pop(0)
			GetNewBlock()
			SyncPos()
			
			break
		
		


		wn.update()
		sleep(0.001)

	if len(Moving_Block) == 0:
		GenNewBlock()
		Moving_Block.append(Comming_Blocks[0])
		Moving_Block[0][1].sety(350)
		Moving_Block[0][1].setx(0)
		Comming_Blocks.pop(0)
		showing = "Up"
		dgshowing = "Up"
		SyncPos()

# Made by Alex Bruksch / Sturm2002
# Somewhere beginning 2020 

		