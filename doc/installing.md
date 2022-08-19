
## 安装 Django 

如果您已经安装了 Django，则可以跳过此部分并直接跳转到创建第一个项目部分。Django作为Python包出现，因此可以安装在任何Python环境中。如果您尚未安装Django，以下是安装它以进行本地开发的快速指南。

Django 3 继续提供新功能，同时保持框架的核心功能。 3.0 版本首次包含异步服务器网关接口 (ASGI) 支持，这使得 Django 完全支持异步。 Django 3.0 还包括对 MariaDB 的官方支持、对 PostgreSQL 的新排除约束、过滤器表达式增强、模型字段选择的枚举以及其他新功能。

Django 3.0 支持 Python 3.6、3.7 和 3.8。在本书中的示例中，我们将使用 Python 3.8.2。如果您使用的是Linux或macOS，则可能安装了Python。如果您使用的是Windows，则可以在 https://www.python.org/downloads/windows/ 下载Python安装进程

如果您不确定您的计算机上是否安装了 Python，您可以通过在 shell 中键入 python 来验证这一点。如果您看到类似以下内容，则说明您的计算机上安装了 Python：

```shell
(venv) hairong@sihairong:~/object/django-blog$ python --version
Python 3.10.5
```

如果您安装的 Python 版本低于 3.6，或者您的计算机上没有安装 Python，请从 https://www.python.org/downloads/ 下载 Python 3.8.2 并安装它。

由于您将使用Python 3，因此您不必安装数据库。这个Python版本带有一个内置的SQLite数据库。SQLite是一个轻量级数据库，你可以与Django一起开发。如果计划在生产环境中部署应用进程，则应使用功能齐全的数据库，如 PostgreSQL、MySQL 或 Oracle。你可以在 https://docs.djangoproject.com/ en/3.0/topics/install/#database-install找到更多关于如何使用 Django 运行数据库的信息。


### 创建一个隔离的 Python 环境
从 3.3 版开始，Python 附带了 venv 库，它为创建轻量级虚拟环境提供了支持。每个虚拟环境都有自己的 Python 二进制文档，并且可以在其站点目录中拥有自己独立的一组已安装 Python 包。使用 Python venv 模块创建隔离的 Python 环境允许您为不同的项目使用不同的包版本，这比在系统范围内安装 Python 包实用得多。使用 venv 的另一个优点是您不需要任何管理权限来安装 Python 包

使用以下命令创建隔离环境：
```shell
python -m venv my_venv
```

这将创建一个 my_env/ 目录，包括您的 Python 环境。您在虚拟环境处于活动状态时安装的任何 Python 库都将进入 my_env/lib/python3.8/site-packages 目录。

运行以下命令以激活虚拟环境：
```shell
source my_venv/bin/activate
```

shell 提示符将包含括在括号中的活动虚拟环境的名称，如下所示：
```shell
(venv) hairong@sihairong:~/object/django-blog$
```

您可以随时使用停用命令停用环境。 您可以在 https://docs.python.org/3/ library/venv.html 找到有关venv的更多信息。

### 用 pip 安装 Django
pip包管理系统是安装Django的首选方法。Python 3.8 预装了 pip，但你可以在 https://pip.pypa.io/en/stable/installing/ 找到 pip 安装说明。

在[pypi](https://pypi.org/project/Django/)中查询最新的django版本 

在 shell 提示符下运行以下命令，使用 pip 安装 Django：
```shell
pip install "Django==3.0.*"
```

Django将安装在虚拟环境的Python site-packages/目录中。

现在检查Django是否已成功安装。在终端上运行python，导入Django，查看版本，如下：
```shell
>>> import django
>>> django.get_version()
'3.0.14'
```
如果您得到类似 3.0.X 的输出，则 Django 已成功安装在您的机器上。

## 创建你的第一个项目
