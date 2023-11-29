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

def total_stocks(items):
  return sum(item[0] for item in items)

def stock_maximization(M, items):
  dp = [[0] * (M + 1) for _ in range(len(items) + 1)]
  #initialize the table

  for i in range(1, len(items) + 1):
    for j in range(1, M + 1):
      if items[i - 1][1] > j:
        dp[i][j] = dp[i - 1][j]
      else:
        pass

  return dp[len(items)][M]

file_path = 'input.txt'

parsed_inputs = parse_file(file_path)
