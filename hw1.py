import random  #found it on the Internet
stockrandom = random.uniform(0.5, 1.5)#made them easier to apply
fundrandom = random.uniform(0.9, 1.2)
class Stock():
	def __init__(self, price, assetname):
		self.price = price
		self.assetname = assetname
class MutualFund():
	def __init__(self, fundname):
		self.fundname = fundname

class Portfolio(Stock):
	def __init__(self):
		self.account = dict({'MONEY': float(0), 'STOCK': {}, 'M. FUNDS': {}}) #dictionary for all of the assets (school exercise)
		self.histora = [] #list for transaction history
	def __repr__(self):
		return "You have %f dollars, %s stocks and %s bonds in your account. " % (self.account['MONEY'], self.account['STOCK'], self.account['M. FUNDS'])

	def addCash(self, input): #adds cash
		self.account ['MONEY'] += input
		self.histora.append (("%f $ has been added.") % (input))
	def withdrawCash(self,input): #withdraws cash
		if self.account ['MONEY'] < input:
		   print("Insufficient Funds")
		else:
		   self.account ['MONEY'] -= input
		   self.histora.append (("%f $ has been withdrawn.") % (input))

	def buyStock(self, number, Stock):
		self.number = number
		global pricee #made price variable easier to use
		pricee = Stock.price
		if self.account ['MONEY'] < number*pricee: #prevents overbuying
			print("Insufficient Funds")
		elif Stock.assetname in self.account['STOCK']: #checks whether the stock exists in the account
			self.account['STOCK'][Stock.assetname] += number
			self.histora.append (("You have bought additional %i %s stocks!") % (self.number, Stock.assetname))

		else:
			self.account['STOCK'][Stock.assetname] = number #adds stock
			self.withdrawCash(number * pricee)
			self.histora.append (("You have bought %i %s stocks!") % (self.number, Stock.assetname))
	def sellStock(self,assetname ,number ):
		self.addCash(self.number * pricee * stockrandom )
		self.histora.append (("You have sold %i %s stocks.") % (self.number, assetname))
		if self.account['STOCK'][assetname]== number: #removes stock if it's number hits zero.
			del self.account['STOCK'][assetname]
		else:
			self.account['STOCK'][assetname] -= number #sells stock

	def buyMutualFund(self, share, MutualFund):
		self.share = share
		if share > self.account ['MONEY']:
			print("Insufficient funds")
		elif MutualFund.fundname in self.account['M. FUNDS']: #checks whether the fund already exists in the account
			self.account['M. FUNDS'][MutualFund.fundname] += float(share)
			self.histora.append (("You have bought additional %f percent of %s fund") % (self.share,MutualFund.fundname))
		else:
			self.account['M. FUNDS'][MutualFund.fundname] = float(share) #buys funds
			self.withdrawCash(share)
			self.histora.append (("You have bought %f percent of %s fund") % (self.share,MutualFund.fundname))
	def sellMutualFund(self, fundname, share):
		self.addCash(share * fundrandom)
		self.histora.append (("You have sold %f percent of %s fund") % (self.share, fundname))
		if share == self.account['M. FUNDS'][fundname]: #deletes the funds when shares hit zero
			del self.account['M. FUNDS'][fundname]
		else:
		    self.account['M. FUNDS'][fundname] -=  share #removes some of the shares

	def history(self): #provides transaction history
		print("Your transaction history:")
		print(*self.histora, sep = "\n")

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
