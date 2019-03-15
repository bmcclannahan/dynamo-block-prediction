from Block import Block

def generate_block(lines, start, end):
    block = []
    for i in range(start, end +1):
        current = lines[i].split(" ")
        index = 0
        for j in range(len(current)):
            if current[index] == '':
                del current[index]
            else:
                current[index].rstrip()
                index += 1
        if len(current) > 1:
            block.append(current[:-1])
    return block

def filter_jz_blocks(blocks):
    jz_blocks = []
    for block in blocks:
        if block[-2][-2] == 'jz' or block[-2][-2] == 'jnz':
            jz_blocks.append(block)
    return jz_blocks

def write_blocks(blocks, filname):
    jump_file = open(filname, 'a+')
    for block in blocks:
        for line in block:
            new_line = ''
            for instr in line:
                new_line += instr.rstrip() + ' '
            jump_file.write(new_line+'\n')

def read_file(filename):
    blocks_file = open(filename,"r")
    block_lines = blocks_file.readlines()

    blocks = []
    block_start = 0
    block_end = 0

    for i in range(len(block_lines)):
        line = block_lines[i]
        if line.split(" ")[0] == "Block":
            block_start = i
        elif line.split(" ")[0] == "Actual:":
            block_end = i

            blocks.append(generate_block(block_lines, block_start, block_end))
    return blocks

def create_block_object(block_lines):
    actual_length = len(block_lines[-1][-1])
    #print(block_lines[-1][-1],block_lines[-2][-1][0-actual_length:], block_lines[-1][-1] == block_lines[-2][-1][0-actual_length:])
    return Block(block_lines[1:-1], block_lines[-1][-1] == block_lines[-2][-1][0-actual_length:], block_lines)
