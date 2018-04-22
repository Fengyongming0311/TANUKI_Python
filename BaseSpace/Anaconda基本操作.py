查看API文档

python -m pydoc -p 4895

-p 4895   为设置的端口号


Anaconda Navigtor ：用于管理工具包和环境的图形用户界面，后续涉及的众多管理命令也可以在 Navigator 中手工实现。

Jupyter notebook ：基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。

qtconsole ：一个可执行 IPython 的仿终端图形界面程序，相比 Python Shell 界面，qtconsole 可以直接显示代码生成的图形，实现多行代码输入执行，以及内置许多有用的功能和函数。

spyder ：一个使用Python语言、跨平台的、科学运算集成开发环境。


####################################################################
对所有工具包进行升级，以避免可能发生的错误。
conda upgrade --all

在终端询问是否安装如下升级版本时，输入 y。


========================
安装一个 package：
conda install package_name


同时安装多个包，比如同时安装numpy 、scipy 和 pandas，则执行如下命令：
conda install numpy scipy pandas



指定安装的版本，比如安装 1.1 版本的 numpy ：
conda install numpy=1.10


移除一个 package：
conda remove package_name


升级 package 版本：
conda update package_name



查看所有的 packages：
conda list


如果你记不清 package 的具体名称，也可以进行模糊查询：
conda  search search_term





======================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++
管理Python环境
conda create -n env_name  list of packages

其中 -n 代表 name，env_name 是需要创建的环境名称，list of packages 则是列出在新环境中需要安装的工具包。

例如，当我安装了 Python3 版本的 Anaconda 后，默认的 root 环境自然是 Python3，但是我还需要创建一个 Python 2 的环境来运行旧版本的 Python 代码，最好还安装了 pandas 包，于是我们运行以下命令来创建：

conda create -n py2 python=2.7 pandas


细心的你一定会发现，py2 环境中不仅安装了 pandas，还安装了 numpy 等一系列 packages，这就是使用 conda 的方便之处，它会自动为你安装相应的依赖包，而不需要你一个个手动安装。

进入名为 env_name 的环境：

source activate env_name

退出当前环境：

source deactivate



另外注意，在 Windows 系统中，使用 activate env_name 和 deactivate 来进入和退出某个环境。

删除名为 env_name 的环境：

conda env remove -n env_name


显示所有的环境：
conda env list


当分享代码的时候，同时也需要将运行环境分享给大家，执行如下命令可以将当前环境下的 package 信息存入名为 environment 的 YAML 文件中。
conda env export > environment.yaml


同样，当执行他人的代码时，也需要配置相应的环境。这时你可以用对方分享的 YAML 文件来创建一摸一样的运行环境。
conda env create -f environment.yaml




# 更新conda，保持conda最新
conda update conda

# 更新anaconda
conda update anaconda

# 更新python
conda update python



###################################
在pycharm中配置anaconda的解释器

具体做法是：File->Default settings->Default project->project interpreter

接着点击 project interpreter 的右边的小齿轮，选择 add local ，选择anaconda文件路径下的python.exe。接着pycharm会更新解释器，导入模块等，要稍等一点时间。

好了，到目前为止，anaconda在pycharm中的配置就基本完成了。难道我们就要满足使用conda中的那些包了吗？并不是，conda为我们带来了更多的东西，使我们在管理Python库的时候更加方便快捷！接下来就让我来详细为你解说一下吧！











