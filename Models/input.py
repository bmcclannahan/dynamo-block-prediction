instruction_library = [('mov',0),('test',1),('jz',2),('jmp',3),('sub',4),('cmp',5),('call',6),('jnz',7),('movzx',8)]
instruction_library.extend([('or',9),('add',10),('push',11),('setz',12),('xor',13),('pop',14),('lea',15),('and',16)])
instruction_library.extend([('data16',17),('lock',18),('dec',19),('shl',20),('cmpxchg',21),('setnz',22),('nop',23)])
instruction_library.extend([('shr',24),('movd',25),('movdqa',26),('movdqu',27),('neg',28),('pmovmskb',29),('mul',30)])
instruction_library.extend([('div',31),('sar',32),('cmovnz',33),('movss',34),('pcmpeqb',35),('inc',36),('pslldq',37)])
instruction_library.extend([('psubb',38),('pxor',39),('movhpd',40),('movlpd',41),('movsxd',42),('psrldq',43),('por',44)])
instruction_library.extend([('cmovb',45),('sbb',46),('rol',47)])
instruction_dictionary = dict(instruction_library)

parameter_type_dict = {'m':0, 'r':1, 'o':2, 'n':3}

def get_feed_forward_input_array(filename):
    file = open(filename,"r")
    lines = file.readlines()
    prev_opcode = ''
    prev_first = ''
    prev_second = ''
    opcode = ''
    first_parameter = ''
    second_parameter = ''
    result = 0

    network_input = []
    network_output = []
    for i in range(1,len(lines)):
        if lines[i][0] == '-':
            array = [0]*(len(instruction_library)+8)
            array[instruction_dictionary[prev_opcode]] = 1
            array[len(instruction_dictionary) + parameter_type_dict[prev_first]] = 1
            array[len(instruction_dictionary) + 4 + parameter_type_dict[prev_second]] = 1
            network_input.append(array)
            network_output.append(result)
        else:
            split = lines[i].split(' ')
            #print(split)
            if len(split) == 1:
                if split[0]:
                    result = 1
                else:
                    result = 0
            else:
                prev_opcode = opcode
                prev_first = first_parameter
                prev_second = second_parameter
                
                opcode = split[0]
                first_parameter = split[1]
                second_parameter = split[2]
        
    return network_input, network_output