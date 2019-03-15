def average_instr_len_by_result(blocks):
    total_instructions_with_mem_jump = 0
    total_instructions_without_mem_jump = 0
    total_blocks_with_mem_jump = 0
    total_blocks_without_mem_jump = 0
    for block in blocks:
        if block.jumps:
            total_blocks_with_mem_jump += 1
            total_instructions_with_mem_jump += len(block.instructions)
        else:
            total_blocks_without_mem_jump += 1
            total_instructions_without_mem_jump += len(block.instructions)

    return(total_instructions_with_mem_jump, total_instructions_without_mem_jump, total_blocks_with_mem_jump, total_blocks_without_mem_jump)
