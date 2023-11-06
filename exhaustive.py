# Darren Chen
# CPSC335

stock_combinations = []
candidate = None

def total_value(candidate, items):
  return sum(items[i][1] for i in candidate)

def verify_combination(M, items, candidate):
  return total_value(candidate, items) <= M

def stock_maximization (M, items):
  best = None
  for candidates in stock_combinations(items):
    if verify_combination(M, items, candidate):
      if best is None or total_value(candidate) > total_value(best):
        best = candidate
  return best
