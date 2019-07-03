set1=["a","e","i","o","u"]
set2=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
word=str(input())
if word in set1:
  print("Vowel")
elif word in set2:
  print("Consonant")
else:
  print("invalid")
