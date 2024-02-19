# d - dark
# p - player
# m - mountain
# e - enemy
# t - treasure

# map1
# m mmm mmm mmm m
# m tdd dpd ddd m
# m ddd ddd ddd m
# m ddd ded ddd m
# m mmm mmm mmm m

#qwerty layout:
# QWERT   YUIOP
#  ASDFG   HJKL
#   ZXCVB   NM

# qwerty keymap:
# map: q
# inventory: w
# attack: e
# magic: r
# movement: asdf

map  = [
          [m mmm mmm mmm m],
          [],
          [],
          [],
          [m mmm mmm mmm m]
]
  


class Player(self):
  self.pos_x = 1
  self.pos_y = 1

#main loop
while True:
  print(current_map)
  input_var = input("input:")
