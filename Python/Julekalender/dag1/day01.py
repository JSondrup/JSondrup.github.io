def solutionA(lines):
    facit = 0
    highest_number = 0
    for line in lines:
        if line == '':
            facit = 0
        else:
            facit = facit+int(line)
            if facit > highest_number:
                highest_number = facit


    return highest_number


def solutionB(lines):
  # TODO: replace with code solving the problem
  result = -1 # Dummy result
  return result


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
  input_file_name = "input-day01.txt" 

  print(f"Loading data from: {input_file_name}")
  lines = load_data(input_file_name)


  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")