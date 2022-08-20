
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

### 运行开发服务器
Django附带了一个轻量级的Web服务器来快速运行你的代码，而无需花时间配置生产服务器。当你运行Django开发服务器时，它会不断检查代码中的更改。它会自动重新加载，使您无需在代码更改后手动重新加载它。但是，它可能不会注意到某些操作，例如向项目添加新文档，因此在这些情况下，您必须手动重新启动服务器。

通过键入项目根文档夹中的以下命令来启动开发服务器：
```shell
python manage.py runserver
```

现在在浏览器中打开 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)。您应该会看到一个页面，说明项目已成功运行，如以下屏幕截图所示：
![](https://upload.wikimedia.org/wikipedia/commons/5/53/Django_2.1_landing_page.png)
前面的屏幕截图表明 Django 正在运行。如果您查看控制台，您将看到浏览器执行的 GET 请求：

每个 HTTP 请求都由开发服务器记录在控制台中。运行开发服务器时发生的任何错误也将显示在控制台中。

您可以在自定义主机和端口上运行 Django 开发服务器，也可以告诉 Django 加载特定的设置文档，如下所示：
```shell
python manage.py runserver 127.0.0.1:8001
```
> 当您必须处理需要不同配置的多个环境时，您可以为每个环境创建不同的设置文档。

请记住，此服务器仅用于开发，不适合生产用途。为了在生产环境中部署Django，您应该使用Web服务器（例如Apache，Gunicorn或uWSGI）将其作为WSGI应用进程运行，或者使用Uvicorn或Daphne等服务器将其作为ASGI应用进程运行。您可以在 https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/ 上找到有关如何使用不同Web服务器部署Django的更多信息。

第 14 章“上线”解释了如何为 Django 项目设置生产环境

### 项目设置
让我们打开 settings.py 文档，并查看项目的配置。 Django在此文档中包含了几个设置，但这些只是所有可用Django设置的一部分。您可以在 https://docs.djangoproject.com/en/3.0/ref/settings/ 查看所有设置及其默认值。

以下设置值得一看：
- DEBUG 是一个布尔值，用于打开和关闭项目的调试模式。如果设置为 True，当您的应用进程抛出未捕获的异常时，Django 将显示详细的错误页面。当您迁移到生产环境时，请记住您必须将其设置为 False。切勿在启用调试的情况下将站点部署到生产环境中，因为您将暴露与项目相关的敏感数据。

- ALLOWED_HOSTS 在调试模式打开或运行测试时不应用。将站点移动到生产环境并将 DEBUG 设置为 False 后，您必须将域/主机添加到此设置中，以允许它为您的 Django 站点提供服务。

- INSTALLED_APPS是您必须为所有项目编辑的设置。此设置告诉Django哪些应用进程在此站点上处于活动状态。默认情况下，Django包括以下应用进程：
    + django.contrib.admin：一个管理站点
    + django.contrib.auth： 默认认证系统
    + django.contrib.contenttypes：处理内容类型的框架
    + django.contrib.sessions：一个会话框架
    + django.contrib.messages：一个消息传递框架
    + django.contrib.staticfiles：管理静态文档的框架

- MIDDLEWARE 是一个列表，其中包含要执行的中间件。

- ROOT_URLCONF 表示定义应用进程的根 URL 模式的 Python 模块。
- DATABASES 是一个字典，其中包含要在项目中使用的所有数据库的设置。必须始终存在默认数据库。默认配置使用 SQLite3 数据库。
- LANGUAGE_CODE定义了此Django站点的默认语言代码。
- USE_TZ 告诉 Django 激活/停用时区支持。 Django 支持时区感知日期时间。当您使用 startproject 管理命令创建新项目时，此设置设置为 True。

如果您对在这里看到的内容不太了解，请不要担心。您将在接下来的章节中学习不同的 Django 设置。

### 项目和应用
在本书中，您将一遍又一遍地遇到术语项目和应用进程。在Django中，一个项目被认为是具有某些设置的Django安装。 应用进程是一组模型、视图、模板和 URL。应用进程与框架交互以提供一些特定的功能，并且可以在各种项目中重用。您可以将项目视为您的网站，其中包含多个应用进程，例如博客，wiki或论坛，这些应用进程也可以由其他项目使用。

下图显示了一个 Django 项目的结构：

![](https://djangobook.com/wp-content/uploads/2022/01/structure_drawing1.png)

### 创建应用进程
现在让我们创建你的第一个Django应用进程。您将从头开始创建一个博客应用进程。从项目的根目录中，运行以下命令：
```shell
python manage.py startapp blog
```

这将创建应用进程的基本结构，如下所示：
+ blog/
    - __init__.py
    - admin.py
    - apps.py
    - migrations/
        - __init__.py
    - models.py
    - tests.py
    - views.py

这些文档如下所示：
- admin.py：这是您注册模型以将它们包含在 Django 管理站点中的位置——使用此站点是可选的。
- apps.py：这包括博客应用进程的主要配置。
- migrations：此目录将包含您的应用进程的数据库迁移。迁移允许 Django 跟踪您的模型更改并相应地同步数据库。
- models.py：这包括应用进程的数据模型;所有Django应用进程都需要有一个 models.py 文档，但这个文档可以留空。
- tests.py：您可以在此处为应用进程添加测试。
- views.py：你的应用进程的逻辑在这里；每个视图接收一个 HTTP 请求，对其进行处理，然后返回一个响应。


## 设计博客数据架构
您将通过为您的博客定义数据模型来开始设计您的博客数据模式。模型是一个 Python 类，它是 django.db.models.Model 的子类，其中每个属性代表一个数据库字段。 Django 将为 models.py 文档中定义的每个模型创建一个表。当你创建一个模型时，Django 会为你提供一个实用的 API 来方便地查询数据库中的对象。

首先，您需要定义一个 Post models。将以下行添加到博客应用进程的 models.py 文档中：
```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
    @Description	:Blog Post DataModels
    ----------
    @Param			:None
    ----------
    @Returns		:None
    '''
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED')
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    class Meat():
        '''
        @Description	:None
        ----------
        @Param			:None
        ----------
        @Returns		:None
        '''
        ordering = ('-publish')

    def __str__(self):
        '''默认返回 title'''
        return self.title
```
这是您的博客文章数据模型。让我们看一下您刚刚为该模型定义的字段：
- title：这是帖子标题的字段。该字段是 CharField，它转换为 SQL 数据库中的一个 VARCHAR 列。

- slug：这是一个用于 URL 的字段。 slug 是一个短标签，只包含字母、数字、下划线或连字符。您将使用 slug 字段为您的博客文章构建漂亮的、对 SEO 友好的 URL。您已将 unique_for_date 参数添加到此字段，以便您可以使用发布日期和 slug 为帖子构建 URL。 Django 将防止多个帖子在给定日期出现相同的 slug。

- author：此字段定义了多对一关系，这意味着每个帖子都由用户编写，用户可以编写任意数量的帖子。对于此字段，Django 将使用相关模型的主键在数据库中创建一个外键。在这种情况下，您依赖于Django身份验证系统的用户模型。on_delete 参数指定删除被引用对象时要采用的行为。这不是Django所特有的;它是一个SQL标准。使用 CASCADE，您可以指定在删除引用的用户时，数据库还将删除所有相关的博客文章。您可以在 https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models 查看所有可能的选项。 ForeignKey.on_delete。使用related_name属性指定反向关系的名称（从“用户”到“发布”）。这将允许您轻松访问相关对象。稍后您将了解有关此内容的更多信息。

- body：这是帖子的正文。此字段是一个文本字段，可转换为 SQL 数据库中的 TEXT 列。

- publish：此日期时间指示发布帖子的时间。您使用 Django 的 timezone now 方法作为默认值。这会以时区感知格式返回当前日期时间。您可以将其视为标准 Python datetime.now 方法的时区感知版本。

- created：此日期时间指示帖子的创建时间。由于您在此处使用auto_now_add，因此在创建对象时将自动保存日期。

- updated：此日期时间表示上次更新帖子的时间。由于您在此处使用 auto_now，因此在保存对象时会自动更新日期。

- status：此字段显示帖子的状态。您使用一个选项参数，因此该字段的值只能设置为给定选项之一。

Django 带有不同类型的字段，可用于定义模型。您可以在 https://docs.djangoproject.com/en/4.0/ref/models/fields/ 找到所有字段类型。

模型中的 Meta 类包含元数据。当您查询数据库时，您告诉 Django 默认按发布字段以降序对结果进行排序。 使用负前缀指定降序。这样，最近发布的帖子将首先显示。

__str__() 方法是对象的默认人类可读表示。 Django 会在很多地方使用它，比如管理站点。

### 激活应用进程
为了让 Django 跟踪您的应用进程并能够为其模型创建数据库表，您必须激活它。为此，请编辑 settings.py 文档并将 blog.apps.BlogConfig 添加到 INSTALLED_APPS 设置中。它应该如下所示：
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig'
]
```

BlogConfig 类是应用进程配置。现在Django知道你的应用进程在这个项目中是活跃的，并且能够加载它的模型。

### 创建和应用迁移
既然您已经为博客文章创建了数据模型，那幺您将需要一个数据库表。 Django 带有一个迁移系统，可以跟踪对模型所做的更改，并使它们能够传播到数据库中。如前所述，migrate 命令为 INSTALLED_APPS 中列出的所有应用进程应用迁移；它将数据库与当前模型和现有迁移同步。

首先，您需要为 Post 模型创建初始迁移。在项目的根目录中，运行以下命令：
```shell
python manage.py makemigrations blog
```

Django刚刚在博客应用进程的迁移目录中创建了0001_initial.py文档。您可以打开该文档以查看迁移的显示方式。 迁移指定对其他迁移的依赖关系，以及在数据库中执行的操作，以将其与模型更改同步。

让我们看一下 Django 将在数据库中执行的 SQL 代码来为您的模型创建表。 sqlmigrate 命令获取迁移名称并返回它们的 SQL 而不执行它。运行以下命令来检查第一次迁移的 SQL 输出：
```shell
 python manage.py sqlmigrate blog 0001
```
 
输出应如下所示：
```shell
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(50) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```
确切的输出取决于您使用的数据库。前面的输出是为 SQLite 生成的。正如您在输出中看到的，Django 通过组合应用进程名称和模型的小写名称 (blog_post) 来生成表名称，但您也可以在模型的 Meta 类中使用db_table 属性。

Django 会自动为每个模型创建一个主键，但您也可以通过在您的模型字段之一中指定 primary_key=True 来覆盖它。默认主键是一个 id 列，它由一个自动递增的整数组成。此列对应于自动添加到模型中的 id 字段。

让我们将数据库与新模型同步。运行以下命令以应用现有迁移：
```shell
python manage.py migrate
```
您刚刚为INSTALLED_APPS中列出的应用进程（包括您的博客应用进程）应用了迁移。应用迁移后，数据库将反映模型的当前状态。

如果您编辑 models.py 文档以添加、删除或更改现有模型的字段，或者如果您添加新模型，则必须使用 makemigrations 命令创建新迁移。迁移将允许 Django 跟踪模型更改。然后，您必须使用 migrate 命令应用它，以使数据库与您的模型保持同步。

### 为模型创建管理站点










