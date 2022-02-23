class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0

  def update_ledger(self, amount, description):
    self.ledger.append({"amount": format(amount,'.2f'), "description": description})
    
  def deposit(self, amount, description=''):
    self.balance += amount
    self.update_ledger(amount,description)

  def withdraw(self, amount, description=''):
    if self.check_funds(amount): 
      self.balance -= amount
      self.update_ledger(-amount,description)
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, Category):
    if self.withdraw(amount, "Transfer to " + Category.category):
      Category.deposit(amount,"Transfer from " + self.category)
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def __str__(self):
    total_asterik = 30 - len(self.category)
    statement = ''
  
    for num in range(total_asterik):
      if num == (total_asterik//2):
        statement = statement + self.category + '*'
      else:
        statement = statement +  '*'
      
    for row in self.ledger:
      desc_col_len = 23 - len(row['description'])
      amt_col_len  = 7 - len(str(row['amount']))
      statement = statement + '\n'+ row['description'][:23] +  (" " * desc_col_len) + (" " * amt_col_len) + str(row['amount'])
    statement = statement +  '\n' +  "Total:" + str(self.balance) + '\n'

    return statement
    
def create_spend_chart(categories):
  pass