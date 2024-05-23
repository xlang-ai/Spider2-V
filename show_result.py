import os
from typing import List, Dict

def get_result(action_space, use_model, observation_type, result_dir):
    target_dir = os.path.join(result_dir, action_space, observation_type, use_model)
    if not os.path.exists(target_dir):
        print("New experiment, no result yet.")
        return None

    all_result = []
    domain_result = {}
    all_result_for_analysis = {}

    for domain in os.listdir(target_dir):
        domain_path = os.path.join(target_dir, domain)
        if os.path.isdir(domain_path):
            for example_id in os.listdir(domain_path):
                example_path = os.path.join(domain_path, example_id)
                if os.path.isdir(example_path):
                    if "result.txt" in os.listdir(example_path):
                        # empty all files under example_id
                        if domain not in domain_result:
                            domain_result[domain] = []
                        result = open(os.path.join(example_path, "result.txt"), "r").read()
                        try:
                            domain_result[domain].append(float(result))
                        except:
                            domain_result[domain].append(float(bool(result)))

                        if domain not in all_result_for_analysis:
                            all_result_for_analysis[domain] = {}
                        all_result_for_analysis[domain][example_id] = domain_result[domain][-1]

                        try:
                            result = open(os.path.join(example_path, "result.txt"), "r").read()
                            try:
                                all_result.append(float(result))
                            except:
                                all_result.append(float(bool(result)))
                        except:
                            all_result.append(0.0)

    for domain in domain_result:
        print("Domain:", domain, "Runned:", len(domain_result[domain]), "Success Rate:",
              sum(domain_result[domain]) / len(domain_result[domain]) * 100, "%")

    print(">>>>>>>>>>>>>")
    print("Office", "Success Rate:", sum(
        domain_result["libreoffice_calc"] + domain_result["libreoffice_impress"] + domain_result[
            "libreoffice_writer"]) / len(
        domain_result["libreoffice_calc"] + domain_result["libreoffice_impress"] + domain_result[
            "libreoffice_writer"]) * 100, "%")
    print("Daily", "Success Rate:",
          sum(domain_result["vlc"] + domain_result["thunderbird"] + domain_result["chrome"]) / len(
              domain_result["vlc"] + domain_result["thunderbird"] + domain_result["chrome"]) * 100, "%")
    print("Professional", "Success Rate:", sum(domain_result["gimp"] + domain_result["vs_code"]) / len(
        domain_result["gimp"] + domain_result["vs_code"]) * 100, "%")

    with open(os.path.join(target_dir, "all_result.json"), "w") as f:
        f.write(str(all_result_for_analysis))

    if not all_result:
        print("New experiment, no result yet.")
        return None
    else:
        print("Runned:", len(all_result), "Current Success Rate:", sum(all_result) / len(all_result) * 100, "%")
        return all_result


def get_result_dict_from_dir(result_dir: str) -> Dict[str, Dict[str, float]]:
    """ Given the result directory, return all results under this directory.
    @return:
        {
            "dbt": {
                "8aa9e870-b0c9-5417-be80-03154e83c7a3": 1.0,
                "8ff98608-8e0e-526e-9413-d744554ba708": 0.0
            }
        }
    """
    result_dict = {}
    for tool in os.listdir(result_dir):
        tool_result_dir = os.path.join(result_dir, tool)
        if tool not in result_dict: result_dict[tool] = dict()
        for eid in os.listdir(tool_result_dir):
            example_result_file = os.path.join(tool_result_dir, eid, 'result.txt')
            if os.path.exists(example_result_file) and os.path.isfile(example_result_file):
                with open(example_result_file, 'r') as inf:
                    score = inf.read().strip()
                    try:
                        score = float(score)
                    except:
                        print(f'[ERROR]: when trying to convert result into score for {example_result_file}')
                        continue
                result_dict[tool][eid] = score
    return result_dict


if __name__ == '__main__':
    get_result("pyautogui", "gpt-4-vision-preview", "screenshot", "./results")
