#!/usr/bin/env python
# -*- coding: utf-8 -*-
store=5000
money=input('How much will you want to withdraw:')
balance=store-money
if balance<0:
	print u' 您的餘額不足!'
elif balance==0:
	print u' 您的存款無剩餘存款'
else:
	print u' 您的存款還剩%d元'%balance
f=open("ATM.txt","a")
f.write("餘額剩下:%d\n"%balance)

