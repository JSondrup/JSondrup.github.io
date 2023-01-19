def solutionA(lines):
  for line in lines:
    opp = line[0]
    me = line[2]
    draw = 3
    win = 6
    loss = 0
    X = 1
    Y = 2
    Z = 3
    total = 0
    total_A = 0
    total_B = 0
    total_C = 0
    if opp == 'A':
      if me == 'X':
         sum = X + draw
      if me == "Y":
        sum = Y + win
      if me == 'Z':
        sum = Z + win
    total += sum
    if opp == 'B':
      if me == 'X':
        sum = X + loss
      if me == "Y":
        sum = Y + draw
      if me == 'Z':
        sum = Z + win
    total += sum
    if opp == 'C':
      if me == 'X':
        sum = X + win
      if me == "Y":
        sum = Y + loss
      if me == 'Z':
        sum = Z + draw
    total += sum
  print(total)
  return sum # Dummy result, deliberately wrong


def solutionB(lines):
  # TODO: replace with code solving the problem
  return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  # input_file_name = "input-day02.txt" 
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")
