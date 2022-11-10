import pandas as pd


while True:
	print('(✿◠‿◠)')
	print("welcome to our store")
	print("press1-to see all our products")
	print("press2-to filter products")
	print("press3-to place an order")
	print("press4- to see our stats")
	print("press5-to see the order details")
	press = input('select the options from above\n')
#press2=input('select the above')
	if press=='1':
		df=pd.read_csv('Name21.csv')
		print(df)
		print('---------------------------------------------------------------------------------------------------------------------------------------')
	...
	if press=='3':
		   df=pd.read_csv('Name21.csv')
		   df1=pd.read_csv('NAME14.csv')
		   order=input('please provide the serial no. of product\n')
		   print(df[df['serialno']==order])
		   Name=input('please provide your name')
		   phoneno=input('please provide your phone number')
		   Address=input('please provide your address')
		   emailid=input('please provide your email address')
		   money='money to paid:-\n',(df.Price[df['serialno']==order])+100
		   print(money)
		   con=input('do you want to place order(y/n) ')
		   data=df1.fillna({'NAME':Name,'Phoneno':phoneno,'Address':Address,'emailid':emailid,'money':money,})
	#	   data2=df1.at['*',:] = [Name,phoneno,Address,emailid,money]
		   if con=='y':
		   	print('your order for\n',df.Name[df['serialno']==order],'\n','is being placed\n')
		   	print('please continue shopping  (｡◕‿◕｡)')
		   	print('---------------------------------------------------------------------------------------------------------------------------------------')
		   	print(quit)
		   ...
		   if con=='n':
		   	print('please continue shoping (｡◕‿◕｡)')
		   	print('---------------------------------------------------------------------------------------------------------------------------------------')
		   
	if press=='2':
	   	df=pd.read_csv('Name21.csv')
	   	filter1=input('select the prices range :\n00,000-10,000(a)\n10,000-20,000(b)\n20,000-30,000(c)\n30,000-50,000(d)\n50,000-flagship(e)\n')
	   	filter2=input('choose the brand:\nMi(x)\nSamsung(y)\nRealme(z)\nApple(k)\nRedmi(l)\n')
	   	
	   	if filter1=='a':
	   		print(df[df['Price']<=10000])
	   	...
	   	if filter1=='b':
	   		df=pd.read_csv('Name21.csv')
	   		print(df[(df['Price'] >= 10000) & (df['Price'] <= 20000)])
	   	...
	   	if filter1=='c':
	   	 	print(df[(df['Price'] >= 20000) & (df['Price'] <= 30000)])
	   	...
	   	if filter1=='d':
	   	 	print(df[(df['Price'] >= 30000) & (df['Price'] <= 50000)])
	   	 	
	   	...
	   	if filter1=='e':
	   	 	print(df[df['Price']>=50000])
	   	...
	   	if filter2=='x':
	   	 	print(df[df.BRAND=='Mi'])
	   	...
	   	if filter2=='y':
	   	 	print(df[df.BRAND=='Samsung'])
	   	...
	   	if filter2=='z':
	   	 	print(df[df.BRAND=='Realme'])
	   	...
	   	if filter2=='k':
	   	 	print(df[df.BRAND=='Apple'])
	   	... 
	   	if filter2=='l':
	   		print(df[df.BRAND=='Redmi'])
	   	...
	if press=='5':
	   df1=pd.read_csv('NAME14.csv')
	   print(data)
	   
	   
	 
	 
	 
	  
	  	
	  			
	   	
	   	


	   		   	   	
	   	