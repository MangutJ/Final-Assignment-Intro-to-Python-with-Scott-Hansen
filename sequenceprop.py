def sequence_replacement(sequence: list[int], iterations: int) -> list[int]:
  """
  This function takes a sequence of integers and iterates over it, replacing consecutive 
  equal elements with their count followed by the element itself. 

  Args:
      sequence: A list of integers representing the initial sequence.
      iterations: The number of times the replacement process should be applied.

  Returns:
      A new list of integers representing the sequence after the specified number of iterations.

  Raises:
      TypeError: If either sequence or iterations is not of type int.
  """

  if not isinstance(sequence, list) or not all(isinstance(x, int) for x in sequence):
    raise TypeError("sequence must be a list of integers")

  if not isinstance(iterations, int):
    raise TypeError("iterations must be an integer")

  if iterations == 0:
    return sequence

  new_sequence = []
  count = 1
  for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
      count += 1
    else:
      new_sequence.extend([count, sequence[i - 1]])
      count = 1
  new_sequence.extend([count, sequence[-1]])

  return sequence_replacement(new_sequence, iterations - 1)


# Wrapper function
def sequence_prop_30(sequence: int) -> int:
  """
  This function takes an integer, converts it to a list of digits, applies the 
  sequence_replacement function with 30 iterations, and returns the length of the resulting list.

  Args:
      sequence: An integer representing the initial sequence.

  Returns:
      An integer representing the length of the final sequence after 30 iterations.

  Raises:
      TypeError: If the sequence is not of type int.
  """

  if not isinstance(sequence, int):
    raise TypeError("sequence must be an integer")

  final_sequence = sequence_replacement(list(map(int, str(sequence))), 30)
  return len(final_sequence)
