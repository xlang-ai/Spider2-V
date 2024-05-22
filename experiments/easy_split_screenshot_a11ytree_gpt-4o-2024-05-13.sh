python run_spider2.py --path_to_vm "/Users/rhythmcao/Virtual Machines.localized/ubuntu.vmwarevm/ubuntu.vmx" \
    --snapshot_name "spider2.0" \
    --observation_space screenshot_a11y_tree \
    --action_space pyautogui \
    --model gpt-4o-2024-05-13 \
    --max_steps 20 \
    --max_tokens 1500 \
    --max_trajectory_length 3 \
    --sleep_after_execution 1 \
    --test_all_meta_path evaluation_examples/test_easy.json \
    --proxy # used in Chinese mainland
    #--from_scratch \
    # --verbose_instruction \
    # --headless \
