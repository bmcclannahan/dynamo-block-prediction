from Instruction import Instruction

instruction_library = ['mov','test','jz','jmp','sub','cmp','call','jnz','movzx','or','add','push','setz', 'xor', 'pop', 'lea']
instruction_library.extend(['and', 'data16', 'lock', 'dec', 'shl', 'cmpxchg', 'setnz', 'nop', 'shr', 'movd', 'movdqa', 'movdqu'])
instruction_library.extend(['neg', 'pmovmskb', 'mul', 'div', 'sar', 'cmovnz', 'movss', 'pcmpeqb', 'inc', 'pslldq'])
instruction_library.extend(['psubb', 'pxor', 'movhpd', 'movlpd', 'pxor', 'psrldq', 'por', 'cmovb', 'sbb', 'rol','movsxd'])

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
            mem = instruction[0]
            hex_bits = None
            name = None
            assembly = None
            for i in range(len(instruction)-1):
                if instruction[i+1] in instruction_library:
                    hex_bits = instruction[1:i]
                    name = instruction[i]
                    assembly = instruction[i+1:]
            #if name == None:
                #print(instruction)
            if name != None:
                instr_list.append(Instruction(mem,hex_bits,name,assembly))
        return instr_list
