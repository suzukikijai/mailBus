# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""



#system functions
import cgi, cgitb 
from datetime import datetime 

#user functions
from hashingFunction import hasher




#input values from response form
def importForm(genTime):
	viff = dict();
	# form = cgi.FieldStorage() # Create instance of FieldStorage 
	# viff['emailID']  = form.getvalue('emailIDs')
	# viff['username']  = form.getvalue('username')
	# viff['time'] = genTime.strftime('%Y-%m-%d %H:%M:%S')
	# viff['formGenTime'] = genTime.strftime('%Y-%m-%d %H:%M:%S::%f')
	# viff['formID'] = hasher(formGenTime)
	###############tempMOCKER###############
	viff['emailID']  = "asdasd"
	viff['username']  = "asdasd"
	viff['accessedTime'] = genTime.strftime('%Y-%m-%d %H:%M:%S')
	formGenTime = genTime.strftime('%Y-%m-%d %H:%M:%S::%f')
	viff['formID'] = hasher(formGenTime)
	return(viff)
 
def tokenizer(saltedEmailID,saltedUsername,formID):
    tokGen = dict();
    rawtoken = str(saltedEmailID)+str(saltedUsername)
    tokenInit = hasher(rawtoken)+str(formID)
    temptoken = str(tokenInit)+str(formID)
    tokGen['tokenID'] = temptoken
    return(tokGen)
