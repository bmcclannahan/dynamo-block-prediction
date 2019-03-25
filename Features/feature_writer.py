def write_features_to_file(filename, blocks):
    file = open(filename, 'a+')
    for block in blocks:
        file.write('--------------------\n')
        for instruction in block.instructions:
            file.write(instruction.op+' '+instruction.first_parameter+' '+instruction.second_paramater+' '+'\n')
        if block.jumps:
            file.write('True\n')
        else:
            file.write('False\n')
        file.write('--------------------')
