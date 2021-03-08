import random  #found it from internet
stockrandom = random.uniform(0.5, 1.5)#made them easier to apply
fundrandom = random.uniform(0.9, 1.2)
class Stock():
	def __init__(self, price, assetname):
		self.price = price
		self.assetname = assetname
class MutualFund():
	def __init__(self, fundname):
		self.fundname = fundname

class Portfolio():
	def __init__(self):
		self.account = dict({'MONEY': float(0), 'STOCK': {}, 'M. FUNDS': {}}) #dictionary for all of the assets (school exercise)
		self.histora = [] #list for transaction history
	def __repr__(self):
		return "You have %f dollars, %s stocks and %s bonds in your account. " % (self.account['MONEY'], self.account['STOCK'], self.account['M. FUNDS'])

	def addCash(self, input):
		self.account ['MONEY'] += input
		self.histora.append (("%f $ has been added.") % (input))
	def withdrawCash(self,input):
		if self.account ['MONEY'] < input:
		   print("Insufficient Funds")
		else:
		   self.account ['MONEY'] -= input
		   self.histora.append (("%f $ has been withdrawn.") % (input))

	def buyStock(self, number, Stock):
		self.number = number
		if self.account ['MONEY'] < number*Stock.price:
			print("Insufficient Funds")
		else:
			self.account['STOCK'][Stock.assetname] = int(number)
			self.withdrawCash(number * Stock.price)
			self.histora.append (("You have bought %i %s stocks!") % (self.number, Stock.assetname))
	def sellStock(self,Stock ,number ):
		self.addCash(self.number * Stock.price * stockrandom )
		self.histora.append (("You have sold %i %s stocks.") % (self.number, Stock.assetname))
		if self.account['STOCK'][Stock.assetname]== number:
			del self.account['STOCK'][Stock.assetname]
		else:
			self.account['STOCK'][Stock.assetname] -= number

	def buyMutualFund(self, share, MutualFund):
		self.share = share
		if share > self.account ['MONEY']:
			print("Insufficient funds")
		else:
			self.account['M. FUNDS'][MutualFund.fundname] = share
			self.withdrawCash(share)
			self.histora.append (("You have bought %f percent of %s fund") % (self.share,MutualFund.fundname))
	def sellMutualFund(self, MutualFund, share):
		self.addCash(share * fundrandom)
		self.histora.append (("You have sold %f percent of %s fund") % (self.share, MutualFund.fundname))
		if share == self.account['M. FUNDS'][MutualFund.fundname]:
			del self.account['M. FUNDS'][MutualFund.fundname]
		else:
		    self.account['M. FUNDS'][MutualFund.fundname] -=  share

	def history(self):
		print("Your transaction history:")
		print(*self.histora, sep = "\n")

#Unfortunately, I couldn't make sales work. I couln't find a way to replace mf3 and s with BRT and HFH.

portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50) #Removes $50
print(portfolio)
portfolio.history()
