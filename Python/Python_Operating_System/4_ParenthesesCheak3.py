Data = ['<', '(', ')', '>', '<', '<']
stack = []

pare = [0] * 128

pare[ord('>')] = '<'
pare[ord(']')] = '['
pare[ord('}')] = '{'
pare[ord(')')] = '('