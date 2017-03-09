Class Bank_Accont(object)
 def 


 class Bank_Account(object):
  def _init_(self,name,account_number,balance):
    balance=0
   
     self.name=name
    self.account_number=account_number
    self.balance=balance
    def balance(self):
      return self.balance
    
    def deposit(self,amount):
      if amount<=0:
       print ("invalid amount")
    else:
      self.balance+=amount
      
    def withdraw(self,amount):
      if amount>self.balance: 
        return "withdrawal amount exceeds the balance"
      elif amount<=0:
        return invalid
      elif amount-self.balnce<500:
        return insufficient funds
      else:
        return self.balance-=amount-self
        