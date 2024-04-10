from sorted import sorted_steps

# Define the rule list
rule_list = [['C', 'A'], ['C', 'F'], ['A', 'B'], ['A', 'D'], ['B', 'E'], ['D', 'E'], ['F', 'E']]

# Get the sorted steps
step_string = sorted_steps(rule_list)

# Print the result
print("Sorted steps:", step_string)
