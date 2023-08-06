# from Stock_main import *
# from Buy import *
from main_package.Stock_main import *
from main_package.Buy import *



class User(Stock, Buy):
    def __init__(self,Stock):
        __metaclass__ = Stock # the class User inherits from Stock and must initialize a meta class from Stock 
        self.stock = Stock
        self.len_range = int(self.stock.n)
        self.balance = 10000 # initial balance 
        self.info = {'price_of_stock_buy': [],
                            'expense': [],
                            'volume_list': [],
                            'total_price_of_stock_by_each_process': 0,
                            'total_stock_price_list': [], 
                            'result_list': []}
    def check_the_input_Y_N(self, input):
            if (input == "Y" or input == 'y'):
                return True
            else:
                return False
            
    def check_balance(balance, expense):
                        if (balance - expense >= 0):
                            
                            return True
                        else:
                            return False


    def print_stock_info(high, low, vol):
                print("|The high price of stock is {} {}".format(high,'\t|'))
                print("|The low price of stock is {} {}".format(low,'\t\t|'))
                print("|The volume of stock is {} {}".format(vol,'\t\t|'))

    def process(self):
        for i in range(self.len_range):
            curr_balance = self.balance # updating the balance
            curr_high_price_ele = self.stock.high_price_list[i]
            curr_low_price_ele = self.stock.low_price_list[i]
            curr_volume_ele = self.stock.volume_list[i]
            
            print('\n|----------------Round{}-----------------|'.format(i+1))
            User.print_stock_info(curr_high_price_ele, curr_low_price_ele, curr_volume_ele)

            self.buy_or_pass = input("Do you want to buy the stock? (Y/N)\n")
            if (self.check_the_input_Y_N(self.buy_or_pass) == True):
                print("|\t-------- Buying --------\t|")        
                if (Buy.check_balance(curr_balance, self.info['total_price_of_stock_by_each_process']) == True):
                    print("|Enough balance to buy the stock\t|")
                
                    result = Buy.buy_stock(high_price = curr_high_price_ele, low_price = curr_low_price_ele, balance = curr_balance, vol = curr_volume_ele)
                    # print("|result:{}\t\t|".format(result))
                    print("|---------------------------------------|")
                    
                    # result example: [40100.0, 401.0, 100.0]
                    exp = int(result[0])
                    ran_price = int(result[1])
                    in_vol = int(result[2])
                    
                    self.info['expense'].append(exp)                        # list contain the each expense of stock (user input)
                    self.info['total_stock_price_list'].append(ran_price)   # list contain the each price of run by random
                    self.info['volume_list'].append(in_vol)                 # list contain the each volume of stock (user input)
                    self.balance -=  exp
                            
            else:
                if (self.buy_or_pass != "N" and self.buy_or_pass != "n"):
                    self.info['expense'].append(0)
                    self.info['total_stock_price_list'].append(0)
                    self.info['volume_list'].append(0)
                    break
                else:
                    self.info['expense'].append(0)
                    self.info['total_stock_price_list'].append(0)
                    self.info['volume_list'].append(0)
                    print("|You pass this round\t\t\t|")
                    print("|---------------------------------------|")

                
        print("\nEnd of the game")
        print("----------------------------------------")
        print("Calculating your total expense.........\n")
        # print("The total price of the stock you bought is {}".format(sum(self.info['expense'])))

    def get_expense_list(self):
            return self.info['expense'][0:self.len_range]

    def get_price_of_stock_buy_list(self):
            return self.info['total_stock_price_list'][0:self.len_range]

    def get_volume(self):
            return self.info['volume_list'][0:self.len_range]