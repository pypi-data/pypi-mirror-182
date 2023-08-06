# from Stock_main import *
# from User import *

from main_package.Stock_main import *
from main_package.Buy import *
from sub_package.User import *
from sub_package.bot import *
from sub_package.endgame import *


Stock1 = Stock()
U1 = User(Stock1)
U1.process()

U2 = bot(Stock1)
U2.process()

player_1_status = [U1.get_expense_list(), U1.get_price_of_stock_buy_list(), U1.get_volume()]
dobby_2_status = [U2.get_expense_list(), U2.get_price_of_stock_buy_list(), U2.get_volume()]
stock_list = [Stock1.get_high_price(), Stock1.get_low_price(), Stock1.get_size()]
# print(player_1_status, '\n', dobby_2_status, '\n', stock_list)

# Execute end game 

# Add cashback amount to totals
(cb1, cb2) = cashback(player_1_status, dobby_2_status)
dobby_2_status.append(cb2)
player_1_status.append(cb1)
#Final value
dobby_final_value = final_price(dobby_2_status, stock_list)
dobby_2_status.append(dobby_final_value)
# print(dobby_final_value)
player_final_value = final_price(player_1_status, stock_list)
player_1_status.append(player_final_value)

# create a dataframe for player 1

headers = ['Totalexpense','Buyprice','Buyvol','Cashback','Sellprice']
pd1 = pd.DataFrame(player_1_status, headers)
pd1.index.name = 'Round'
pd1 = pd1.T
pd1['Sellvalue'] = pd1.Buyvol * pd1.Sellprice
pd1['GainLoss'] = pd1.Sellvalue + pd1.Cashback - pd1.Totalexpense
pd1.index = np.arange(1, len(pd1) + 1) # set index of dataframe sarting from 1
pd1.loc['Column_Total']= pd1.sum(numeric_only=True, axis=0)



# create a dataframe for player 2
headers = ['Totalexpense','Buyprice','Buyvol','Cashback','Sellprice']
pd2 = pd.DataFrame(dobby_2_status, headers)
pd2.index.name = 'Round'
pd2 = pd2.T

pd2['Sellvalue'] = pd2.Buyvol * pd2.Sellprice
pd2['GainLoss'] = pd2.Sellvalue + pd2.Cashback - pd2.Totalexpense
pd2.index = np.arange(1, len(pd2) + 1) # set index of dataframe sarting from 1
pd2.loc['Column_Total']= pd2.sum(numeric_only=True, axis=0)



# print the final result
print("\n------Final Result------\n")
print("Player")
print(pd1)
print("\nDobby")
print(pd2)


player_score = pd1.loc['Column_Total']['GainLoss']
dobby_score = pd2.loc['Column_Total']['GainLoss']
if dobby_score > player_score:
      print("The winner is: DOBBY!!!")
else:
      print("The winner is: YOU!!!")