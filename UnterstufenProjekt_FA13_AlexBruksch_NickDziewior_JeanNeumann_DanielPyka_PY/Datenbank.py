import os
from sqlite3.dbapi2 import connect
from typing import Collection, DefaultDict
from globalVars import ProtypeDBPath
from tkinter import *
import sqlite3

GlobalDBPath = ProtypeDBPath
GlobalUsername = ""

def connection():


	#Es gibt nur noch eine Datenbank, welche alle Infos beinhaltet
	conn = sqlite3.connect(GlobalDBPath)

	c = conn.cursor()

	#Tabelle nur mit user creds 
	c.execute("""CREATE TABLE IF NOT EXISTS user_info ( 
			
			usern TEXT,
			passw TEXT,
			email TEXT
			

			)""")
	#Tabelle generelle game Infos mit zugehörigen user

	c.execute("""CREATE TABLE IF NOT EXISTS user_game_info ( 
			
			round INTEGER,
			wins INTEGER,
			loses INTEGER,
			rating INTEGER, 
			difficulty INTEGER,
			moves TEXT,
			usern TEXT, 
			FOREIGN KEY (usern)
			REFERENCES user_info (usern) 
				ON UPDATE CASCADE 
				ON DELETE CASCADE 
			
			)""")



	#Infos über und für die KI

	c.execute("""CREATE TABLE IF NOT EXISTS ki_info ( 
			
			round_ki INTEGER,
			rating_ki INTEGER,
			difficulty_ki INTEGER,
			moves_ki TEXT, 
			usern TEXT, 
			FOREIGN KEY (usern)
			REFERENCES user_info (usern) 
				ON UPDATE CASCADE 
				ON DELETE CASCADE 
		
			)""")
	conn.commit()
	conn.close()

	#global username
	user = ""

	

def CheckCredentialsDB(UserName, Password,LoginOrReg):
	
	#global user 
	user = UserName
	FoundUserName = False
	# If LoginOrReg == True  # Login
	# If LoginOrReg == False # Register
	conn = sqlite3.connect(GlobalDBPath)

	c = conn.cursor()
	c.execute("SELECT usern, passw FROM user_info")
	#in Python müssen Daten von Abfragen der Datenbank in Variablen gespeichert werden 
	records = c.fetchall()
	
	
	if LoginOrReg == False:
		for record in records:
			if records is None or len(records) == 0:
				c.execute(f"INSERT INTO user_info (usern, passw) VALUES (?,?)",(user,Password))
				c.execute(f"INSERT INTO user_game_info (rating, moves, wins, loses,difficulty, round, usern) VALUES (0,0,0,0,0,0,?)", [user])
				c.execute(f"INSERT INTO ki_info (rating_ki, moves_ki,difficulty_ki,round_ki, usern) VALUES (0,0,0,0,?)", [user])							
				conn.commit()
				conn.close()
				return True  
			else:
				if record[0] != user:
					pass
					
				else:
					FoundUserName = True
					break
		if FoundUserName == False:
			c.execute("INSERT INTO user_info (usern, passw) VALUES (?,?)",(user,Password))
			c.execute(f"INSERT INTO user_game_info (rating, moves, wins,loses,difficulty,round, usern) VALUES (0,0,0,0,0,0,?)", [user])
			c.execute(f"INSERT INTO ki_info (rating_ki, moves_ki,difficulty_ki,round_ki, usern) VALUES (0,0,0,0,?)", [user])							
			conn.commit()
			conn.close()
			return True
		else:
			conn.close()
			return False
						
	else:
		for record in records:
			
			if record[0] == user and record[1] == Password:
					
					conn.commit()
					conn.close()
					break
					 
		else:
			conn.close()
			return False
		return True
	#conn.close()


# was für daten wir brauchen bzw du bekommst kannst du in MAINGUI.py Zeile 424 - 430 sehen
def winOrDefeat(user,winOrDefeat, rating=0, rating_ki=0, moves=0, moves_ki=0, difficulty=0, difficulty_ki=0):
	 
	#Es wird zu jedem Eintrag (ob win oder defeat) der UserName eingefügt, damit anschließend alle Abfragen über den User laufen. -> doppelte und dreifache gleiche user
	# If winOrDefeat == True  # win
	# If winOrDefeat == False # defeat

	# If win_kiOrDefeat_ki == True  # win
	# If win_kiOrDefeat_ki == False # defeat
	
	conn = sqlite3.connect(GlobalDBPath)
	c = conn.cursor()
	
	if user != "" and user != None:
			if winOrDefeat == True: # warum 2 argumente 1 für win und 1 für defeat ? warum nicht einfach nur eins was true oder false ist ?
					c.execute(f"SELECT COALESCE(SUM(wins), 0) FROM user_game_info WHERE usern = (?)", [user])
					wins = c.fetchone()
					res = int(''.join(map(str, wins)))
					res += 1
					c.execute(f"SELECT COALESCE(SUM(rating), 0) FROM user_game_info WHERE usern = (?)", [user])
					total12 = c.fetchone()
					res2 = int(''.join(map(str, total12)))
					res2 += rating
					                   
					c.execute(f"SELECT COALESCE(SUM(moves), 0) FROM user_game_info WHERE usern = (?)", [user])
					total13 = c.fetchone()
					res3 = int(''.join(map(str, total13)))
					res3 += moves

					c.execute(f"SELECT COALESCE(SUM(round), 0) FROM user_game_info WHERE usern = (?)", [user])
					total14 = c.fetchone()
					res4 = int(''.join(map(str, total14)))
					res4 += 1
                   

					c.execute(f"UPDATE user_game_info SET wins = (?), rating = (?), moves = (?), round = (?) WHERE usern = (?)", (res,res2,res3,res4,user))
					conn.commit()
					return True 
			elif winOrDefeat == False:
					c.execute(f"SELECT COALESCE(SUM(loses), 0) FROM user_game_info WHERE usern = (?)", [user])
					loses = c.fetchone()
					res = int(''.join(map(str, loses)))
					res += 1
					c.execute(f"SELECT COALESCE(SUM(moves), 0) FROM user_game_info WHERE usern = (?)", [user])
					total13 = c.fetchone()
					res3 = int(''.join(map(str, total13)))
					res3 += moves_ki
					c.execute(f"SELECT COALESCE(SUM(round), 0) FROM user_game_info WHERE usern = (?)", [user])
					total14 = c.fetchone()
					res4 = int(''.join(map(str, total14)))
					res4 += 1
					c.execute(f"SELECT COALESCE(SUM(rating), 0) FROM user_game_info WHERE usern = (?)", [user])
					totals4 = c.fetchone()
					res2 = int(''.join(map(str, totals4)))
					if res2 == 0:
						c.execute(f"UPDATE user_game_info SET loses = (?), rating = (?), moves = (?), round = (?) WHERE usern = (?)", (res,res2,res3,res4,user))
					elif res2 + rating <= 0:
						c.execute(f"UPDATE user_game_info SET rating = 0 WHERE usern = (?)", [user])
					else:
						res2 += rating
					

					c.execute(f"UPDATE user_game_info SET loses = (?), rating = (?), moves = (?), round = (?) WHERE usern = (?)", (res,res2,res3,res4,user))
					

					
					conn.commit()
					return True
			conn.commit()
			conn.close()

			conn = sqlite3.connect(GlobalDBPath)
			c = conn.cursor()
			if winOrDefeat == True:
					c.execute(f"SELECT COALESCE(SUM(rating_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total12 = c.fetchone()
					res2 = int(''.join(map(str, total12)))
					res2 += rating
					c.execute(f"SELECT COALESCE(SUM(moves_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total13 = c.fetchone()
					res3 = int(''.join(map(str, total13)))
					res3 += moves
					c.execute(f"SELECT COALESCE(SUM(round_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total14 = c.fetchone()
					res4 = int(''.join(map(str, total14)))
					res4 += 1
                   

					c.execute(f"UPDATE ki_info SET rating_ki = (?), moves_ki = (?), round_ki = (?) WHERE usern = (?)", (res2,res3,res4,user))
					conn.commit()
					return True 
			elif winOrDefeat == False:
					c.execute(f"SELECT COALESCE(SUM(rating_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total12 = c.fetchone()
					res2 = int(''.join(map(str, total12)))
					res2 += rating
					c.execute(f"SELECT COALESCE(SUM(moves_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total13 = c.fetchone()
					res3 = int(''.join(map(str, total13)))
					res3 += moves
					c.execute(f"SELECT COALESCE(SUM(round_ki), 0) FROM ki_info WHERE usern = (?)", [user])
					total14 = c.fetchone()
					res4 = int(''.join(map(str, total14)))
					res4 += 1
                   

					c.execute(f"UPDATE ki_info SET rating_ki = (?), moves_ki = (?), round_ki = (?) WHERE usern = (?)", (res2,res3,res4,user))
					conn.commit()
					return True 
	else:
			return False
	conn.commit()
	conn.close()
	

	
	

def stats(user):
	OutArr = []
	
	
	if user:
			conn = sqlite3.connect(GlobalDBPath)
			c = conn.cursor()
			#select oid 
			
			#inner join???
			c.execute(f"SELECT COALESCE(SUM(wins), 0), COALESCE(SUM(loses), 0), COALESCE(SUM(round), 0) FROM user_game_info WHERE usern = (?)", [user])
			records = c.fetchone()
			
			OutArr.append(records[0])
			OutArr.append(records[1])
			OutArr.append(records[2])
			
			
			#summierte Ausgabe
			
			c.execute(f"SELECT COALESCE(SUM(rating), 0) FROM user_game_info WHERE usern = (?)", [user])
			totals3 = c.fetchall()
			
			for total3 in totals3:
					OutArr.append(total3[0])
			
			c.execute(f"SELECT COALESCE(SUM(moves), 0) FROM user_game_info WHERE usern = (?)", [user])
			totals5 = c.fetchall()
			
			for total5 in totals5:
					OutArr.append(total5[0])

			

			
			#ki.db
			conn = sqlite3.connect(GlobalDBPath)
			c = conn.cursor()
			
			c.execute(f"SELECT moves_ki FROM ki_info WHERE usern = (?)", [user])
			records_ki = c.fetchone()
			
			OutArr.append(records_ki[0])
			
			c.execute("SELECT usern, rating FROM user_game_info ORDER BY rating DESC")
			leader = c.fetchall()
			OutArr.append(leader)

			
			
			
			

			if OutArr != None:
				return OutArr
			

			conn.commit()
			conn.close()
	elif not user:
		return False


if __name__ == "__main__":
	connection()
	CheckCredentialsDB("test", 1223, True)
	winOrDefeat("test",True,20,30,10,10,7,3)
	stats("test")