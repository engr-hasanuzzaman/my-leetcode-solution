'''
The cost of stock on each day is given in an array A[] of size N. 
Find all the days on which you buy and sell the stock so that
in between those days your profit is maximum.
'''

class Solution:
	def stockBuySell(self, A, n):
		#code here
		buy_day = 0
		ans = []
		previous_price = A[0]
		for i in range(1,n):
            # if buy price & currenc price same need to change buy_date
            # if current price is less then pre_price calculate buy & sell
		    if A[i] < previous_price or A[i] == A[buy_day]:
		        if buy_day != i - 1 and i - 1 > buy_day:
		            ans.append([buy_day, i-1])
		        buy_day = i  # change buy day
		    previous_price = A[i]
		if buy_day < n - 1:
		    ans.append([buy_day, n - 1])
		return ans