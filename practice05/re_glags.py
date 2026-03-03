import re
# Example 1 - IGNORECASE
print(re.search(r"total", "TOTAL: $45.67", re.IGNORECASE).group())  # TOTAL

# Example 2 - MULTILINE
text = "Total: $45.67\nSubtotal: $30.00"
print(re.findall(r"^\w+:", text, re.MULTILINE))  # ['Total:', 'Subtotal:']

# Example 3 - IGNORECASE with findall
print(re.findall(r"total", "TOTAL total Total", re.IGNORECASE))  # ['TOTAL','total','Total']

# Example 4 - MULTILINE start of line
text2 = "Date: 2026-02-27\nInvoice: #12345"
print(re.findall(r"^Invoice:.*", text2, re.MULTILINE))  # ['Invoice: #12345']
