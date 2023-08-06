import random
import numpy as np
import pandas as pd
# this is for end game module


def cashback(player_1_status, dobby_2_status):
      cash_back_1 = list()
      cash_back_2 = list()
      play_track_1 = player_1_status[0]
      play_track_2 = dobby_2_status[0]
      
      #assuming both user and dobby play the same number of times
      #if user had decided not to play a round, they get cashback for the same amount played by Dobby or viceversa
      #this is to make a fair comparison for game totals
      for i in range(len(play_track_1)):
            if play_track_1[i] == 0 or play_track_2[i] == 0:
                  if play_track_1[i] == 0:
                        cash_back_1.append(play_track_2[i])
                        cash_back_2.append(0)
                  elif play_track_2[i] == 0:
                        cash_back_2.append(play_track_1[i])  
                        cash_back_1.append(0)
                  else:
                        cash_back_1.append(0)
                        cash_back_2.append(0)      
            else:
                  cash_back_1.append(0)
                  cash_back_2.append(0)
                  
      return (cash_back_1, cash_back_2)



# Calculate current price for each stock and calculate player win
# add one more argument for player stock high and low to calculate current price

def buy_stock_rp(high_price, low_price, vol=0):
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

def final_price(status, stock_list):
      high = stock_list[0]
      low = stock_list[1]
      rounds = stock_list[2]
      
      # vol = status[2]
      sell_price = []

      for i in range(rounds):
            curr_price = buy_stock_rp(high[i], low[i])
            sell_price.append(float(curr_price[1]))
            #total_value.append(stock_price*vol[i])

      return sell_price

# show summary for all rounds, by player