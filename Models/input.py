import numpy as np
 
instruction_library = [('mov',0),('test',1),('jz',2),('jmp',3),('sub',4),('cmp',5),('call',6),('jnz',7),('movzx',8)]
instruction_library.extend([('or',9),('add',10),('push',11),('setz',12),('xor',13),('pop',14),('lea',15),('and',16)])
instruction_library.extend([('data16',17),('lock',18),('dec',19),('shl',20),('cmpxchg',21),('setnz',22),('nop',23)])
instruction_library.extend([('shr',24),('movd',25),('movdqa',26),('movdqu',27),('neg',28),('pmovmskb',29),('mul',30)])
instruction_library.extend([('div',31),('sar',32),('cmovnz',33),('movss',34),('pcmpeqb',35),('inc',36),('pslldq',37)])
instruction_library.extend([('psubb',38),('pxor',39),('movhpd',40),('movlpd',41),('movsxd',42),('psrldq',43),('por',44)])
instruction_library.extend([('cmovb',45),('sbb',46),('rol',47),('jb',48),('jbe',49),('bsf',50),('punpcklbw',51),('cmovnb',52)])
instruction_library.extend([('cmovl',53),('cmovz',54),('ucomiss',55),('cvttss2si',56),('imul',57),('xchg',58)])
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
                #print(split)
                if split[0].rstrip() == 'True':
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
        
    return np.array(network_input), np.array(network_output)

def get_recurrent_three_input_array(filename, size):
    file = open(filename, "r")
    lines = file.readlines()

    network_input = [None]*size
    network_output = [None]*size
    block_array = [0]*3
    output_block = [[0]]*3
    index = 0

    for i in range(1,len(lines)):
        split = lines[i].split(' ')
        if lines[i][0] == '-':
            continue
        elif len(split) == 1:
            if split[0].rstrip() == "True":
                output_block[2] = [1]
                network_output[index] = output_block[:]
            else:
                output_block[2] = [0]
                network_output[index] = output_block[:]
            network_input[index] = block_array[:]
            
            index += 1
        else:
            array = [0]*(len(instruction_library)+8)
            array[instruction_dictionary[split[0]]] = 1
            array[len(instruction_dictionary) + parameter_type_dict[split[1]]] = 1
            array[len(instruction_dictionary) + 4 + parameter_type_dict[split[2]]] = 1
            block_array[0] = block_array[1]
            block_array[1] = block_array[2]
            block_array[2] = array

    return network_input, network_output

def get_recurrent_input_array(filename):
    file = open(filename, "r")
    lines = file.readlines()

    network_input = []
    network_output = []
    block_array = []

    for i in range(1,len(lines)):
        split = lines[i].split(' ')
        if lines[i][0] == '-':
            continue
        elif len(split) == 1:
            if split[0].rstrip() == "True":
                network_output.append([1])
            else:
                network_output.append([0])
            network_input.append(block_array)
            block_array = []
        else:
            array = [[0]]*(len(instruction_library)+8)
            array[instruction_dictionary[split[0]]] = [1]
            array[len(instruction_dictionary) + parameter_type_dict[split[1]]] = [1]
            array[len(instruction_dictionary) + 4 + parameter_type_dict[split[2]]] = [1]
            block_array.append(array)

    return network_input, network_output