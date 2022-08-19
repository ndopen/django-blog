
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
我们的第一个Django项目将构建一个完整的博客。Django提供了一个命令，允许您创建一个初始项目文档结构。从 shell 运行以下命令
```shell
django-admin startproject mysite .
```
这将创建一个名为mysite的Django项目。

这些文档如下所示：
- manage.py：这是一个用于与项目交互的命令行实用工具。 它是 django-admin.py 工具周围的薄包装。您无需编辑此文档。

- mysite/：这是您的项目目录，由以下文档组成：
    - __init__.py：一个空文档，告诉 Python 将 mysite 目录视为 Python 模块。
    - asgi.py：这是将项目作为 ASGI 运行的配置，ASGI 是用于异步 Web 服务器和应用进程的新兴 Python 标准。
    - settings.py：这表明您的项目的设置和配置，并包含初始默认设置。
    - urls.py：这是您的 URL 模式所在的地方。此处定义的每个 URL 都映射到一个视图。
    - wsgi.py：这是将项目作为 Web 服务器网关接口 （WSGI） 应用进程运行的配置。

生成的 settings.py 文档包含项目设置，包括使用 SQLite3 数据库的基本配置和名为 INSTALLED_APPS 的列表，其中包含默认情况下添加到项目中的常见 Django 应用进程。 稍后我们将在“项目设置”部分中介绍这些应用进程。

Django 应用进程包含一个 models.py 文档，其中定义了数据模型。每个数据模型都映射到一个数据库表。要完成项目设置，您需要创建与 INSTALLED_APPS 中列出的应用进程模型关联的表。 Django 包含一个管理这个的迁移系统。

打开 shell 并运行以下命令：
```shell
(venv) hairong@sihairong:~/object/django-blog$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

前面几行是 Django 应用的数据库迁移。通过应用迁移，初始应用进程的表在数据库中创建。您将在本章的创建和应用迁移部分了解迁移管理命令。

