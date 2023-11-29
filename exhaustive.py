# Darren Chen
# CPSC335

import ast
from itertools import combinations

def parse_file(file_path):
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

  parsed_results = []

  i = 0
  while i < len(lines):
    N = int(lines[i])
    i += 1

    stock_and_values = ast.literal_eval(lines[i].strip())
    i += 1
    amount = int(lines[i].strip())
    i += 1

    parsed_results.append((N, stock_and_values, amount))
    # make a tuple

  return parsed_results

file_path = 'input.txt'

parsed_inputs = parse_file(file_path)

def total_value(candidate, items):
  return sum(items[i][1] for i in candidate)

def total_stocks(candidate, items):
   return sum(items[i][0] for i in candidate)

def verify_combination(M, items, candidate):
  return total_value(candidate, items) <= M

def stock_combinations(items):
    for combo_length in range(1, len(items) + 1):
        for combo in combinations(range(len(items)), combo_length):
            yield list(combo)

def stock_maximization (M, items):
  best = None
  best_stock_count = 0
  for candidate in stock_combinations(items):
      if verify_combination(M, items, candidate):
          candidate_stock_count = total_stocks(candidate, items)
          if best is None or candidate_stock_count > best_stock_count:
              best = candidate
              best_stock_count = candidate_stock_count
  return best_stock_count

print("Using exhaustive program: ")

# tester
for N, stocks_and_values, amount in parsed_inputs:
  print(stock_maximization(amount, stocks_and_values))
