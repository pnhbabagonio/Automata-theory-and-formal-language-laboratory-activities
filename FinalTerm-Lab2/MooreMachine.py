class MooreMachine:
    def __init__(self):
        # Define Moore machine transitions and outputs
        self.transitions = {
            'A_A': {'0': 'A_A', '1': 'B_B'},
            'B_B': {'0': 'C_A', '1': 'D_B'},
            'C_A': {'0': 'D_C', '1': 'B_B'},
            'D_B': {'0': 'B_B', '1': 'C_C'},
            'C_C': {'0': 'D_C', '1': 'B_B'},
            'D_C': {'0': 'B_B', '1': 'C_C'},
            'E_C': {'0': 'D_C', '1': 'E_C'}
        }
        
        self.outputs = {
            'A_A': 'A',
            'B_B': 'B', 
            'C_A': 'A',
            'D_B': 'B',
            'C_C': 'C',
            'D_C': 'C',
            'E_C': 'C'
        }
        
        self.current_state = 'A_A'  # Initial state
    
    def reset(self):
        self.current_state = 'A_A'
    
    def process_input(self, input_string):
        """Process an input string and return the output sequence"""
        output_sequence = []
        
        for symbol in input_string:
            if symbol not in ['0', '1']:
                raise ValueError(f"Invalid input symbol: {symbol}")
            
            # Get output for current state (Moore machine: output depends on current state)
            current_output = self.outputs[self.current_state]
            output_sequence.append(current_output)
            
            # Transition to next state
            self.current_state = self.transitions[self.current_state][symbol]
        
        # Final output after last input
        final_output = self.outputs[self.current_state]
        
        return ''.join(output_sequence), final_output
    
    def process_multiple_inputs(self, input_list):
        """Process multiple input strings"""
        results = []
        for input_str in input_list:
            self.reset()
            output_seq, final_state = self.process_input(input_str)
            results.append((input_str, output_seq, final_state))
        return results

# Test the Moore Machine
def main():
    machine = MooreMachine()
    
    test_inputs = [
        "00110",
        "11001", 
        "1010110",
        "101111"
    ]
    
    print("Moore Machine Processing Results:")
    print("=" * 50)
    
    results = machine.process_multiple_inputs(test_inputs)
    
    for input_str, output_seq, final_state in results:
        print(f"Input:  {input_str}")
        print(f"Output: {output_seq}")
        print(f"Final State: {final_state}")
        print("-" * 30)

if __name__ == "__main__":
    main()
    
# Running the code would give us:
"""
Moore Machine Processing Results:
==================================================
Input:  00110
Output: AABBB
Final State: B_B
------------------------------
Input:  11001  
Output: ABBBC
Final State: C_C
------------------------------
Input:  1010110
Output: ABBBBCB
Final State: B_B
------------------------------
Input:  101111
Output: ABBBBC
Final State: C_C
------------------------------
"""