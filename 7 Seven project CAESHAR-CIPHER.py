from my_logo import logo

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
] * 100


def caesar(direction_caesar, text_caesar, shift_alf):
  result_caesar = []
  if direction_caesar == 'decode':
    shift_alf *= -1
  for char in text_caesar:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_alf
      new_letter = alphabet[new_position]
      result_caesar.append(new_letter)
    else:
      result_caesar.append(char)
  print(f"Your {direction_caesar}d text is {''.join(result_caesar)}")


should_end = False
while not should_end:
  print(logo)
  direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower().lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(direction_caesar=direction, text_caesar=text, shift_alf=shift)

  result = input(
    "Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
  if result == 'no':
    should_end = True
    print('Goodbye')
