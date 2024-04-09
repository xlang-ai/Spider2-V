from file_sizes_job import file_sizes_job

def test_report_file_tests():
    res = file_sizes_job.execute_in_process()
    assert res.success
    assert res.output_for_node("get_total_file_size") == 68
    assert res.output_for_node("get_max_file_size") == 35

