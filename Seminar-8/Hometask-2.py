def encrypt_caesar(message, shift):
  result = ''
  for symbol in message:
    if 1040 <= ord(symbol) <= 1103:
      if ord(symbol) > 1071 and ord(symbol) + shift > 1103:
        result += chr(1072 + (ord(symbol) + shift - 1103) - 1)
      elif ord(symbol) <= 1071 and ord(symbol) + shift > 1071:
        result += chr(1040 + (ord(symbol) + shift - 1071) - 1)
      else:
        result += chr(ord(symbol) + shift)
    else:
      result += symbol
  print(result)


def decrypt_caesar(message, shift):
  result = ''
  for symbol in message:
    if 1040 <= ord(symbol) <= 1103:
      if ord(symbol) >= 1072 and ord(symbol) - shift < 1072:
        res += chr(1103 - (1072 - (ord(symbol) - shift) - 1))
      elif ord(symbol) >= 1040 and ord(symbol) - shift < 1040:
        res += chr(1071 - (1040 - (ord(symbol) - shift) - 1))
      else:
        res += chr(ord(symbol) - shift)
    else:
      res += symbol
  print(result)

encrypt_caesar('Да здравсвует салат Цезарь', 3)
decrypt_caesar('Йе мйхезцзшкч цереч Ыкмехб', 3)