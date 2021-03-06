#!/usr/bin/python
import re
import cgi
import csv
import cgitb
cgitb.enable()

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage()
	username = form.getvalue("username1")
	inventory = []
	content = ""
	log = True
	
	with open ('LoggedIn.csv', 'r') as logd:
		users = []		
		for line in logd:
			line = line.strip()			
			users.append(line)
		if (username in users):
			log = True			
	
	if (log == True):
		if ((form.has_key("bbaby")) and (form["bbaby"].value !="") and (form.has_key("baby")) and (form["baby"].value !="")):
			baby = int(form.getvalue("bbaby"))
		else:
			baby = 0
		if ((form.has_key("bfirm")) and (form["bfirm"].value !="") and (form.has_key("firm")) and (form["firm"].value !="")):
			firm = int(form.getvalue("bfirm"))
		else:
			firm = 0
		if ((form.has_key("bfunny")) and (form["bfunny"].value !="") and (form.has_key("funny")) and (form["funny"].value !="")):
			funny = int(form.getvalue("bfunny"))
		else:
			funny = 0
		if ((form.has_key("bganja")) and (form["bganja"].value !="") and (form.has_key("ganja")) and (form["ganja"].value !="")):
			ganja = int(form.getvalue("bganja"))
		else:
			ganja = 0
		if ((form.has_key("bhuh")) and (form["bhuh"].value !="") and (form.has_key("huh")) and (form["huh"].value !="")):
			huh = int(form.getvalue("bhuh"))
		else:
			huh = 0
		if ((form.has_key("bpointer")) and (form["bpointer"].value !="") and (form.has_key("pointer")) and (form["pointer"].value !="")):
			pointer = int(form.getvalue("bpointer"))
		else:
			pointer = 0
		if ((form.has_key("brasta")) and (form["brasta"].value !="") and (form.has_key("rasta")) and (form["rasta"].value !="")):
			rasta = int(form.getvalue("brasta"))
		else:
			rasta = 0
		if ((form.has_key("bskeptic")) and (form["bskeptic"].value !="") and (form.has_key("skeptic")) and (form["skeptic"].value !="")):
			skeptic = int(form.getvalue("bskeptic"))
		else:
			skeptic = 0
		if ((form.has_key("bwave")) and (form["bwave"].value !="") and (form.has_key("wave")) and (form["wave"].value !="")):
			wave = int(form.getvalue("bwave"))
		else:
			wave = 0	

		with open ('Inventory.csv', 'r') as f:	
			for line in f:
				line = (line.split(","))
				inventory.append(int(line[1]))

			if ((inventory[0]-(baby))>=0)and((inventory[1]-(firm))>=0)and((inventory[2]-(funny))>=0)and((inventory[3]-(ganja))>=0)and((inventory[4]-(huh))>=0)and((inventory[5]-(pointer))>=0)and((inventory[6]-(rasta))>=0)and((inventory[7]-(skeptic))>=0)and((inventory[8]-(wave))>=0):
				line1 = 'baby,'+str(inventory[0]-(baby))+',20\n'
				line2 = 'firm,'+str(inventory[1]-(firm))+',20\n'
				line3 = 'funny,'+str(inventory[2]-(funny))+',20\n'
				line4 = 'ganja,'+str(inventory[3]-(ganja))+',20\n'
				line5 = 'huh,'+str(inventory[4]-(huh))+',20\n'
				line6 = 'pointer,'+str(inventory[5]-(pointer))+',20\n'
				line7 = 'rasta,'+str(inventory[6]-(rasta))+',20\n'
				line8 = 'skeptic,'+str(inventory[7]-(skeptic))+',20\n'
				line9 = 'wave,'+str(inventory[8]-(wave))+',20\n'

				content = line1+line2+line3+line4+line5+line6+line7+line8+line9
		
				with open ('Inventory.csv', 'w') as wf:
					wf.write(content)
				wf.close
				print "<html>"
				print"	<head><title>Barack Pics - Bill</title></head>"
				print "	<body>"
				print "  <p>"
				print "  <b>BILL</b><br>"
				print "  ============================<br>"
				print "	 B-Baby " + str(baby) + "  = $" + str(20*(baby)) + "<br>"
				print "  B Firm " + str(firm) + " = $" + str(20*(firm))+ "<br>"
				print "	 B Funny " + str(funny) + "  = $" + str(20*(funny)) + "<br>"
				print "  B Ganja? " + str(ganja) + " = $" + str(20*(ganja))+ "<br>"
				print "	 Huh? " + str(huh) + "  = $" + str(20*(huh)) + "<br>"
				print "  2 the Point " + str(pointer) + " = $" + str(20*(pointer))+ "<br>"
				print "	 BaRast Obama " + str(rasta) + "  = $" + str(20*(rasta)) + "<br>"
				print "  B Skeptical " + str(skeptic) + " = $" + str(20*(skeptic))+ "<br>"
				print "	 Good Bye! " + str(wave) + "  = $" + str(20*(wave)) + "<br>"
				print "  ============================<br>"
				print "  <b>TOTAL : $" + str( (20*(baby)) + (20*(firm)) + (20*(funny)) + (20*(ganja)) + (20*(huh)) + (20*(pointer)) + (20*(rasta)) + (20*(skeptic)) + (20*(wave)) )+ " CND</b><br>" 
				print "  THANK YOU FOR YOUR PURCHASE"
				print "  Login again if you want to place another order.<br>"
				print "  </p>"
				print "  To go back to Home page : " + '<a href="index.html">Home</a><br>'
				print "  To go back to Login page : " + '<a href="login.html" target="_blank">Login</a><br>'
				print " </body>"
				print "</html>"
			else:	
				print "<html>"
				print " <head><title>Error</title></head>"
				print " <body>"
				print "  <p>"
				print "  Our apologies. It seems we're out of inventory.<br>"
				print "  You have been logged out.<br>"
				print "  Please login again in order to place an order<br>"
				print "  To go back to Home page : " + '<a href="index.html">Home</a><br>'
				print "  To go back to Login page : " + '<a href="login.html">Login</a><br>'
				print "  </p>"
				print " </body>"
				print "</html>"
		f.close()	
	
	else:
		print "<html>"
		print " <head><title>Error</title></head>"
		print " <body>"
		print "  <p>"
		print "  Please login if you wish to buy stuff.<br>"
		print "  If you have not yet registered, please do so. <br>"
		print "  Main : " + '<a href="index.html">Home</a><br>'
		print "  To Login : " + '<a href="login.html">Login</a><br>'
		print "  To Register : " + '<a href="registration.html">Register</a><br>'
		print " </body>"
		print "</html>"
	
main()

