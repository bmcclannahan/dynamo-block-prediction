from Instruction import Instruction, instruction_library


#A block is made up of instructions and a boolean that represents whether it
#jumps or goes to the next line
class Block:

    def __init__(self, instructions, jumps, file_text):
        self.instructions = self.build_instruction_list(instructions)
        self.jumps = jumps
        self.file_text = file_text

    def build_instruction_list(self, instructions):
        instr_list = []
        for instruction in instructions:
            name = None
            index = 1
            for i in range(len(instruction)-1):
                if instruction[i+1] in instruction_library:
                    name = instruction[i]
                    index = i
            # if name == None:
            #     print(instruction)
            if name != None:
                instr_list.append(Instruction(instruction,index+1))
        return instr_list

    def print_block(self):
        print('------------------')
        print(self.file_text)
        print(self.jumps)
        print('------------------')
        for instruction in self.instructions:
            print(instruction.op, instruction.first_parameter, instruction.second_paramater)
        print('------------------')
