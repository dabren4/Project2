# Darren Chen
# CPSC335

import ast

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
