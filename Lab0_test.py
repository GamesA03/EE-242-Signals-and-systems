a=input("Input A:")
def isPalindrome(input_string):
  letters = list(input_string)
  reversed_letters = letters[::-1]

  for i in range(len(input_string)):

      if letters[i] != reversed_letters[i]:
        return False
  return True

b=isPalindrome("Mahmood Hameed")
print("Output B:"+str(b)) #Should be False
c=isPalindrome("Signals, Systems and Data I:I ataD dna smetsyS ,slangiS")
print("Output C:"+str(c)) #Should be True
d=isPalindrome(a)
print("Output D:"+str(d))