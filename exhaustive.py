# Darren Chen
# CPSC335

stock_combinations = []
candidate = None

def total_value():
  pass

def verify_combination():
  pass

def stock_maximization (M, items):
  best = None
  for candidates in stock_combinations(items):
    if verify_combination(M, items, candidate):
      if best is None or total_value(candidate) > total_value(best):
        best = candidate
  return best
