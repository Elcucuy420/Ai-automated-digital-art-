import random
PALETTES = [
  ["#0B0C10","#1F2833","#C5C6C7","#66FCF1","#45A29E"],
  ["#FDF6E3","#EEE0CB","#D9CAB3","#C5BAA4","#A0937D"],
  ["#1E1E1E","#2D2D2D","#4C566A","#88C0D0","#ECEFF4"],
  ["#2B2D42","#8D99AE","#EDF2F4","#EF233C","#D90429"],
  ["#231942","#5E548E","#9F86C0","#BE95C4","#E0B1CB"],
  ["#0D1B2A","#1B263B","#415A77","#778DA9","#E0E1DD"],
  ["#F72585","#B5179E","#7209B7","#3A0CA3","#4361EE"],
]
def pick():
  return random.choice(PALETTES)
