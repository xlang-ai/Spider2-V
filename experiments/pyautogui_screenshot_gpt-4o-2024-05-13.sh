python run_spider2.py --path_to_vm "vm_data/Ubuntu0/Ubuntu0/Ubuntu0.vmx" \
    --snapshot_name "init_state" \
    --observation_space screenshot \
    --action_space pyautogui \
    --model gpt-4o-2024-05-13 \
    --max_tokens 1500 \
    --max_trajectory_length 3 \
    --sleep_after_execution 1 \
    --test_all_meta_path evaluation_examples/test_validated.json # dict path to all tool: [eid1, eid2] data to be tested
    #--proxy # used in Chinese mainland
    #--host 172.16.12.1 # used in Chinse mainland, set to the host ip in LAN with VM
    #--port 58591 # used in Chinse mainland, set to the proxy port in the host
    #--from_scratch # ignore all existing results, run all examples in `test_all_meta_path` from scratch
    #--verbose_instruction # use extra verbose instruction, with step-by-step instruction
    #--headless # run without gui
