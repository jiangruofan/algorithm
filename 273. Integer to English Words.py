class Solution:
    def numberToWords(self, num: int) -> str:
        single = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                 "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return 'Zero'

        def convert(s, index):
            res = ''
            if s[0] != '0':
                res += single[int(s[0])] + ' Hundred '
            if s[1] == '1':
                res += teens[int(s[2])] + ' '
                return res + index + ' '
            if s[1] != '0':
                res += tens[int(s[1])] + ' '
            if s[2] != '0':
                res += single[int(s[2])] + ' '
            return res if res == '' else res + index + ' '

        s1 = str(num)
        s1 = '0' * (12 - len(s1)) + s1
        ans = convert(s1[0:3], 'Billion') + convert(s1[3:6], 'Million') + convert(s1[6:9], 'Thousand') + convert(
            s1[9:12], '')
        return ans.rstrip()