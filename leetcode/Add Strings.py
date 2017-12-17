# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 思考: 使用ord()來轉換文字為unicode, but長度只能為1
# 處理溢位: 每次將加總%10 把剩餘的樹加到list, 加總//10給溢位carry
# 因為result接到的答案是從個位開始 所以要reverse 結果list

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        carry = 0 # initial 溢位
        result = []
        while len(num1) > 0 or len(num2) > 0:
            # ord("0") == 48 
            n1 = ord(num1.pop()) - ord("0") if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord("0") if len(num2) > 0 else 0
            
            Sum = n1 + n2 + carry
            result.append(Sum%10) # 只存入非溢位數
            carry = Sum // 10 # 存入溢位
        
        if carry: # 還有剩餘溢位,直接加上result
            result.append(carry)
        
        result = result[::-1]
        return "".join([str(i) for i in result])
        