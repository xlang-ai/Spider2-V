import os, time
from typing import List, Dict
from collections import defaultdict
import os, string, json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import matplotlib.pyplot as plt

ALL_DOMAINS = ['excel', 'servicenow', 'jupyter', 'dbt', 'airflow', 'dagster', 'airbyte', 'snowflake', 'bigquery', 'superset', 'metabase']
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1gJNk_ndBTH4tib1gyzLUKRcmDT-z4s5o0CGR8rFsU-g"

# os.environ['http_proxy'] = 'http://127.0.0.1:58591'
# os.environ['https_proxy'] = 'http://127.0.0.1:58591'
CLIENT_SECRETS = 'client_secrets.json'
CREDENTIALS = 'credentials.json'


def print_result_dict(result_dict):
    for tool in result_dict:
        print(f'For {tool}: ', end='')
        value = result_dict[tool]
        if type(value) in [tuple, list]:
            print(f'{len(value)} examples')
        elif type(value) == dict:
            print(', '.join([f'{k} = {v:.2f}' if type(v) == float else f'{k} = {v}' for k, v in value.items()]))
        else: print(result_dict[tool])
    return


class GoogleSheetAPI:

    TOOLS = ['excel', 'servicenow', 'jupyter', 'dbt', 'airflow', 'dagster', 'airbyte', 'snowflake', 'bigquery', 'superset', 'metabase']

    def _get_sheet(self):
        creds = None
        if os.path.exists(CREDENTIALS):
            creds = Credentials.from_authorized_user_file(CREDENTIALS, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRETS, SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(CREDENTIALS, "w") as token:
                token.write(creds.to_json())
        try:
            service = build("sheets", "v4", credentials=creds)
            # Call the Sheets API
            sheet = service.spreadsheets()
        except HttpError as err:
            print(f'HTTPError while getting google sheet: {err}')
        return sheet

    def __init__(self):
        self.sheet = self._get_sheet()


    def get_validated_number(self):
        """ Get the number of validated examples for each tool
        """
        tools = self.TOOLS
        result = {}
        for tool in tools:
            range = f'{tool}!A1:K50' # extract each tool's data
            response = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
            values = response.get("values", [])
            annotated, validated = 0, 0
            # column H, I, K -> Done, Validated, Passed
            for i, row in enumerate(values):
                if i == 0: continue
                done, verbose, passed = '', '', ''
                if len(row) >= 8: done = row[7]
                if len(row) >= 9: verbose = row[8]
                if len(row) >= 11: passed = row[10]
                if done == "✅": annotated += 1
                if done == "✅" and verbose == "✅" and passed == "✅": validated += 1
            result[tool] = {'annotated': annotated, 'validated': validated}
        result['total'] = {'annotated': sum([result[t]['annotated'] for t in tools]), 'validated': sum([result[t]['validated'] for t in tools])}
        return result


    def get_validated_uuids(self, unfinished: bool = False, column_char: str = None, output_file: str = None):
        """ Get the validated uuids for each tool.
        @args:
            unfinished: if True, return the uuids that are annotated and validated but not finished yet (has no result in column `column_char`, e.g., Q)
        @return:
            result: a dict, tool -> list of validated uuids
        """
        tools, result = self.TOOLS, {}
        if unfinished:
            assert column_char is not None, "Must specify column_char when extracting unfinished uuids"
            if len(column_char) == 1:
                column_index = string.ascii_uppercase.index(column_char.upper())
            else:
                first_column_index = string.ascii_uppercase.index(column_char[0]) + 1
                second_column_index = string.ascii_uppercase.index(column_char[1])
                column_index = first_column_index * 26 + second_column_index

        for tool in tools:
            range = f'{tool}!A1:AZ50' # extract each tool's data
            response = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
            values = response.get("values", [])
            validated_uuids = []
            # column H, I, K -> Done, Validated, Passed
            for i, row in enumerate(values):
                if i == 0: continue
                done, verbose, passed = '', '', ''
                if len(row) >= 8: done = row[7]
                if len(row) >= 9: verbose = row[8]
                if len(row) >= 11: passed = row[10]
                if done == "✅" and verbose == "✅" and passed == "✅":
                    if unfinished:
                        if len(row) <= column_index: # not found yet
                            validated_uuids.append(row[0].strip())
                        elif str(row[column_index]).strip() == "": # no result yet
                            validated_uuids.append(row[0].strip())
                    else: validated_uuids.append(row[0].strip())
            result[tool] = validated_uuids
        column = f' in column char {column_char}' if unfinished else ''
        print(f'In total, found {sum([len(result[t]) for t in tools])} validated{" but not finished" if unfinished else ""} uuids' + column)
        if output_file is not None:
            with open(output_file, 'w') as of:
                json.dump(result, of, indent=4, ensure_ascii=False)
            print('Write validated uuids into file:', output_file)
        return result


    def get_result_dict_from_sheet(self, column_char: str):
        print('Aggregated results from Google Sheet is:')
        column_char = column_char.upper()
        if len(column_char) == 1:
            column_index = string.ascii_uppercase.index(column_char)
        else:
            first_column_index = string.ascii_uppercase.index(column_char[0]) + 1
            second_column_index = string.ascii_uppercase.index(column_char[1])
            column_index = first_column_index * 26 + second_column_index
        result_dict = {}
        method = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'dbt!{column_char}1:{column_char}1').execute().get('values', [])[0][0]
        for tool in self.TOOLS:
            data_range = f'{tool}!A1:AZ50'
            response = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=data_range).execute()
            values = response.get("values", [])
            result_dict[tool] = {'total': 0, 'unfinished': 0, 'outliers': 0, 'success': 0, "failed": 0}
            for rid, row in enumerate(values):
                if rid == 0:
                    if len(row) <= column_index:
                        print(f'No method title for {tool} in column {column_char}, which should be {method}')
                        break
                    assert row[column_index] == method, f"Method title for {tool} is {row[column_index]} instead of the desired {method}"
                if len(row) < 8 or row[7] != "✅": # this example is not annotated yet, just skip
                    continue
                result_dict[tool]['total'] += 1
                if len(row) <= column_index or str(row[column_index]) == "": # result not available yet
                    result_dict[tool]['unfinished'] += 1
                    continue
                result = str(row[column_index])
                if result not in ["0", "1"]:
                    print(f'[WARNING]: result for {tool}/{row[0]} and method {method} (column {column_char}) is {result}, neither 0 nor 1')
                    result_dict[tool]['outliers'] += 1
                    continue
                if result == "1":
                    result_dict[tool]['success'] += 1
                else: result_dict[tool]['failed'] += 1
            assert result_dict[tool]['success'] + result_dict[tool]['failed'] == result_dict[tool]['total'] - result_dict[tool]['outliers'] - result_dict[tool]['unfinished']
            count = result_dict[tool]['success'] + result_dict[tool]['failed']
            result_dict[tool]['rate'] = result_dict[tool]['success'] * 100.0 / count if count > 0 else 0.0
            
        total = sum([result_dict[tool]['total'] for tool in result_dict])
        unfinished = sum([result_dict[tool]['unfinished'] for tool in result_dict])
        outliers = sum([result_dict[tool]['outliers'] for tool in result_dict])
        success = sum([result_dict[tool]['success'] for tool in result_dict])
        failed = sum([result_dict[tool]['failed'] for tool in result_dict])
        rate = success * 100.0 / (success + failed) if success + failed > 0 else 0.0
        result_dict['total'] = {'total': total, 'unfinished': unfinished, 'outliers': outliers, 'success': success, 'failed': failed, 'rate': rate}
        print_result_dict(result_dict)
        return result_dict


    def write_result_dict_into_sheet(self, result_dict, column_name: str, column_char: str = "", column_index: int = -1):
        total = sum([len(result_dict[tool]) for tool in result_dict])
        print(f'Start to write {total} result into Google Sheet ...')
        column_char = column_char.upper()
        if column_char != "":
            if column_index >= 0:
                if column_index >= len(string.ascii_uppercase):
                    first_column_index = column_index // 26 - 1
                    second_column_index = column_index % 26
                    exp_column_char = string.ascii_uppercase[first_column_index] + string.ascii_uppercase[second_column_index]
                else: exp_column_char = string.ascii_uppercase[column_index]
                assert exp_column_char == column_char
            else:
                if len(column_char) == 1:
                    column_index = string.ascii_uppercase.index(column_char)
                else:
                    first_column_index = string.ascii_uppercase.index(column_char[0]) + 1
                    second_column_index = string.ascii_uppercase.index(column_char[1])
                    column_index = first_column_index * 26 + second_column_index
        else:
            assert column_index >= 0, "Must specify at least one of column_index or column_char"
            if column_index >= len(string.ascii_uppercase):
                first_column_index = column_index // 26 - 1
                second_column_index = column_index % 26
                column_char = string.ascii_uppercase[first_column_index] + string.ascii_uppercase[second_column_index]
            else: column_char = string.ascii_uppercase[column_index]
        total = 0
        for tool in result_dict:
            data_range = f'{tool}!A1:AZ50' # extract each tool's data
            response = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=data_range).execute()
            values = response.get("values", [])
            tool_result = result_dict[tool]
            cell_pos = {} # uuid -> tuple (tool, row_index, int score)
            # get existing result
            for rid, row in enumerate(values):
                if rid == 0:
                    if len(row) < column_index + 1:
                        # print(f'[ERROR]: please check the sheet for tool {tool}: column_index={column_index} exceeding maximum column numbers')
                        print(f'column {column_char}: "{column_name}" (index={column_index}) not exist yet, create it!')
                        data_range = f'{tool}!{column_char}1:{column_char}1'
                        body = {"values": [[column_name]]}
                        result = self.sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=data_range, valueInputOption='RAW', body=body).execute()
                    else:
                        if row[column_index].strip() != column_name:
                            print(f'[ERROR]: please check the sheet for tool {tool}: column_index={column_index} is not {column_name}')
                            break
                if len(row) == 0: continue
                eid = row[0].strip()
                if eid not in tool_result: continue
                cur_res = row[column_index] if len(row) > column_index else "" # means no value is written yet
                score = tool_result[eid]
                if str(cur_res) == "1" and int(score) == 0:
                    print(f'[WARNING]: {tool} cell for row {rid} and column {column_name} has value 1 already, but new score=0. Just skip !')
                    continue
                if str(cur_res) == "0" and int(score) == 1:
                    print(f'[Attention]: {tool} cell for row {rid} and column {column_name} has value 0 already, but will be updated to score 1.0 !')
                if str(cur_res) == str(int(score)): continue
                cell_pos[eid] = (tool, rid, int(score))
            
            # update result, one data point each time
            for eid in cell_pos:
                tool, rid, score = cell_pos[eid]
                data_range = f'{tool}!{column_char}{rid+1}:{column_char}{rid+1}'
                body = {"values": [[score]]}
                result = self.sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=data_range, valueInputOption='RAW', body=body).execute()
                time.sleep(1)
            total += len(cell_pos)
            # print(f'In total, for tool {tool}, update {len(cell_pos)} result for method {column_name} (in column {column_char})')
        print(f'In total, update {total} result for method {column_name} (in column {column_char})')
        return

class LocalUtilsAPI():

    TOOLS = ['excel', 'servicenow', 'jupyter', 'dbt', 'airflow', 'dagster', 'airbyte', 'snowflake', 'bigquery', 'superset', 'metabase']

    def __init__(self, data_dir: str = 'evaluation_examples/examples', result_dir: str = 'results'):
        self.data_dir = data_dir
        self.result_dir = result_dir

    def check_data_recursively(self, func: callable, error_msg: str = "Check failed"):
        """ Recursively check the data config by calling `func` for each sample.
        @args:
            func: a callable function that takes the data config dict as input and returns a boolean value
            error_msg: a string to print if the function returns False
        """
        for tool in self.TOOLS:
            tool_dir = os.path.join(self.data_dir, tool)
            for eid in os.listdir(tool_dir):
                edir = os.path.join(tool_dir, eid)
                if not os.path.isdir(edir): continue
                fp = os.path.join(edir, f'{eid}.json')
                with open(fp, 'r') as inf:
                    data = json.load(inf)
                if not func(data):
                    print(f'[ERROR]: {error_msg} for {tool}/{eid}')
        return

    def update_data_recursively(self, func: callable):
        """ Recursively update the data config by calling `func` for each sample.
        @args:
            func: a callable function that takes the data config dict as input and returns a new data config dict
        """
        for tool in self.TOOLS:
            tool_dir = os.path.join(self.data_dir, tool)
            for eid in os.listdir(tool_dir):
                edir = os.path.join(tool_dir, eid)
                if not os.path.isdir(edir): continue
                fp = os.path.join(edir, f'{eid}.json')
                with open(fp, 'r') as inf:
                    data = json.load(inf)
                new_data = func(data)
                with open(fp, 'w') as ouf:
                    json.dump(new_data, ouf, indent=4, ensure_ascii=False)
        return

    def get_dataset_statistics(self):
        total = 0
        tags = defaultdict(lambda: 0)
        action_numbers = defaultdict(lambda: {'easy': [], 'medium': [], 'hard': []})
        hardness = lambda x: 'easy' if x <= 5 else 'medium' if x <= 15 else 'hard'
        for tool in self.TOOLS:
            tool_dir = os.path.join(self.data_dir, tool)
            for eid in os.listdir(tool_dir):
                edir = os.path.join(tool_dir, eid)
                if not os.path.isdir(edir): continue
                fp = os.path.join(edir, f'{eid}.json')
                with open(fp, 'r') as inf:
                    data = json.load(inf)
                total += 1
                for t in data['tags']: tags[t] += 1
                level = hardness(data['action_number'])
                action_numbers[tool][level].append(data['action_number'])

        print_result_dict(tags)
        for tool in action_numbers:
            print(f'For {tool}: ', end='')
            count = sum([len(action_numbers[tool][level]) for level in action_numbers[tool]])
            for level in action_numbers[tool]:
                print(f'{level}: {len(action_numbers[tool][level])}|{len(action_numbers[tool][level]) / count * 100: .2f}%, ', end='')
            avg = sum([sum(action_numbers[tool][l]) for l in action_numbers[tool]]) / count
            print(f'average_action_number = {avg:.2f}')
        print('For all tools: ', end='')
        for l in ['easy', 'medium', 'hard']:
            count = sum([len(action_numbers[tool][l]) for tool in action_numbers])
            print(f'{l}: {count}|{count / total * 100:.2f}%, ', end='')
        avg = sum([sum(action_numbers[tool][l]) for l in ['easy', 'medium', 'hard'] for tool in action_numbers]) / total
        print(f'average_action_number = {avg:.2f}')
        print(f'Total number of examples: {total}')
        return action_numbers


    def get_result_dict_from_dir(self, experiment_name: str, include_uuid: bool = True):
        """ Given the result directory, return all results under this directory.
        @return:
            if include_uuid:
            {
                "dbt": {
                    "8aa9e870-b0c9-5417-be80-03154e83c7a3": 1.0,
                    "8ff98608-8e0e-526e-9413-d744554ba708": 0.0
                }
            }
            else:
            {
                "dbt": {
                    "success": 2,
                    "failed": 50,
                    "rate": 4
                }
            }
        """
        result_dict = {}
        result_dir = os.path.join(self.result_dir, experiment_name)
        for tool in os.listdir(result_dir):
            tool_result_dir = os.path.join(result_dir, tool)
            if not os.path.isdir(tool_result_dir): continue
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
        if not include_uuid:
            for tool in result_dict:
                success = sum([1 for eid in result_dict[tool] if int(result_dict[tool][eid]) == 1])
                failed = sum([1 for eid in result_dict[tool] if int(result_dict[tool][eid]) == 0])
                rate = success * 100.0 / (success + failed) if success + failed > 0 else 0.0
                result_dict[tool] = {'success': success, 'failed': failed, 'rate': rate}
            result_dict['total'] = {
                'success': sum([result_dict[tool]['success'] for tool in result_dict]),
                'failed': sum([result_dict[tool]['failed'] for tool in result_dict])
            }
            result_dict['total']['rate'] = result_dict['total']['success'] * 100.0 / (result_dict['total']['success'] + result_dict['total']['failed']) if result_dict['total']['success'] + result_dict['total']['failed'] > 0 else 0.0
        return result_dict

    def compare_result_from_dir(self, *result_dict):
        total = len(result_dict)
        for idx, results in enumerate(result_dict):
            s = set()
            for tool in results:
                for uid in results[tool]:
                    s.add((tool, uid))
            if idx == 0:
                joint = s
            else: joint = joint.intersection(s)
        print('In total, there are', len(joint), 'joint examples')
        for idx, results in enumerate(result_dict):
            res = [results[tool][uid] for (tool, uid) in joint]
            rate = sum(res) * 100.0 / len(res) if len(res) > 0 else 0.0
            print(f'Success rate for result{idx}: {rate:.2f}')
        return

    def filter_examples(self, fp, output_file=None):
        with open(fp, 'r') as inf:
            data = json.load(inf)
        count, new_data = 0, {}
        for tool in data:
            new_data[tool] = []
            if tool == 'excel':
                continue
            for uid in data[tool]:
                config = os.path.join('evaluation_examples', 'examples', tool, uid, f'{uid}.json')
                config = json.load(open(config, 'r'))
                if 'account' in config['tags']: continue
                new_data[tool].append(uid)
                count += 1
        output_file = fp if output_file is None else output_file
        with open(output_file, 'w') as of:
            json.dump(new_data, of, indent=4, ensure_ascii=False)
        print(f'In total, filter {count} from {sum([len(data[tool]) for tool in data])} examples and write to file {output_file}.')
        return

sheet = GoogleSheetAPI()
data = LocalUtilsAPI()

if __name__ == '__main__':

    # get annotated and validated number for each tool from google sheet
    result_dict = sheet.get_validated_number()
    print_result_dict(result_dict)
    exit(0)

    # get validated uuids for each tool from google sheet and write into json file (for experiment)
    # sheet.get_validated_uuids(output_file='evaluation_examples/test_validated.json')
    # only extract unfinished experiment samples according experiment column XX, e.g., S or AA, if unfinished=True, must specify column_char
    # sheet.get_validated_uuids(unfinished=True, column_char='AA', output_file='evaluation_examples/test_unfinished_validated.json')
    # self-customized filter method
    # data.filter_examples('evaluation_examples/test_validated.json', output_file='evaluation_examples/test_ablation.json')
    # exit(0)

    # get aggregated result from local result directory, e.g., results/pyautogui_som_gpt-4o-2024-05-13
    # if you want to write into googlesheet from local result dir, please set include_uuid=True !!!
    # result_dict1 = data.get_result_dict_from_dir(experiment_name='pyautogui_som_gpt-4o-2024-05-13_rag', include_uuid=True)
    # if you want to see aggregated results from local dir, set include_uuid=False
    # print_result_dict(result_dict1)
    # if you want to write into googlesheet from local result dir, please set include_uuid=True !!!
    # result_dict2 = data.get_result_dict_from_dir(experiment_name='pyautogui_som_gpt-4-vision-preview_rag', include_uuid=True)
    # if you want to see aggregated results from local dir, set include_uuid=False
    # print_result_dict(result_dict2)
    # if you want to compare results, set include_uuid=True
    # data.compare_result_from_dir(result_dict1, result_dict2)
    # exit(0)

    # write/update result from result_dict into google sheet, must specify the column name
    # if column name does not exist, it will be created
    # either `column_char` or `column_index` should be provided
    # if cell empty, write result into it; if already 1, not write 0; if already 0, update to 1
    ################### Please be careful when writing data into Google Sheet  ####################
    # sheet.write_result_dict_into_sheet(result_dict1, column_name='rag-pyautogui-som-gpt4o', column_char='AA')
    ################### Please be careful when writing data into Google Sheet  ####################

    # get result from google sheet, this will print aggregated results for column Q on Google sheet
    # sheet.get_result_dict_from_sheet('AA')
    # exit(0)

    def check_data_tool(data: dict) -> bool:
        tool = data['snapshot']
        if tool not in GoogleSheetAPI.TOOLS or (tool not in data['related_apps'] and tool + '-cloud' not in data['related_apps']):
            return False
        else: return True

    # there should be no error message printed if all data are correct
    data.check_data_recursively(check_data_tool, error_msg="Tool consistency check failed")

    def add_data_category(data: dict) -> dict:
        tool = data['snapshot']
        if tool in ['excel', 'jupyter']:
            if 'traditional_data_processing' not in data['tags']:
                data['tags'].append('traditional_data_processing')
        elif tool in ['dbt']:
            if 'data_transformation' not in data['tags']:
                data['tags'].append('data_transformation')
        elif tool in ['dagster', 'airflow']:
            if 'data_orchestration' not in data['tags']:
                data['tags'].append('data_orchestration')
        elif tool in ['airbyte']:
            if 'data_ingestion_and_integration' not in data['tags']:
                data['tags'].append('data_ingestion_and_integration')
        elif tool in ['metabase', 'superset']:
            if 'data_analysis_and_visualization' not in data['tags']:
                data['tags'].append('data_analysis_and_visualization')
        elif tool in ['bigquery', 'snowflake']:
            if 'data_warehousing' not in data['tags']:
                data['tags'].append('data_warehousing')
        elif tool in ['servicenow']:
            if 'it_service_management' not in data['tags']:
                data['tags'].append('it_service_management')
        else:
            raise ValueError(f'Unknown tool {tool}')
        return data

    # add data category for each example
    data.update_data_recursively(add_data_category)

    # calculate some statistics for the dataset
    # data.get_dataset_statistics()
