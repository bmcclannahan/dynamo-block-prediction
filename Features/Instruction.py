
#An instruction is a memory location, hex values, instruction name, and register/memory block_analysis_functions
class Instruction:

    def __init__(self, memory_loc, hex_bits, name, assembly):
        self.memory_loc = memory_loc
        self.hex_bits = hex_bits
        self.name = name
        self.assembly = assembly
