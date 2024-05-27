python run_spider2.py --snapshot_name "spider2.0" \
    --observation_space som \
    --action_space pyautogui \
    --model gpt-4o-2024-05-13 \
    --max_tokens 1500 \
    --max_trajectory_length 3 \
    --temperature 0.5 \
    --sleep_after_execution 1 \
    --test_all_meta_path evaluation_examples/test_ablation.json \
    --proxy # used in Chinese mainland
    #--host 172.16.12.1 # used in Chinse mainland, set to the host ip in LAN with VM
    #--port 58591 # used in Chinse mainland, set to the proxy port in the host
    #--headless # run withou gui
