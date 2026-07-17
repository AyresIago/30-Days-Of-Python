solve_linear = lambda x1, x2, y1, y2:(
  m := (y2 - y1)/(x2-x1),
  y1 - m*x1
)

print(solve_linear(4, 6, 9, 2))

