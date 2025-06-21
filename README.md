# 汉语语篇衔接特征的自动分析

本项目开源了如下论文所涉及的数据和源码：
This project releases the data and codes from the following articles:

- 彭一平，胡韧奋，吴继峰. 汉语语篇衔接特征的自动分析和应用研究. 语言文字应用. 2023(1).

为了方便研究者的使用，本项目提供了命令行和图形界面两种调用方式。

## 1. 命令行

**环境 (Environments)**

* Python 3.8.5
* ltp 4.1.5.post2
* numpy 1.21.5
* pandas 1.4.1
* tqdm 4.64.0

**模型 (Models)**

* 项目依赖[LTP 4.0 模型](https://github.com/HIT-SCIR/ltp/blob/master/MODELS.md)，请下载相应版本后置于./models

**运行 (Run the codes)**

```python
python main.py
```


## 2. 图形界面

填写[`试用申请`](https://www.wjx.top/vm/OtWw5Vm.aspx# )后可获得l2c-cohesion分析器下载地址。

l2c-cohesion提供了Windows, MacOS (Arm)两种客户端程序，支持现代汉语语篇衔接指标计算。

![f32aaa31a9be2e58a8d798e7b0bbe93](https://github.com/mybluue/l2c-cohesion/assets/73818220/f9b5649c-3d73-473d-ab50-fa73548801b2)


### 2.1 使用说明

(1) 下载系统对应的程序，解压缩后无须安装，直接打开。<b>Mac OS系统 </b>首次运行程序如提示开发者身份未验证，请 `右键`点击 `打开`，为方便后续使用，还可将程序拖至Mac应用程序目录，之后便可通过 `启动台`快捷访问。

(2) 在文本框中输入文本，或者点击 `选择文件`按钮上传txt格式文件，支持上传多个文件进行批量处理。为确保程序运行顺畅，文本框输入限定最长 <b>10万字符 </b>，上传文件限定最长 <b>100万字符/文件 </b>。

(3) 点击 `保存文件`按钮指定结果输出位置，默认结果保存为xlsx格式表格文件。

(4) 点击 `指标分析`按钮运行程序，程序运行进度在底部状态栏显示。程序处理速度与系统配置有关，如需处理较大规模语料，请耐心关注状态栏提示，运行过程中 <b>切勿 </b>点击其他按钮。

### 2.2 指标分析结果

指标定义及抽取方法来自论文彭一平等（2023），包括词汇、语法和话题三个层面共计27个指标，如下表所示：

| 指标                    | 含义             | 指标                 | 含义           |
| ----------------------- | ---------------- | -------------------- | -------------- |
| local_lexical_cohesion  | 局部词汇衔接     | conj_density         | 连词密度       |
| global_lexical_cohesion | 全局词汇衔接     | CN_ratio             | 连词名词比     |
| local_noun_cohesion     | 局部名词衔接     | C_NPS                | 句均连词数量   |
| global_noun_cohesion    | 全局名词衔接     | C_TTR                | 连词多样性     |
| central_sent_num        | 中心句子数量     | subj_density         | 主语密度       |
| central_sent_ratio      | 中心句子比例     | subj_TTR             | 主语多样性     |
| pron_density            | 代词密度         | subj_n_TTR           | 名词主语多样性 |
| PN_ratio                | 代词名词比       | subj_p_ratio         | 代词主语比例   |
| PPN_ratio               | 人称代词名词比   | subj_n_ratio         | 名词主语比例   |
| PPP_ratio               | 人称代词比例     | local_subj_cohesion  | 局部主语衔接   |
| PP_TTR                  | 人称代词多样性   | global_subj_cohesion | 全局主语衔接   |
| P_TTR                   | 代词多样性       | subj_sc_num          | 主语语义类数量 |
| P_NPS                   | 句均代词数量     | subj_sc_density      | 主语语义类密度 |
| PP_NPS                  | 句均人称代词数量 |                      |                |

**注1：** 当用户在文本框中输入时，以框中全部内容为指标分析对象；当用户上传文件时，以每个文件中的内容为一篇分析对象，如需分析多篇文本，请将其分别存储在多个txt文件中。

**注2：** 考虑到打包后程序的大小及其在本地的运行速度，l2c-cohesion工具使用的ltp模型版本为[v3.4.0](http://ltp.ai/download.html)。
