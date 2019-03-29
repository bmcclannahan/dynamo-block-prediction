instruction_library = ['mov','test','jz','jmp','sub','cmp','call','jnz','movzx','or','add','push','setz', 'xor', 'pop', 'lea']
instruction_library.extend(['and', 'data16', 'lock', 'dec', 'shl', 'cmpxchg', 'setnz', 'nop', 'shr', 'movd', 'movdqa', 'movdqu'])
instruction_library.extend(['neg', 'pmovmskb', 'mul', 'div', 'sar', 'cmovnz', 'movss', 'pcmpeqb', 'inc', 'pslldq'])
instruction_library.extend(['psubb', 'pxor', 'movhpd', 'movlpd', 'pxor', 'psrldq', 'por', 'cmovb', 'sbb', 'rol','movsxd'])
instruction_library.extend(['jb','jbe','bsf','punpcklbw','cmovnb','cmovl','cmovz','ucomiss','cvttss2si', 'imul', 'xchg'])

#An instruction is a memory location, hex values, instruction name, and register/memory block_analysis_functions
class Instruction:

    def __init__(self, text, name_index):
        self.op, self.first_parameter, self.second_paramater = self.parseInstruction(text,name_index)

    #types of parameters
    #r = register
    #m = memory
    #o = memory offset of register
    #n = no value for this parameter
    def parseInstruction(self, text, name_index):
        count = 0
        for i in range(name_index, len(text)):
            if text[i-count] == '<rel>':
                text = text[0:i]+text[i+1:]
                count += 1
        opcode = text[name_index]
        first_parameter = ''        
        second_paramater = ''
        if len(text)-1 == name_index:
            first_parameter = 'n'
            second_paramater = 'n'
        elif len(text)-2 == name_index:
            first_parameter = 'm'
            second_paramater = 'n'
        elif len(text)-3 == name_index:
            if text[name_index+1][0] == '%':
                first_parameter = 'r'
            elif text[name_index+1][0] == '$':
                first_parameter = 'm'
            else:
                first_parameter = 'o'
            if text[name_index+2][0] == '%':
                second_paramater = 'r'
            elif text[name_index+2][0] == '$':
                second_paramater = 'm'
            else:
                second_paramater = 'o'
        else:
            arrow_index = 0
            for i in range(name_index+1,len(text)):
                if text[i] == '->':
                    arrow_index = i
            if arrow_index != 0:
                if opcode == 'mov':
                    if text[name_index+1][0] != '%':
                        first_parameter = 'o'
                        second_paramater = 'n'
                    else:
                        first_parameter = 'm'
                        second_paramater = 'm'
                elif arrow_index - name_index < len(text) - arrow_index:
                    first_parameter = 'o'
                    if text[-1][0] == '%':
                        second_paramater = 'r'
                    elif text[-1][0] == '$':
                        second_paramater = 'm'
                    else:
                        second_paramater = 'o'
                else:
                    second_paramater = 'o'
                    if text[name_index+1][0] == '%':
                        first_parameter = 'r'
                    elif text[name_index+1][0] == '$':
                        first_parameter = 'm'
                    else:
                        first_parameter = 'o'
        
        return opcode, first_parameter, second_paramater
