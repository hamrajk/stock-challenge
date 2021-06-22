#Stockmarketchallenge

'''
Welcome to Forma.ai stock statement generator! In this problem, you will be coding up a transaction
statement generator for a existing trader on our stock trading system. The inputs are provided below, and
the exact output you are to generate is provided after the inputs.

actions: the timestamped actions that the stock trader performed, it can be BUY or SELL type, and they can
buy or sell a few different stocks. However, you should assume that the number of ticker is not limited to
3 types as in the example below, but potentially infinite, so the ticker should not be hardcoded anywhere.

stock_actions: the timestamped actions that the stock performed regardless of who the trader is. It includes
stock splits, and dividend payouts. Even though these actions are not performed by our trader, it still affects
our trader's portfolios, so it should be recorded in the statement that we prepare.

We are looking for easy to understand/extend program that doesn't perform any unnecessary actions.

Feel free to extend the test cases to include new ones that exercises your program to the fullest.
'''

# input

actions = [{'date': '1992/07/14 11:12:30', 'action': 'BUY', 'price': '12.3', 'ticker': 'AAPL', 'shares': '500'}, {'date': '1992/09/13 11:15:20', 'action': 'SELL', 'price': '15.3', 'ticker': 'AAPL', 'shares': '100'}, {'date': '1992/10/14 15:14:20', 'action': 'BUY', 'price': '20', 'ticker': 'MSFT', 'shares': '300'}, {'date': '1992/10/17 16:14:30', 'action': 'SELL', 'price': '20.2', 'ticker': 'MSFT', 'shares': '200'}, {'date': '1992/10/19 15:14:20', 'action': 'BUY', 'price': '21', 'ticker': 'MSFT', 'shares': '500'}, {'date': '1992/10/23 16:14:30', 'action': 'SELL', 'price': '18.2', 'ticker': 'MSFT', 'shares': '600'}, {'date': '1992/10/25 10:15:20', 'action': 'SELL', 'price': '20.3', 'ticker': 'AAPL', 'shares': '300'}, {'date': '1992/10/25 16:12:10', 'action': 'BUY', 'price': '18.3', 'ticker': 'MSFT', 'shares': '500'}]
stock_actions = [{'date': '1992/08/14', 'dividend': '0.10', 'split': '', 'stock': 'AAPL'}, {'date': '1992/09/01', 'dividend': '', 'split': '3', 'stock': 'AAPL'}, {'date': '1992/10/15', 'dividend': '0.20', 'split': '', 'stock': 'MSFT'},{'date': '1992/10/16', 'dividend': '0.20', 'split': '', 'stock': 'ABC'}]


#Sample Output

"""
On 1992-07-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $0 of dividend income
  Transactions:
    - You bought 500 shares of AAPL at a price of $12.30 per share
On 1992-08-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL paid out $0.10 dividend per share, and you have 500 shares
On 1992-09-01, you have:
    - 1500 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL split 3 to 1, and you have 1500 shares
On 1992-09-13, you have:
    - 1400 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - You sold 100 shares of AAPL at a price of $15.30 per share for a profit of $1120.00
 """

#Convert the date formats in each list of dictionaries so they are the same and can be added
#also add 'type' keys to format what kind of action it is


from datetime import datetime


for dictionary in stock_actions:
	date_string = dictionary['date']
	date_object = datetime.strptime(date_string, '%Y/%m/%d')
	dictionary['date'] = str(date_object)
	dictionary['type'] = "stock_action"



for dictionary in actions:
	date_string = dictionary['date']
	date_object = datetime.strptime(date_string, '%Y/%m/%d %H:%M:%S')
	dictionary['date'] = str(date_object)
	dictionary['type'] = "action"


all_actions = stock_actions + actions


#Organize the all_actions list by date
for dictionary in all_actions:
		all_actions.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))



#initial filler values for owned stocks and current date
owned_stocks = [{'ticker':"filler"}]
current_date = "blank"
owned = False #used a few times to ensure the stock is actually owned before performing an operation with it
total_dividend = 0 #keeping track of total divident for output
profit = 0 #for profit output statements when selling


for record in all_actions:
	if current_date != record['date'][0:10]: #This is for displaying the date headings
		current_date = record['date'][0:10]
		print("On " + current_date + ", you have:")

		#All the buy actions
		if record['type'] == "action" and record['action'] == "BUY":
			for my_record in owned_stocks:
				if my_record['ticker'] != record['ticker']:
					owned = False
				else:
					owned = True
					break

		
		if record['type'] == "action" and record['action'] == "BUY":			
			if owned == False:
				new_entry = {'ticker': record['ticker'], "shares": float(record['shares']), "avgprice": float(record['price']), "buy_count": 1, "dividend": float(0)}
				owned_stocks.append(new_entry)
								
			else:
				my_record["buy_count"] += 1
				my_record["avgprice"] = ((my_record["avgprice"] * my_record["shares"]) + (float(record["price"])) * float(record["shares"]))
				my_record["shares"] += float(record["shares"])
				my_record["avgprice"] /= my_record["shares"]
				

				

		#All the sell actions
		if record['type'] == "action" and record['action'] == "SELL":
			for my_record in owned_stocks:
				if my_record['ticker'] == record['ticker']:	
					my_record["shares"] -= float(record["shares"])	
					if my_record['shares'] == 0:
						owned_stocks.remove(my_record) #this is to remove a stock if we own 0 shares of it


		#Stock actions, assuming dividents and stock splits cannot occur on the same day
		if record['type'] == "stock_action":
			for my_record in owned_stocks:
				if my_record['ticker'] != record['stock']:
					pass
				elif my_record['ticker'] == record['stock']:	
					if record['dividend'] != '':
						my_record['dividend'] = my_record['dividend'] + float(record['dividend']) * float(my_record["shares"])
						total_dividend += my_record['dividend']
					if record['split'] != '':
						my_record['shares'] *= float(record['split'])
						my_record['avgprice'] /= float(record['split'])


		#display the results
		for my_record in owned_stocks:
			if my_record['ticker'] == 'filler':
				pass
			else:
				print("\t- " + str(my_record['shares']) + " shares of " + my_record['ticker'] + " at $" + "{:.2f}".format(my_record["avgprice"]) + " per share.")
				

		print("\t- $" + str(total_dividend) + " of divident income")



		#logic for displaying results
		print("    Transactions:")
		if record['type'] == "action" and record['action'] == "BUY":
			print("\t- You bought " + str(record['shares']) + " shares of " + str(record['ticker']) + " at a price of $" + str(record['price']) + " per share.")
		if record['type'] == "action" and record['action'] == "SELL":
			profit = float(record["shares"]) * float(record["price"]) - float(record["shares"]) * float(my_record["avgprice"])  
			print("\t- You sold " + str(record['shares']) + " shares of " + str(record['ticker']) + " at a price of $" + str(record['price']) + " per share for a profit of $" + str(profit))
		if record['type'] == "stock_action" and record['dividend'] != '':
				for my_record in owned_stocks:
					if my_record['ticker'] != record['stock']:
						owned = False
					else:
						owned = True
						break
				if owned == True:
					print("\t- " + str(record['stock']) + " paid out $" + str(record['dividend']) + " per share, and you have " + str(my_record["shares"]) + " shares.")

		if record['type'] == "stock_action" and record['split'] != '':
				for my_record in owned_stocks:
					if my_record['ticker'] != record['stock']:
						owned = False
					else:
						owned = True
						break
				if owned == True:
					print("\t- " + str(record['stock']) + " split " + str(record['split']) + " to 1, and you have " + str(my_record['shares']) + "shares.")










#     	