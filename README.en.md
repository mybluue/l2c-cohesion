English | [中文](./README.md)

# Automatic Analysis of Chinese Textual Cohesion Features

This project releases the data and codes from the following article:

> Peng, Y., Hu, R., & Wu, J. (2023). Hànyǔ yǔpiān xiánjiē tèzhēng de zìdòng fēnxī hé yìngyòng yánjiū [Automatic analysis and application of cohesion features in Chinese discourse] (in Chinese). Yǔyán wénzì yìngyòng [Applied Linguistics], (1), 114–129. https://doi.org/10.16499/j.cnki.1003-5397.2023.01.009

To facilitate usage for researchers, this project provides two invocation methods: a Command Line Interface (CLI) and a Graphical User Interface (GUI).

## 1. Command Line Interface (CLI)

**Environments**

* Python 3.8.5
* ltp 4.1.5.post2
* numpy 1.21.5
* pandas 1.4.1
* tqdm 4.64.0

**Models**

* The project relies on the [LTP 4.0 Models](https://github.com/HIT-SCIR/ltp/blob/master/MODELS.md). Please download the corresponding version and place it in the `./models` directory.

**Run the codes**

```python
python main.py
```

## 2. Graphical User Interface (GUI)

You can obtain the download link for the **l2c-cohesion** analyzer by filling out the [`Trial Application Form`](https://www.wjx.top/vm/OtWw5Vm.aspx# ).

l2c-cohesion provides client programs for both Windows and MacOS (Arm), supporting the calculation of modern Chinese textual cohesion metrics.

![GUI Screenshot](https://github.com/mybluue/l2c-cohesion/assets/73818220/f9b5649c-3d73-473d-ab50-fa73548801b2)

### 2.1 User Manual

(1) Download the program corresponding to your operating system. After decompression, it can be opened directly without installation. For **Mac OS**, if a prompt regarding an unverified developer appears on the first run, please `Right-click` and select `Open`. For convenience, you can also drag the program to the Mac Applications folder for quick access via `Launchpad`.

(2) Enter text in the text box, or click the `Select File` button to upload `.txt` format files (batch processing of multiple files is supported). To ensure smooth operation, the text box input is limited to a maximum of <b>100,000 characters</b>, and uploaded files are limited to a maximum of <b>1,000,000 characters per file</b>.

(3) Click the `Save File` button to specify the output location for the results. By default, the results are saved as an `.xlsx` spreadsheet file.

(4) Click the `Analyze Metrics` button to run the program. The running progress is displayed in the bottom status bar. The processing speed depends on your system configuration. If processing large-scale corpora, please pay attention to the status bar prompts and be patient. <b>Do not</b> click other buttons while the program is running.

### 2.2 Metric Analysis Results

The metric definitions and extraction methods are derived from Peng et al. (2023), comprising a total of 27 metrics across lexical, grammatical, and topic levels, as shown in the table below:

| Metric                  | Definition                      | Metric               | Definition                          |
| ----------------------- | ------------------------------- | -------------------- | ----------------------------------- |
| local_lexical_cohesion  | Local lexical cohesion          | conj_density         | Conjunction density                 |
| global_lexical_cohesion | Global lexical cohesion         | CN_ratio             | Conjunction-noun ratio              |
| local_noun_cohesion     | Local noun cohesion             | C_NPS                | Conjunctions per sentence           |
| global_noun_cohesion    | Global noun cohesion            | C_TTR                | Conjunction diversity (TTR)         |
| central_sent_num        | Number of central sentences     | subj_density         | Subject density                     |
| central_sent_ratio      | Ratio of central sentences      | subj_TTR             | Subject diversity (TTR)             |
| pron_density            | Pronoun density                 | subj_n_TTR           | Noun-subject diversity (TTR)        |
| PN_ratio                | Pronoun-noun ratio              | subj_p_ratio         | Pronoun-subject ratio               |
| PPN_ratio               | Personal pronoun-noun ratio     | subj_n_ratio         | Noun-subject ratio                  |
| PPP_ratio               | Personal pronoun ratio          | local_subj_cohesion  | Local subject cohesion              |
| PP_TTR                  | Personal pronoun diversity      | global_subj_cohesion | Global subject cohesion             |
| P_TTR                   | Pronoun diversity               | subj_sc_num          | Number of subject semantic classes  |
| P_NPS                   | Pronouns per sentence           | subj_sc_density      | Subject semantic class density      |
| PP_NPS                  | Personal pronouns per sentence  |                      |                                     |

**Note 1:** When inputting text in the text box, all content within the box is treated as a single analysis object. When uploading files, the content of each file is treated as a single analysis object. If you need to analyze multiple texts, please store them in separate `.txt` files.

**Note 2:** Considering the packaged program size and local running speed, the LTP model version used by the l2c-cohesion tool is [v3.4.0](http://ltp.ai/download.html).