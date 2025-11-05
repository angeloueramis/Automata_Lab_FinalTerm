class MooreMachine:
    def __init__(self):
        self.transitions = {
            'A': {'0': ('A', 'A'), '1': ('B', 'B')},
            'B': {'0': ('C', 'A'), '1': ('D', 'B')},
            'C': {'0': ('D', 'C'), '1': ('B', 'B')},
            'D': {'0': ('B', 'B'), '1': ('C', 'C')},
            'E': {'0': ('D', 'C'), '1': ('E', 'C')}
        }

        #start state
        self.current_state = 'A'

    def reset(self, start_state='A'):
        """Reset the machine to start state (for each test)"""
        self.current_state = start_state

    def process_input(self, input_string):
        """Process input string and return the sequence of outputs."""
        output_sequence = []

        for inp in input_string:
            if inp not in ('0', '1'):
                return None 

            next_state, output = self.transitions[self.current_state][inp]
            output_sequence.append(output)
            self.current_state = next_state 

        return ''.join(output_sequence)

    def test(self, test_strings):
        print("Testing Converted Moore Machine:\n")
        for s in test_strings:
            self.reset()  #reset to start state for each test
            output = self.process_input(s)
            if output is not None:
                print(f"Input: {s:<10} → Output: {output}")
            else:
                print(f"Input: {s:<10} → Invalid sequence")

#testing
if __name__ == "__main__":
    lab = MooreMachine()
    lab.test(["00110", "11001", "1010110", "101111"])

    #for manual input
    print("\nTry your own input:")
    user_input = input("Enter input string (0s and 1s): ")
    lab.reset()
    result = lab.process_input(user_input)
    print(f"Output: {result}")
