from block_parsing_functions import generate_block, filter_jz_blocks, write_blocks, read_file, create_block_object, generate_unprocessed_block, read_unprocessed_file
from block_analysis_functions import average_instr_len_by_result
from feature_writer import write_features_to_file
from Block import Block

block_files = ['400_perlbench-makerand_pl.txt', '401_bzip2-dryer.txt', '403_gcc_hs-cccp_i.txt', '410-bwaves.txt', '429_mcf-inp_in.txt', '433_milc-su3imp_in.txt', '434_zeusmp.txt', '435_gromacs.txt', '436_cactusADM-benchADM_par.txt', '437_leslie3d-leslie3d_in.txt', '444_namd-namd_input.txt', '445_gobmk-capture_tst.txt', '447_dealII.txt', '450_soplex-test_mps.txt', '453_povray-test_ini.txt', '454_calculix-beampic.txt', '456_hmmer-bombesin_hmm.txt', '458_sjeng_hs-test.txt', '459_GemsFDTD.txt', '462_libquantum_hs-33_5.txt', '464_h264ref_hs-fman_t_enc_bsln_cfg.txt', '465_tonto.txt', '470_lbm.txt', '471_omnetpp-omnetpp_ini.txt', '473_astar-lake_cfg.txt', '482_sphinx3.txt']
for i in range(len(block_files)):
    split = block_files[i].split('.')
    file_heading = split[0]

    file =read_unprocessed_file('../Block_Files/' + file_heading + '.txt')
    #print(file[1])
    blocks = filter_jz_blocks(file)
    write_blocks(blocks,'./Feature_Files/' + file_heading + '_filtered_blocks.txt')
    #print(blocks[0])
    file_blocks = read_file('./Feature_Files/' + file_heading + '_filtered_blocks.txt')
    blocks = []

    num_blocks = len(file_blocks)
    total_instructions = 0

    for block in file_blocks:
        total_instructions += len(block) - 2

    print("Total blocks: ", num_blocks)
    print("Instructions per block:", total_instructions/num_blocks)
    for block in file_blocks:
        blocks.append(create_block_object(block))

    #blocks[2].print_block()

    write_features_to_file('./Feature_Files/' + file_heading + '_features.txt', blocks)

    (instr_on_jump, instr_on_no_jump, blocks_on_jump, blocks_on_no_jump) = average_instr_len_by_result(blocks)
    print(instr_on_jump, instr_on_no_jump, blocks_on_jump, blocks_on_no_jump)


    print("Instructions Per Jump:",instr_on_jump/blocks_on_jump)
    print("Instructions per no jump", instr_on_no_jump/blocks_on_no_jump)
