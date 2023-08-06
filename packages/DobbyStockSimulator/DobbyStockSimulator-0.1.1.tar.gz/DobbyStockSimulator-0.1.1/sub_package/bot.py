
from main_package.Stock_main import *
import numpy as np


class bot(Stock):
      def __init__(self, Stock):
            self.stock = Stock
            self.len_range = int(self.stock.n)
            self.balance = 10000  # initial balance
            self.info = {'price_of_stock_buy': [],
                        'expense': [],
                        'volume_list': [],
                        'total_price_of_stock_by_each_process': 0,
                        'total_stock_price_list': [],
                        'result_list': []}

      def print_stock_info(self, high, low, vol):
            print("|The high price of stock is {} {}".format(high, '\t|'))
            print("|The low price of stock is {} {}".format(low, '\t\t|'))
            print("|The volume of stock is {} {}".format(vol, '\t\t|'))

      def buy_stock_rp(self, high_price, low_price, vol=0):
            high_price_ = high_price
            low_price_ = low_price
            vol_ = vol
            total_price = 0
            buy_volume = 0
            random_price = float(random.randint(int(low_price_), int(high_price_)))

            info = []
            buy_price = float(random_price)
            if vol_ > 0:
                  buy_volume = float(vol_)
                  total_price = np.multiply(float(buy_price), buy_volume)

            info.append(total_price)
            info.append(buy_price)
            info.append(buy_volume)
            # print("Execution:", info)

            return info

      def process(self):
        print("Dobby's turn to play")
        for i in range(self.len_range):
            curr_balance = self.balance  # updating the balance
            curr_high_price_ele = self.stock.high_price_list[i]
            curr_low_price_ele = self.stock.low_price_list[i]
            curr_volume_ele = self.stock.volume_list[i]
            
            print('\n|----------------Round{}-----------------|'.format(i+1))
            self.print_stock_info(curr_high_price_ele,
                                  curr_low_price_ele, curr_volume_ele)
            self.buy_or_pass = int(random.randint(0, 1))

            if self.buy_or_pass == 1:
                  print("|***Dobby is buying***")
            else:
                  print("|***Dobby pass this round*** \t\t|")
                  
            # print("Dobby selection", self.buy_or_pass)

            if self.buy_or_pass == 1:
            #     print("\n---Dobby Buying---")
                print("|\t-----Dobby Buying ----- \t|")  
                result = self.buy_stock_rp(
                    high_price=curr_high_price_ele, low_price=curr_low_price_ele)
                max_vol = curr_balance // result[1]

                print("|The random price of stock: {}\t|".format(result[1]))
                print("|Maximum volume of stock is {} \t|".format(max_vol))

                if curr_balance >= result[1]:
                    print("|Enough balance to buy the stock\t|")

                    print("|---------------------------------------|")

                    # result example: [40100.0, 401.0, 100.0]
                    in_vol = int(random.randint(int(1), int(max_vol)))
                    ran_price = int(result[1])
                    exp = float(np.multiply(float(ran_price), float(in_vol)))
                    print("|Dobby bought {} volume of stock  \t|".format(in_vol))
                    print("|Input vol: {}, expense: {} \t\t|".format(
                        in_vol, in_vol*ran_price))

                    # list contain the each expense of stock
                    self.info['expense'].append(exp)
                    # list contain the each price of run by random
                    self.info['total_stock_price_list'].append(ran_price)
                    # list contain the each volume of stock
                    self.info['volume_list'].append(in_vol)
                    self.balance -= exp

                  #   print("|result:|", exp, result[1], in_vol)

                else:
                    print("Not enough balance for this stock, so Dobby pass this round")
                    self.info['expense'].append(0)
                    self.info['total_stock_price_list'].append(0)
                    self.info['volume_list'].append(0)
                  #   print("|Dobby pass this round\t\t\t|")
                    print("|---------------------------------------|")
            else:
                self.info['expense'].append(0)
                self.info['total_stock_price_list'].append(0)
                self.info['volume_list'].append(0)
            #     print("|Dobby pass this round\t\t\t|")
                print("|---------------------------------------|")

        print("\nEnd of the game")
        print("----------------------------------------")
        print("Calculating your total expense.........\t")
        print("The total price of the stock you bought is {}".format(
            sum(self.info['expense'])))

      def get_expense_list(self):
            return self.info['expense'][0:self.len_range]

      def get_price_of_stock_buy_list(self):
            return self.info['total_stock_price_list'][0:self.len_range]

      def get_volume(self):
            return self.info['volume_list'][0:self.len_range]