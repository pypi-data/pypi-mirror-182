import numpy as np
import random
class Buy():
      def __init__(self, high_price, low_price, balance):
            self.high_price = high_price
            self.low_price = low_price
            self.balance = balance
            self.volume = 0
            self.price = 0
            self.expense = 0
      
      def check_balance(balance, expense):
            try:
                  if (balance - expense >= 0):
                        return True
                  else:
                        return False
            except TypeError:
                  print("Error: balance and expense must be numeric values")
            except ValueError:
                  print("Error: balance and expense must be positive numeric values")
            except ZeroDivisionError:
                  print("Error: balance and expense cannot be zero")
            except Exception:
                  print("An unknown error occurred")
                        
                        
      def check_volume(curr_vol, input_vol):
            try:
                  if (curr_vol - input_vol >= 0):
                        return True
                  else:
                        return False
            except TypeError:
                  print("Error: curr_vol and input_vol must be numeric values")
            except ValueError:
                  print("Error: curr_vol and input_vol must be positive numeric values")
            except ZeroDivisionError:
                  print("Error: curr_vol and input_vol cannot be zero")
            except Exception:
                  print("An unknown error occurred")

      def execute(high_price, low_price, balance, input_volume, random_price):
            info = []
            input_volume = float(input_volume)
            
            bool_var = Buy.check_balance(balance, input_volume*random_price)
            buy_price = float(random_price)
            buy_volume = float(input_volume)
            total_price = np.multiply(float(buy_price), buy_volume)
            
            info.append(total_price)
            info.append(buy_price)
            info.append(buy_volume)
            # print("Execution:", info)
            return info
      
      def buy_stock(high_price, low_price, balance, vol):
            high_price_ = high_price
            low_price_ = low_price
            balance_ = balance
            vol_ = vol
            random_price = float(random.randint(int(low_price), int(high_price_)))
                  
            print("|The random price of stock: {}\t|".format(random_price))
            print("|Volume of stock is {}\t\t\t|".format(vol))
            input_volume = int(input("How many volume do you want to buy?\n"))
            input_volume = float(input_volume)
            
            bool_var_bal = Buy.check_balance(balance_, input_volume*random_price)
            bool_var_vol = Buy.check_volume(vol_, input_volume)
            print("|You bought {} volume of stock  \t|".format(input_volume))
            print("|Input vol: {}, expense: {} \t|".format(input_volume, input_volume*random_price))
            if (bool_var_bal == True and bool_var_vol == True):
                  # print("|You bought {} volume of stock \t|".format(input_volume))
                  # print("|Input vol: {}, expense: {} \t|".format(input_volume, input_volume*random_price))
                  if (bool_var_vol == True):
                        execute_result = Buy.execute(high_price_, low_price_, balance_, input_volume, random_price)
                        # print(execute_result)
                        return execute_result
                  else:
                        print("|\t-------- Warning --------\t|")  
                        
                        while(bool_var_vol == False):
                              print("|The vol you input is {}, and the expense is {}".format(input_volume, input_volume*random_price))
                              print("|Sorry, the input volume is larger than the available volume of the stock")
                              print("|Please buy a smaller volume")
                              input_volume = int(input("How many volume do you want to buy?\n"))
                              input_volume = float(input_volume)
                              bool_var_vol = Buy.check_volume(vol_, input_volume)
                              if (bool_var_vol == True):
                                    print("|You bought {} volume of stock\t\t|".format(input_volume))
                                    execute_result = Buy.execute(high_price_, low_price_, balance_, input_volume, random_price)
                                    # print(execute_result)
                                    return execute_result
            else:
                  print("|\t-------- Warning --------\t|")  
                  
                  while(bool_var_bal == False):
                        # print("The vol you input is {}, and the expense is {}".format(input_volume, input_volume*random_price))
                        print("|Sorry, balance isn't enough\t\t|")
                        # print("Please buy a smaller volume")
                        input_volume = int(input("How many volume do you want to buy?\n"))
                        input_volume = float(input_volume)
                        bool_var_bal = Buy.check_balance(balance_, input_volume*random_price)
                        if (bool_var_bal == True):
                              print("|You bought {} volume of stock\t|".format(input_volume))
                              execute_result = Buy.execute(high_price_, low_price_, balance_, input_volume, random_price)
                              # print(execute_result)
                              return execute_result