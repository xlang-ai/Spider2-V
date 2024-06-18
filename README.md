<p align="center">
  <img src="assets/spider2v-overview.png" alt="Spider2-V">
</p>

<p align="center">
  <a href="https://spider2-v.github.io/">Website</a> •
  <a href="https://arxiv.org/abs/">Paper</a> •
  <a href="https://github.com/xlang-ai/Spider2-V/tree/main/evaluation_examples">Data</a> •
  <a href="https://spider2-v.github.io/explorer.html">Data Viewer</a> •
  <!-- <a href="https://discord.gg/4Gnw7eTEZR">Discord</a> -->
</p>

<p align="center">
    <a href="https://img.shields.io/badge/PRs-Welcome-red">
        <img src="https://img.shields.io/badge/PRs-Welcome-red">
    </a>
    <a href="https://img.shields.io/github/last-commit/xlang-ai/Spider2-V?color=green">
        <img src="https://img.shields.io/github/last-commit/xlang-ai/Spider2-V?color=green">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
    </a>
    <!-- <a href="https://badge.fury.io/py/Spider2-V">
        <img src="https://badge.fury.io/py/Spider2-V.svg">
    </a>
    <a href="https://pepy.tech/project/Spider2-V">
        <img src="https://static.pepy.tech/badge/Spider2-V">
    </a> -->
    <br/>
</p>


## 📢 Updates
- 2024-06-20: We released our [paper](https://arxiv.org/abs/), [environment and benchmark](https://github.com/xlang-ai/Spider2-V), and [project page](https://spider2-v.github.io/). Check it out!

## 🏗️ Installation
### 💾 On Your Desktop or Server
The executable environment~(desktop Ubuntu 22.04 LTS) is based on our previous work [OSWord](https://github.com/xlang-ai/OSWorld). Please install the pip dependencies and virtual machine first.

1. First, clone this repository and `cd` into it. Then, install the dependencies listed in `requirements.txt`. It is recommended that you use the latest version of `conda` to manage the environment, but you can also choose to manually install the dependencies. Please ensure that the version of Python is >= 3.11.
```bash
# Clone the Spider2-V repository
git clone https://github.com/xlang-ai/Spider2-V

# Change directory into the cloned repository
cd Spider2-V

# Optional: Create a Conda environment for Spider2-V
conda create -n spider2v python=3.11
conda activate spider2v

# Install required dependencies
pip install -r requirements.txt
```
2. Install [VMware Workstation Pro](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html) (for systems with Apple Chips, you should install [VMware Fusion](https://www.vmware.com/go/getfusion)) and append the `vmrun` command into system path.  The installation process can refer to [How to install VMware Worksation Pro](./INSTALL_VMWARE.md). Verify the successful installation by running the following:
```bash
vmrun -T ws list
```
If the installation along with the environment variable set is successful, you will see the message showing the current running virtual machines.
> **Note:** We will also support using [VirtualBox](https://www.virtualbox.org/) in the near future if you have issues with VMware Pro. However, features such as parallelism and macOS on Apple chips are not supported.

3. Install other dependencies like Playwright.
```bash
playwright install chromium
```
All set! Now, you/agent can interact with the environment via the Quick Start below.

<!-- ### On AWS or Azure (Virtualized platform)
We are working on supporting it 👷. Please hold tight! -->

### 🚀 Quick Start
Run the following minimal example to interact with the environment:
- It will automatically download the prepared virtual machines from [Huggingface](https://huggingface.co/datasets/xlangai/) into `./vm_data`, configure the environment, and take one snapshot called `init_state` for you.
```python
from desktop_env.envs.desktop_env import DesktopEnv

# feel free to change the example!
# task instruction: Help me run all cells in this jupyter notebook. I hope to check the results.
example_path = 'evlauation_examples/examples/jupyter/8ecc0ac2-3083-4be0-ace9-43079288d717/8ecc0ac2-3083-4be0-ace9-43079288d717.json'
with open(example_path, 'r') as infile:
    example = json.load(infile)

env = DesktopEnv(action_space="pyautogui")

obs = env.reset(task_config=example)
print(f'Task instruction: {example["instruction"]}')
obs, reward, done, info = env.step("pyautogui.rightClick()")
input('Now, you can finish the task in the virtual machine manually and Press ENTER to evaluate ...')
score = env.evaluate()
print(f'Evaluation score: {float(score):.1f}')
```
You will see all the logs of the system running normally, including the successful creation of the environment, completion of setup, and successful execution of a `rightClick` action on the screen, which means you are ready to continue.

## 🧪 Experiments
### 🕸️ Different Data Splits
The entire task set contains $494$ examples (`evaluation_examples/test_all.json`) covering $20$ applications. There are different categories to split the entire task set into subsets, depending on:
- whether the task instruction is *verbose* or *abstract* (`evaluation_examples/test_verbose.json` and `evaluation_examples/test_abstract.json`)
- whether a real account is needed (`evaluation_examples/test_account.json` and `evaluation_examples/test_non_account.json`)
- etc.
Note that, a *verbose* instruction means we explicitly tell the agent how to complete the task step-by-step. If you want to test examples which require real accounts (e.g., Snowflake and Google BigQuery), please register relevant accounts and fill credentials into templates under folder `evaluation_examples/settings` first (see [Accounts](ACCOUNT_GUIDELINE.md) for more step-by-step details).

With respect to the task format, see [Task Format](evaluation_examples/README.md#task-format).

### 👷 Human Validation
If you want to check more examples manually in the virtual machine on a GUI screen, which includes:
1. reseting the environment;
2. completing the task in the virtual machine by yourself;
3. invoking the customized evaluation function after completion,
you can run the following interactive script:
- if you do not specify the parameter `--path_to_vm`, the script will automatically find available virtual machines under folder `./vm_data`. If not found, it will download our prepared snapshot from [Huggingface](https://huggingface.co/datasets/xlangai/) into `./vm_data` and use it.
- the snapshot name is default to `init_state`.
- if the `--example` argument is not specified, we will randomly sample one example from `evaluation_examples/test_all.json`
```bash
python run_spider2v_human.py --path_to_vm ./vm_data/Ubuntu0/Ubuntu0/Ubuntu0.vmx --snapshot init_state --example evaluation_examples/test_non_account.json
```

### 💻 Agent Baselines
If you wish to run the baseline agent used in our paper, you can execute the following command as an example under the GPT4-o pure-screenshot setting:

Set **OPENAI_API_KEY** environment variable with your API key
```bash
export OPENAI_API_KEY='changme'
```

```bash
python run_spider2v_agent.py --path_to_vm ./vm_data/Ubuntu0/Ubuntu0/Ubuntu0.vmx --headless --observation_space som --action_space pyautogui --model gpt-4o-2024-05-13 --result_dir ./results
```
The results, which include screenshots, actions, and video recordings of the agent's task completion, will be saved in the `./results` directory in this case. You can then run the following command to obtain the result:
```bash
python show_result.py
```

### Evaluation
Please start by reading through the [agent interface](https://github.com/xlang-ai/OSWorld/blob/main/mm_agents/README.md) and the [environment interface](https://github.com/xlang-ai/OSWorld/blob/main/desktop_env/README.md).
Correctly implement the agent interface and import your customized version in the `run.py` file.
Afterward, you can execute a command similar to the one in the previous section to run the benchmark on your agent.

## ❓ FAQ
### What is the username and password for the virtual machines?
The username and password for the virtual machines are as follows:
- **Ubuntu:** `user` / `password`

### How to setup the account and credentials for Google and Google Drive?

See [Account Guideline](ACCOUNT_GUIDELINE.md)

### How can I configure a proxy for the VM if I'm behind a GFW?

See [Proxy Guideline](PROXY_GUIDELINE.md).

### What are the running times and costs under different settings?
| Setting                        | Expected Time* | Budget Cost (Full Test Set/Small Test Set) |
| ------------------------------ | -------------- | ------------------------------------------ |
| GPT-4V (screenshot)            | 10h            | $100 ($10)                                 |
| Gemini-ProV (screenshot)       | 15h            | $0 ($0)                                    |
| Claude-3 Opus (screenshot)     | 15h            | $150 ($15)                                 |
| GPT-4V (a11y tree, SoM, etc.)  | 30h            | $500 ($50)                                 |

\*No environment parallelism. Calculated in April 2024.

## 📄 Citation
If you find this environment useful, please consider citing our work:
```
@misc{OSWorld,
      title={OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments}, 
      author={Tianbao Xie and Danyang Zhang and Jixuan Chen and Xiaochuan Li and Siheng Zhao and Ruisheng Cao and Toh Jing Hua and Zhoujun Cheng and Dongchan Shin and Fangyu Lei and Yitao Liu and Yiheng Xu and Shuyan Zhou and Silvio Savarese and Caiming Xiong and Victor Zhong and Tao Yu},
      year={2024},
      eprint={2404.07972},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
