from block_parsing_functions import generate_block, filter_jz_blocks, write_blocks, read_file, create_block_object, generate_unprocessed_block, read_unprocessed_file
from block_analysis_functions import average_instr_len_by_result
from feature_writer import write_features_to_file
from Block import Block

file =read_unprocessed_file('./blocks2.txt')
print(file[1])
blocks = filter_jz_blocks(file)
write_blocks(blocks,'./filtered_blocks2.txt')
print(blocks[0])
file_blocks = read_file('./filtered_blocks2.txt')
blocks = []

num_blocks = len(file_blocks)
total_instructions = 0

for block in file_blocks:
    total_instructions += len(block) - 2

print("Total blocks: ", num_blocks)
print("Instructions per block:", total_instructions/num_blocks)
for block in file_blocks:
    blocks.append(create_block_object(block))

blocks[2].print_block()

write_features_to_file('features2.txt', blocks)

(instr_on_jump, instr_on_no_jump, blocks_on_jump, blocks_on_no_jump) = average_instr_len_by_result(blocks)
print(instr_on_jump, instr_on_no_jump, blocks_on_jump, blocks_on_no_jump)


print("Instructions Per Jump:",instr_on_jump/blocks_on_jump)
print("Instructions per no jump", instr_on_no_jump/blocks_on_no_jump)
