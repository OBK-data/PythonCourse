import random
class Stock():
	def __init__(self, price, assetname):
		self.price = price
		self.assetname = assetname
class MutualFund():
	def __init__(self, fundname):
		self.fundname = fundname
class Portfolio():
	def __init__(self):
		self.cash = 0.0
		self.account = dict({'MONEY': float(0), 'STOCK': {}, 'M. FUNDS': {}}) #list for stocks
		self.funds = {} #list for funds
		self.histora = [] #list for transaction history
	def __repr__(self):
		return "You have %f dollars, %str stocks and %str bonds in your account. " % (self.account['MONEY'], self.account['STOCK'], self.account['M. FUNDS'])

	def addCash(self, input):
		self.account ['MONEY'] += input
		self.histora.append (("%f $ has been added.") % (input))
	def withdrawCash(self,input):
		self.account ['MONEY'] -= input
		self.histora.append (("%f $ has been withdrawn.") % (input))

	def buyStock(self, number, assetname):
		self.number= number
		self.account['STOCK'][Stock.assetname] += number
		self.withdrawCash(number * stock.price)
		self.histora.append (("You have bought %i %s stocks!") % (self.number, self.assetname))
	def sellStock(self, number, assetname):
		self.account['STOCK'][stock.assetname] -= number
		self.addCash(self.number * Stock.price * random.uniform(0.5, 1.5))
		self.histora.append (("You have sold %i %s stocks.") % (self.number, self.assetname))
	def buyMutualFund(self, share, fundname):
		self.account['M. FUNDS'][MutualFund.fundname] += share
		self.withdrawcash(share)
		self.histora.append (("You have bought %f percent of %s fund") % (self.share,self.fundname))
	def sellMutualFund(self, share, fundname):
		self.account['M. FUNDS'][MutualFund.fundname] -= share
		addcash(share * random.uniform(0.9, 1.2))
		self.histora.append (("You have sold %f percent of %s fund") % (self.share,self.fundname))

	def history(self):
		print("Your transaction history:")
		print(*self.histora, sep = "\n")

portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio

mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history()
