# 构建博客应用程序

## 1. 安装 Django 

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


### 1.1 创建一个隔离的 Python 环境
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

### 1.2 用 pip 安装 Django
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

## 2. 创建你的第一个项目
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
    - urls.py：这是您的 URL 所在的地方。此处定义的每个 URL 都映射到一个视图。
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

### 2.1 运行开发服务器
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

### 2.2 项目设置
让我们打开 settings.py 文档，并查看项目的配置。 Django在此文档中包含了几个设置，但这些只是所有可用Django设置的一部分。您可以在 https://docs.djangoproject.com/en/3.0/ref/settings/ 查看所有设置及其默认值。

以下设置值得一看：
- DEBUG 是一个布尔值，用于打开和关闭项目的调试。如果设置为 True，当您的应用进程抛出未捕获的异常时，Django 将显示详细的错误页面。当您迁移到生产环境时，请记住您必须将其设置为 False。切勿在启用调试的情况下将站点部署到生产环境中，因为您将暴露与项目相关的敏感数据。

- ALLOWED_HOSTS 在调试打开或运行测试时不应用。将站点移动到生产环境并将 DEBUG 设置为 False 后，您必须将域/主机添加到此设置中，以允许它为您的 Django 站点提供服务。

- INSTALLED_APPS是您必须为所有项目编辑的设置。此设置告诉Django哪些应用进程在此站点上处于活动状态。默认情况下，Django包括以下应用进程：
    + django.contrib.admin：一个管理站点
    + django.contrib.auth： 默认认证系统
    + django.contrib.contenttypes：处理内容类型的框架
    + django.contrib.sessions：一个会话框架
    + django.contrib.messages：一个消息传递框架
    + django.contrib.staticfiles：管理静态文档的框架

- MIDDLEWARE 是一个列表，其中包含要执行的中间件。

- ROOT_URLCONF 表示定义应用进程的根 URL 的 Python 模块。
- DATABASES 是一个字典，其中包含要在项目中使用的所有数据库的设置。必须始终存在默认数据库。默认配置使用 SQLite3 数据库。
- LANGUAGE_CODE定义了此Django站点的默认语言代码。
- USE_TZ 告诉 Django 激活/停用时区支持。 Django 支持时区感知日期时间。当您使用 startproject 管理命令创建新项目时，此设置设置为 True。

如果您对在这里看到的内容不太了解，请不要担心。您将在接下来的章节中学习不同的 Django 设置。

### 2.3 项目和应用
在本书中，您将一遍又一遍地遇到术语项目和应用进程。在Django中，一个项目被认为是具有某些设置的Django安装。 应用进程是一组模型、视图、模板和 URL。应用进程与框架交互以提供一些特定的功能，并且可以在各种项目中重用。您可以将项目视为您的网站，其中包含多个应用进程，例如博客，wiki或论坛，这些应用进程也可以由其他项目使用。

下图显示了一个 Django 项目的结构：

![](https://djangobook.com/wp-content/uploads/2022/01/structure_drawing1.png)

### 2.4 创建应用进程
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


## 3. 设计博客数据架构
您将通过为您的博客定义数据模型来开始设计您的博客数据。模型是一个 Python 类，它是 django.db.models.Model 的子类，其中每个属性代表一个数据库字段。 Django 将为 models.py 文档中定义的每个模型创建一个表。当你创建一个模型时，Django 会为你提供一个实用的 API 来方便地查询数据库中的对象。

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

### 3.1 激活应用进程
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

### 3.2 创建和应用迁移
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

## 4. 为模型创建管理站点
现在您已经定义了帖子模型，您将创建一个简单的管理站点来管理您的博客帖子。 Django 带有一个内置的管理界面，对于编辑内容非常有用。 Django 站点是通过读取模型元数据并提供可用于编辑内容的生产就绪界面来动态构建的。您可以开箱即用地使用它，配置您希望模型在其中显示的方式。

django.contrib.admin 应用进程已包含在 INSTALLED_APPS 设置中，因此您无需添加它。

### 4.1 创建超级用户
首先，您需要创建一个用户来管理管理网站。运行以下命令：
```shell
python manage.py createsuperuser
```

您将看到以下输出;输入所需的用户名、电子邮件和密码，如下所示：
```shell
Username (leave blank to use 'hairong'): admin
Email address: admin@admin.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

### 4.2 Django 管理站点

现在使用 python manage.py runserver 命令启动开发服务器，并在浏览器中打开 http://127.0.0.1:8000/admin/。您应该会看到管理登录页面，如以下屏幕截图所示：
![](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_home.png)

使用您在上一步中创建的用户的凭据登录。您将看到管理网站索引页，如以下屏幕截图所示：

您可以在前面的屏幕截图中看到的组和用户模型是位于 django.contrib.auth 中的 Django 身份验证框架的一部分。如果单击“用户”，您将看到之前创建的用户。

### 4.5将模型添加到管理站点
让我们将博客模型添加到管理站点。编辑博客应用进程的 admin.py 文档，使其如下所示：
```python
from django.contrib import admin
from blog.models import Post
# Register your models here.
admin.site.register(Post)
```
现在，在浏览器中重新加载管理网站。您应该会在网站上看到您的帖子模型，如下所示：
![](https://cloud.sihairong.net/s/gK4P593PoQtDL8g/preview)

这很容易，对吧？当您在Django管理站点中注册模型时，您将获得一个用户友好的界面，该界面通过内省模型生成，允许您以简单的方式列出，编辑，创建和删除对象。

单击帖子旁边的添加链接以添加新帖子。您将注意到 Django 为您的模型动态生成的表单，如以下屏幕截图所示：
![](https://cloud.sihairong.net/s/mYZGAYB4H6W7Wir/preview)

Django 为每种类型的字段使用不同的表单小部件。即使是复杂的字段，例如 DateTimeField，也可以通过简单的界面（例如 JavaScript 日期选择器）显示。

填写表格，然后单击“保存”按钮。您应该被重定向到帖子列表页面，其中包含成功消息和您刚刚创建的帖子，如以下屏幕截图所示：
![](https://cloud.sihairong.net/s/jxcHMMLT4xYZ6gj/preview)

### 4.6 自定义模型的显示方式
现在，我们将看看如何自定义管理站点。编辑您的博客应用进程的 admin.py 文档并进行更改，如下所示：
```python
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
```

您正在告诉 Django 管理站点，您的模型是使用从 ModelAdmin 继承的自定义类在站点中注册的。在此类中，可以包含有关如何在站点中显示模型以及如何与模型交互的信息。

list_display 属性允许您设置要在管理对象列表页面上显示的模型字段。 @admin.register() 装饰器执行与您替换的 admin.site.register() 函数相同的功能，注册它装饰的 ModelAdmin 类。

让我们使用以下代码为管理模型添加更多选项：
```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')
    prepopulated_fields = {'slug' : ('title',)}
```

返回浏览器并重新加载帖子列表页面。现在，它看起来像这样：
![](https://cloud.sihairong.net/s/7Nbe7DGWonAJWbj/preview)

您可以看到帖子列表页面上显示的字段是您在 list_display 属性中指定的字段。列表页面现在包含一个右侧栏，允许您按 list_filter 属性中包含的字段过滤结果。

页面上出现了一个搜索栏。这是因为您已使用 search_fields 属性定义了可搜索字段的列表。在搜索栏的正下方，有导航链接可以在日期层次结构中导航;这已由 date_hierarchy 属性定义。您还可以看到，默认情况下，帖子按“状态”和“发布”列排序。您已使用排序属性指定了默认排序条件。

接下来，单击“添加 POST”链接。您还将在此处注意到一些更改。当您键入新帖子的标题时，系统会自动填充辅助信息域。您已经告诉 Django 使用 prepopulated_fields 属性使用 title 字段的输入来预填充 slug 字段。

此外，作者字段现在显示有一个查找小部件，当您拥有数千名用户时，该小部件可以比下拉选择输入更好地扩展。这是通过 raw_id_fields 属性实现的;

只需几行代码，即可自定义模型在管理站点上的显示方式。有很多方法可以自定义和扩展Django管理站点;您将在本书的后面部分了解更多有关此内容的信息。

## 5. 使用查询集和管理器
现在，您已经拥有了一个功能齐全的管理网站来管理博客的内容，现在是时候学习如何从数据库中检索信息并与之交互了。Django附带了一个强大的数据库抽象API，可让您轻松创建，检索，更新和删除对象。Django对象关系映射器（ORM）与MySQL，PostgreSQL，SQLite，Oracle和MariaDB兼容。 请记住，您可以在项目 settings.py 文档的“数据库”设置中定义项目的数据库。Django可以一次处理多个数据库，你可以对数据库路由器进行编程以创建自定义路由方案。

一旦你创建了数据模型，Django 会为你提供一个免费的 API 来与它们交互。您可以在 https://docs.djangoproject.com/en/4.0/ref/models/ 找到官方文档的数据模型参考。

Django ORM 基于查询集。 QuerySet 是用于从数据库中检索对象的数据库查询集合。您可以将过滤器应用于 QuerySet，以根据给定参数缩小查询结果的范围。

### 5.1 创建对象
打开终端并运行以下命令以打开 Python shell：
```shell
python manage.py shell
```

Then, type the following lines:
```shell
>>> from blog.models import *
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username = 'admin')
>>> post = Post(title = 'shell save blog', body='post body', slug='shellblog', author=user)
>>> post.save()
```

让我们分析一下这段代码的作用。首先，您使用用户名 admin 检索用户对象：
```shell
 User.objects.get(username = 'admin')
```
get（） 方法允许您从数据库中检索单个对象。请注意，此方法需要与查询匹配的结果。如果数据库未返回任何结果，则此方法将引发“不存在”异常，如果数据库返回多个结果，则会引发“多对象返回”异常。这两个异常都是对其执行查询的模型类的属性。

然后，您创建一个带有title、slug 和 body 的 Post 实例，并将您之前检索到的用户设置为Post的author：
```python
Post(title = 'shell save blog', body='post body', slug='shellblog', author=user)
```

最后，使用 save() 方法将 Post 对象保存到数据库：
```python
post.save()
```

前面的操作在后台执行 INSERT SQL 语句。您已经了解了如何先在内存中创建对象，然后将其持久化到数据库中，但您也可以使用 create() 方法通过单个操作创建对象并将其持久化到数据库中，如下所示：
```python
Post.objects.create(title='create function', slug = 'function', body='used django Api createFunction', author=user)
```

### 5.2 更新对象
现在，将帖子的标题更改为其他名称，然后再次保存对象：
```shell
>>> post.title = 'New Title'
>>> post.save()
```
这一次，save（） 方法执行 UPDATE SQL 语句。

### 5.3 检索对象
您已经知道如何使用 get（） 方法从数据库中检索单个对象。您使用 Post.objects.get（） 访问了此方法。每个 Django 模型至少有一个管理器，默认管理器称为对象。您可以使用模型管理器获取查询集对象。要从表中检索所有对象，只需在默认对象管理器上使用 all（） 方法，如下所示：
```shell
>>> postsAll = Post.objects.all()
```
这就是创建返回数据库中所有对象的 QuerySet 的方式。请注意，此 QuerySet 尚未执行。 Django QuerySets 是惰性的，这意味着它们仅在被迫时才被评估。这种行为使 QuerySets 非常高效。如果不将 QuerySet 设置为变量，而是直接在 Python shell 上编写，则会执行 QuerySet 的 SQL 语句，因为你强制它输出结果：
```shell
>>> postsAll  
<QuerySet [<Post: Field options>, <Post: blank>, <Post: choices>, <Post: New Title>, <Post: create function>]>
```

#### 5.3.1 使用 filter（） 方法
若要筛选查询集，可以使用管理器的 filter（） 方法。例如，您可以使用以下查询集检索 2020 年发布的所有帖子：
```python
Post.objects.filter(publish__year=2022)
```

您还可以按多个字段进行过滤。例如，您可以使用用户名 admin 检索作者在 2020 年发布的所有帖子：
```python
Post.objects.filter(publish__year=2022, author__username="hairong")
```

这等同于构建链接多个过滤器的相同 QuerySet：
```python
Post.objects.filter(publish__year=2022).filter(author__username="admin")
```

> 具有字段查找方法的查询使用两个下划线构建，例如，publish__year，但相同的符号也用于访问相关模型的字段，例如 author__username。

#### 5.3.2 使用 exclude（）
您可以使用管理器的 exclude（） 方法从查询集中排除某些结果。例如，您可以检索 2020 年发布的所有帖子，其标题不以“New”开头：
```python
Post.objects.filter(publish__year=2022).exclude(title__startswith='new')
```

#### 5.3.3 使用 order_by（）
您可以使用管理器的 order_by（） 方法按不同字段对结果进行排序。例如，您可以检索按标题排序的所有对象，如下所示：
```python
Post.objects.order_by('title')
```

隐含升序。您可以使用负号前缀指示降序，如下所示：
```python
Post.objects.order_by('-publish')
```

### 5.4 删除对象
如果要删除对象，可以使用 delete() 方法从对象实例中执行：
```python
posts = Post.objects.get(id=2)
posts.delete()
```
> 请注意，删除对象还将删除定义为 on_delete 设置为 CASCADE 的 ForeignKey 对象的任何依赖关系。


### 5.5 当查询集被评估时
在评估之前，创​​建 QuerySet 不涉及任何数据库活动。 QuerySet 通常返回另一个未计算的 QuerySet。您可以将任意数量的过滤器连接到 QuerySet，并且在评估 QuerySet 之前不会访问数据库。在评估 QuerySet 时，它会转换为对数据库的 SQL 查询。

QuerySet 仅在以下情况下进行评估：
- 第一次迭代它们时
- 当你对它们进行切片时，例如Post.objects.all（）[：3]
- 当您腌制或缓存它们时
- 当您在它们上调用 repr（） 或 len（） 时
- 当您在它们上显式调用 list() 时
- 当您在语句中测试它们时，例如 bool（），或，and，或 if

### 5.6 创建模型管理器
正如我之前提到的，`objects` 是检索数据库中所有对象的每个模型的默认管理器。但是，您也可以为模型定义自定义管理器。您将创建一个自定义管理器来检索具有已发布状态的所有帖子。

有两种方法可以为模型添加或自定义管理器：可以向现有管理器添加额外的管理器方法，或者通过修改管理器返回的初始 QuerySet 来创建新管理器。第一种方法为您提供 QuerySet API，如 Post.objects.my_manager（），后者为您提供 Post.my_manager.all（）。模型管理器将允许您使用Post.published.all（）检索帖子。

编辑您的博客应用进程的 models.py 文档以添加自定义管理器：
```python
class PublisedManager(models.Manager):
    '''定义published 模型管理方法，返回贴文状态为发布的对象'''
    def get_queryset(self):
        return super(PublisedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):
    objects = models.Manager()
    published = PublisedManager()

    ...
```

模型中声明的第一个管理器成为默认管理器。您可以使用 Meta 属性 default_manager_name 来指定不同的默认管理器。如果模型中没有定义管理器，Django 会自动为其创建对象默认管理器。如果您为模型声明了任何管理器，但还想保留对象管理器，则必须将其显式添加到模型中。在上述代码中，您将默认对象管理器和已发布的自定义管理器添加到 Post 模型。

管理器的 `get_queryset（）` 方法返回将要执行的查询集。重写此方法以将自定义筛选器包含在最终的查询集中。

您现在已经定义了自定义管理器并将其添加到 Post 模型中；您可以使用它来执行查询。让我们测试一下。

使用以下命令再次启动开发服务器：
```shell
python manage.py shell
```

现在，您可以导入 Post 模型并检索标题以 Who 开头的所有已发布帖子，执行以下 QuerySet：
```python
from blog.models import Post
Post.published.filter(title__startswith='Who')
```

若要获取此查询集的结果，请确保在标题以“谁”开头的 Post 对象中将已发布的字段设置为 True。

## 6. 构建List和PostDetail视图
现在，您已经了解了如何使用 ORM，接下来就可以构建博客应用的视图了。Django Views只是一个Python函数，它接收Web请求并返回Web响应。返回所需响应的所有逻辑都位于视图内部。

首先，您将创建应用进程视图，然后为每个视图定义一个 URL ，最后，您将创建 HTML 模板来呈现视图生成的数据。每个视图都会渲染一个模板，将变量传递给它，并返回一个带有渲染输出的 HTTP 响应。

### 6.1 创建List和detail视图
让我们首先创建一个视图来显示帖子列表。编辑您的博客应用进程的 views.py 文档，使其如下所示：
```python
from django.shortcuts import render
from blog.models import Post

def post_list(request):
    '''post list 视图方法，返回已发布所有posts'''
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
```

您刚刚创建了您的第一个 Django 视图。 post_list 视图将`request`对象作为唯一参数。所有视图都需要此参数。在此视图中，您使用之前创建的`PostManager`检索具有已发布状态的所有帖子。

最后，您使用 Django 提供的 render() 快捷方式来呈现具有给定模板的帖子列表。此函数采用请求对象、模板路径和上下文变量来呈现给定的模板。它返回一个带有渲染文本（通常是 HTML 代码）的 HttpResponse 对象。 render() 快捷方式将请求上下文考虑在内，因此模板上下文处理器设置的任何变量都可以由给定模板访问。模板上下文处理器只是将变量设置到上下文中的可调用对象。您将在第 3 章，扩展您的博客应用进程中学习如何使用它们。

让我们创建第二个视图来显示单个帖子。将以下函数添加到 views.py 文档中：
```python
def post_detail(request, post, year, month, day):
    '''post detail 视图，返回请求条件相符合的Post'''
    posts = get_object_or_404(Post, slug = post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'posts' : posts})
```

这是帖子详细信息视图。此视图采用年、月、日和帖子参数来检索具有给定辅助信息区和日期的已发布帖子。请注意，在创建 Post 模型时，已将 unique_for_date 参数添加到辅助信息域。这可确保在给定日期内只有一个帖子具有辅助信息交换，因此，您可以使用日期和数据域来检索单个信息。在详细信息视图中，使用 get_object_or_404（） 快捷方式检索所需的帖子。此函数检索与给定参数匹配的对象，如果未找到任何对象，则检索 HTTP 404（未找到）异常。最后，使用 render（） 快捷方式通过模板呈现检索到的帖子。

### 6.2 为您的视图添加 URL
URL 允许您将 URL 映射到视图。URL 由字符串、视图和允许您在项目范围内命名 URL 的名称（可选）组成。Django贯穿每个URL，并在与请求的URL匹配的第一个处停止。然后，Django 导入匹配的 URL 的视图并执行它，传递 HttpRequest 类的实例和关键字或位置参数。

在博客应用进程的目录中创建一个 urls.py 文档，并在其中添加以下行：
```python
from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    # post urls
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')    
]
```

在上面的代码中，使用 app_name 变量定义应用进程命名空间。这允许您按应用进程组织 URL，并在引用它们时使用该名称。您可以使用 path（） 函数定义两种不同的。第一个 URL 不采用任何参数，并映射到post_list视图。 第二个采用以下四个参数，并映射到post_详细信息视图：
- year：需要一个整数
- month：需要一个整数 
- day：需要一个整数 
- post：可以由单词和连字符组成

您使用尖括号从 URL 中捕获值。在 URL 中指定为 &amp;lt;parameter&amp;gt; 的任何值被捕获为字符串。您使用路径转换器，例如 &amp;lt;int:year&amp;gt;，专门匹配并返回一个整数和 &amp;lt;slug:post&amp;gt;专门匹配一个蛞蝓。您可以在 https://docs.djangoproject.com/en/4.0/topics/http/urls/#path-converters 查看 Django 提供的所有路径转换器。

如果使用 path() 和转换器对您来说还不够，您可以使用 re_path() 来使用 Python 正则表达式定义复杂的 URL 。您可以在 https://docs 了解有关使用正则表达式定义 URL 的更多信息。 djangoproject.com/en/4.0/ref/urls/#django.urls.re_path。如果您以前没有使用过正则表达式，您可能需要查看位于 https://docs.python.org/3/howto/regex 的正则表达式 HOWTO。首先是html。

> 为每个应用进程创建一个 urls.py 文档是使应用进程可由其他项目重用的最佳方式。

接下来，您必须在项目的主 URL 中包含博客应用进程的 URL 。

编辑位于项目的 mysite 目录中的 urls.py 文档，使其如下所示：
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
```

用 include 定义的新 URL 是指在博客应用进程中定义的 URL ，以便它们包含在 blog/path 下。您可以在命名空间博客下包含这些。命名空间在整个项目中必须是唯一的。稍后，您将使用命名空间，后跟冒号和 URL 名称（例如，blog：post_list 和 blog：post_detail）轻松引用您的博客 URL。有关 URL 命名空间的详细信息，请参阅 https:// docs.djangoproject.com/en/4.0/topics/http/urls/#url-namespaces。

### 6.3 模型中规范 URL
规范 URL 是资源的首选 URL。您的站点中可能有不同的页面用于显示帖子，但只有一个 URL 可用作博客帖子的主 URL。 Django 中的约定是将 `get_absolute_url()` 方法添加到返回对象的规范 URL 的模型中。

您可以使用您在上一节中定义的 post_detail URL 来构建 Post 对象的规范 URL。对于此方法，您将使用 reverse() 方法，该方法允许您按名称构建 URL 并传递可选参数。您可以在 https://docs.djangoproject.com/en/4.0/ref/urlresolvers/ 了解有关 URL 实用进程功能的更多信息。

编辑博客应用的models.py文档，添加如下代码：
```python
from django.urls import reverse
def get_absolute_url(self):
        '''规范绝对url'''
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug]) 
```
您将在模板中使用 get_absolute_url（） 方法链接到特定帖子。


## 7. 为您的视图创建模板
您已经为博客应用进程创建了视图和 URLS。 URLs 将 URL 映射到视图，视图决定将哪些数据返回给用户。模板定义了数据的显示方式；它们通常是结合 Django 模板语言用 HTML 编写的。您可以在 https://docs.djangoproject.com/en/4.0/ref/templates/language/ 找到有关 Django 模板语言的更多信息。

让我们将模板添加到您的应用中，以便以用户友好的方式显示帖子。

在您的博客应用目录中创建以下目录和文档：
+ blog/
    - templates/
        - blog/
            - base.html
            - post/
                - list.html
                - detail.html

前面的结构将是您的模板的文档结构。 base.html 文档将包含网站的主要 HTML 结构，并将内容分为主要内容区域和侧边栏。 list.html 和 detail.html 文档将从 base.html 文档继承以分别呈现博客文章列表和详细视图。

Django 具有强大的模板语言，允许您指定数据的显示方式。它基于模板标签、模板变量和模板过滤器：
- 模板标签控制模板的呈现，看起来像 {% tag %}
- 模板变量在呈现模板时被替换为值，并且看起来像 {{ variable }}
- 模板过滤器允许您修改要显示的变量，看起来像{{ variable|filter}}。

您可以在 https://docs.djangoprojectcom/en/4.0/ref/templates/builtins/ 查看所有内置模板标签和过滤器。

编辑 base.html 文档并添加以下代码：
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
</head>
<body>
    <div id='content'>
        {% block content %}
        {% endblock  %}
    </div>

    <div id='sidebar'> 
        <h2>My Blog</h2>
        <p>
            this is my blog
        </p>
    </div>
</body>
</html>
```

{% load static %} 告诉 Django 加载 django.contrib.staticfiles 应用进程提供的静态模板标签，该应用进程包含在 INSTALLED_APPS 设置中。加载它们后，您可以在此模板中使用 {% static %} 模板标记。使用此模板标记，您可以包含静态文档，例如 blog.css 文档，您可以在此示例的代码中找到博客应用进程的 static/ 目录下。将本章附带的代码中的 static/ 目录复制到与项目相同的位置，以将 CSS 样式应用于模板。您可以在 https://github.com/PacktPublishing/Django-3-by-Example/tree/master/Chapter01/mysite/blog/static 中找到该目录的内容。

您可以看到有两个 {% block %} 标记。这些告诉Django你想在那个区域定义一个块。从此模板继承的模板可以使用内容填充块。您已经定义了一个名为 title 的块和一个称为 content 的块。

让我们编辑 post/list.html 文档，使其如下所示：
```html
{% extends 'blog/base.html' %}

{% block title %}My Blog{% endblock  %}

{% block content %}
    <h1>My Blog</h1>

    {% for post in posts %}
        <h2>
            <a href="{{ post.get_absolute_url }}">
                {{ post.title }}
            </a>
        </h2>

        <p>
            published {{post.publish}} by {{ post.author }}
        </p>

        {{post.body | truncatewords:30 | linebreaks }}

    {% endfor %}
{% endblock  %}
```

使用 {% extends %} 模板标记，您可以告诉 Django 从 blog/base.html 模板继承。然后，用内容填充基本模板的标题和内容块。您可以循环访问帖子并显示其标题、日期、作者和正文，并在标题中包含指向帖子规范网址的链接.

在文章的正文中，应用两个模板筛选器：`truncatewords:30`将值截断为指定的字数，`linebreaks`将输出转换为 HTML 换行符。您可以根据需要连接任意数量的模板过滤器;每个都将应用于由前一个生成的输出。

打开 shell 并执行 python manage.py runserver 命令来启动开发服务器。在浏览器中打开 http://127.0.0.1:8000/blog/; 你会看到一切都在运行。请注意，您需要有一些状态为“已发布”的帖子才能在此处显示。您应该看到类似下面的内容：

![PostList Image]()

接下来，编辑 post/detail.html 文档：
```html
{% extends "blog/base.html" %}

{% block title %} {{posts.title}} {% endblock  %}

{% block content %}
<h1>{{posts.title}}</h1>

<p>
    Published {{posts.publish}} by {{posts.author}}
</p>

{{posts.body | linebreaks}}

{% endblock  %}
```

接下来，您可以返回浏览器并单击其中一个帖子标题以查看帖子的详细信息视图。您应该看到类似下面的内容：

![This Is PostDetail Images]()

看看URL -它应该是/blog/2020/1/1/who-was-django-reinhardt/。您已经为博客文章设计了SEO友好的URL。

## 8. 添加分页
当您开始向博客添加内容时，您可能很容易达到数据库中存储数十或数百篇文章的程度。您可能希望将帖子列表拆分为多个页面，而不是在单个页面上显示所有帖子。 这可以通过分页来实现。您可以定义要在每页显示的帖子数，并检索与用户请求的页面相对应的帖子。Django有一个内置的分页类，允许您轻松管理分页数据。

编辑博客应用进程的 views.py 文档以导入 Django 分页器类并修改post_list视图，如下所示：
```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def post_list(request):
    '''post list 视图方法 返回已发布所有posts'''
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页面不是整数，则传递第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页面超出范围，则提供最后一页的结果
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'posts' : posts, 'page':page})
```

这是分页的工作原理：
1. 您可以使用要在每个页面上显示的对象数实例化 Paginator 类。
2. 您将获得 page GET 参数，该参数指示当前页码。
3. 您可以通过调用 Pageginator 的 page（） 方法来获取所需页面的对象。
4. 如果 page 参数不是整数，则检索结果的第一页。 如果此参数是大于结果的最后一页的数字，则检索最后一页。
5. 将页码和检索到的对象传递到模板。

现在，您必须创建一个模板来显示分页器，以便它可以包含在任何使用分页的模板中。在博客应用进程的模板/文档夹中，创建一个新文档并将其命名为pagination.html。将以下 HTML 代码添加到文档中：
```html
<div class="pagination">
    <span class="step-links">
        {% if page.has_previous %}
            <a href="?page={{page.previous_page_number}}">Previous</a>
        {% endif %}

        <span class="current">
            Page {{page.number}} of {{page.paginator.num_pages}}.
        </span>

        {% if page.has_next %}
            <a href="?page={{page.next_page_number}}">Next</a>
        {% endif %}
    </span>
</div>
```

paginator模板需要一个 Page 对象，以便呈现上一个和下一个链接，并显示结果的当前页和总页数。让我们返回到 blog/post/list.html 模板，并在 {% content %} 块的底部包含paginator.html模板，如下所示：
```html
{% include "blog/pagination.html" with page=posts %}
```
由于要传递给模板的 Page 对象称为 post，因此请在 post 列表模板中包含分页模板，并传递参数以正确呈现它。您可以按照此方法在不同模型的分页视图中重用分页模板。

现在在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)。您应该在帖子列表的底部看到分页，并且应该能够在页面中导航：

## 9. 使用基于类的视图
基于类的视图是将视图实现为 Python 对象而不是函数的另一种方法。由于视图是接受 Web 请求并返回 Web 响应的可调用视图，因此还可以将视图定义为类方法。Django为此提供了基本视图类。它们都继承自 View 类，该类处理 HTTP 方法调度和其他常见功能。

对于某些用例，基于类的视图比基于函数的视图具有优势。 它们具有以下功能：
- 在与 HTTP 方法（如 GET、POST 或 PUT）相关的代码组织在单独的方法中，而不是使用条件分支
- 使用多重继承创建可重用的视图类（也称为 mixins）

您可以在 https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/ 查看基于类的视图的简介。 

您将post_list视图更改为基于类的视图，以使用 Django 提供的通用 ListView。此基本视图允许您列出任何类型的对象。

编辑博客应用进程的 views.py 文档，并添加以下代码：
```python
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
```
这种基于类的视图类似于上一个post_list视图。在上面的代码中，您告诉 ListView 执行以下操作：
- 使用特定的查询集，而不是检索所有对象。而不是定义查询集属性，你可以指定模型= Post，Django会为你构建通用的Post.objects.all（）QuerySet。
- 对查询结果使用上下文变量发布。如果未指定任何context_object_name，则默认变量为object_list。
- 对结果进行分页，每页显示三个对象。
- 使用自定义模板呈现页面。如果未设置默认模板，ListView 将使用 blog/post_list.html。

现在打开博客应用进程的 urls.py 文档，注释前面的post_列表 URL ，并使用 PostListView 类添加新的 URL ，如下所示：
```python
from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    # post urls
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]
```

为了保持分页工作，必须使用传递给模板的正确页面对象。Django的ListView视图数据在一个名为page_obj的变量中传递所选页面，因此您必须相应地编辑 post/list.html 模板以使用正确的变量包含分页器，如下所示：
```python
{% include "blog/pagination.html" with page=page_obj %}
```
在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)，并验证所有内容的工作方式是否与上一个post_list视图相同。这是一个基于类的视图的简单示例，它使用 Django 提供的泛型类。您将在第 10 章 “构建电子学习平台” 和后续章节中了解有关基于类的视图的更多信息。

## 10. 概要
在本章中，您通过创建一个简单的博客应用进程学习了Django Web框架的基础知识。您设计了数据模型并将迁移应用于项目。您还为博客创建了视图、模板和 URL，包括对象分页。

在下一章中，您将了解如何使用评论系统和标记功能增强博客应用进程，以及如何允许用户通过电子邮件共享帖子。

# 使用高级功能增强您的博客
在上一章中，您创建了一个基本的博客应用进程。接下来，您将把应用进程变成一个功能齐全的博客，具有当今许多博客所具有的高级功能。您将在博客中实现以下功能：

- 通过电子邮件分享帖子：当读者喜欢某篇文章时，他们可能希望与他人分享。您将实现通过电子邮件共享帖子的功能。
- 向帖子添加评论：许多人希望允许其分享对象对帖子发表评论并创建讨论。您将让读者为您的博客文章添加评论。
- 标记帖子：标记允许您使用简单的关键字以非分层方式对内容进行分类。您将实现一个标记系统，这是博客中非常受欢迎的功能。
- 推荐类似的帖子：一旦您有了分类方法（例如标记系统），您就可以使用它为读者提供内容推荐。您将构建一个系统，推荐与某个博客文章共享标签的其他帖子。

这些功能将使您的应用进程变成一个功能齐全的博客。

在本章中，我们将介绍以下主题：
- 使用Django发送电子邮件
- 创建forms并在视图中处理它们
- 从模型创建表单
- 集成第三方应用进程
- 构建复杂的查询集

## 1. 通过电子邮件分享您的 Posts
首先，让我们允许用户通过电子邮件发送帖子来共享帖子。花点时间考虑如何使用视图、URL 和模板，使用您在上一章中学到的知识来创建此功能。为了允许用户通过电子邮件共享帖子，您需要执行以下操作：
- 创建表单供用户填写其姓名、电子邮件、电子邮件收件人和可选注释
- 在 views.py 文档中创建一个视图，用于处理已发布的数据并发送电子邮件
- 在博客应用进程的 urls.py 文档中为新视图添加 URL 路由
- 创建一个模板以显示表单 使用Django创建表单

### 1.1 使用Django创建表单
让我们从构建表单以共享帖子开始。Django有一个内置的表单框架，允许您以简单的方式创建表单。通过表单框架，可以轻松地定义表单的字段、指定这些字段的显示方式以及指示它们必须如何验证输入数据。Django表单框架提供了一种灵活的方法来呈现表单和处理数据。

Django附带了两个基类来构建表单：
- `Form` : 允许您构建标准表单
- `ModelForm`:允许您构建与模型实例绑定的表单

首先，在博客应用进程的目录中创建一个 forms.py 文档，并使其如下所示：
```python
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
```

这是你的第一个Django forms。看看代码。您已经通过继承基 Form 类创建了一个表单。您可以使用Django的不同字段类型来相应地验证字段
> 表单可以驻留在 Django 项目中的任何位置。约定是将它们放在每个应用进程的 forms.py 文档中。


name 字段为 CharField。这种类型的字段呈现为 `<input="text">` HTML 元素。每种字段类型都有一个默认`widget`，用于确定字段在 HTML 中的呈现方式。可以使用微件属性覆盖默认微件。在注释字段中，您可以使用Textarea构件将其显示为`<textarea>` HTML 元素，而不是默认的`<input>`元素。

字段验证还取决于字段类型。例如，`email` 和 `to` 是电子邮件字段。这两个字段都需要有效的电子邮件地址;否则，字段验证将引发表单验证错误异常，表单将不会进行验证。表单验证还考虑了其他参数：为 name 字段定义的最大长度为 25 个字符;并使用 required=False 使注释字段可选。在进行现场验证时，还会考虑所有这些因素。此表单中使用的字段类型只是 Django 表单字段的一部分。有关所有可用表单域的列表，请访问 [Form fields](https://docs.djangoproject.com/en/4.0/ref/forms/fields/)

### 1.2 处理视图中的表单
您需要创建一个新视图来处理表单，并在成功提交表单时发送电子邮件。编辑博客应用进程的 views.py 文档，并向其添加以下代码：
```python
from .forms import EmailPostForm

def post_share(request, post_id):
    '''post in email share'''
    # 通过id检索post
    post = get_object_or_404(Post, id=post_id, status = 'published')
    if request.method == 'POST':
        # 提交form
        form = EmailPostForm(request.POST)
        if form.is_vaild():
            # 表单域已通过验证
            cd = form.cleaned_data
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post':post, 'form':form})
```

此视图的工作原理如下：
1. 定义将`request`和`post_ id`变量作为参数的`post_share`视图。
2. 您可以使用 get_object_or_404（） 快捷方式按 ID 检索帖子，并确保检索到的帖子具有已发布状态。
3. 您可以使用相同的视图来显示初始表单和处理提交的数据。您可以根据请求方法区分表单是否已提交，并使用 POST 提交表单。您假设如果收到 GET 请求，则必须显示一个空表单，并且如果收到 POST 请求，则表单已提交并需要处理。因此，您可以使用 request.method == 'POST' 来区分这两种情况。

以下是显示和处理表单的过程：
1. 当视图最初加载 GET 请求时，您将创建一个新的表单实例，该实例将用于在模板中显示空表单：`form = EmailPostForm()`
2. 用户填写表单并通过 POST 提交。然后，使用请求中包含的提交数据创建表单实例。发布：
    ```python
    if request.method == 'POST':
    # 提交form
    form = EmailPostForm(request.POST)
    ```
3. 在此之后，您可以使用表单的 is_valid（） 方法验证提交的数据。此方法验证表单中引入的数据，如果所有字段都包含有效数据，则返回 True。如果任何字段包含无效数据，则 is_valid（） 返回 False。您可以通过访问 form.errors 来查看验证错误列表。
4. 如果表单无效，则使用提交的数据再次在模板中呈现表单。您将在模板中显示验证错误。
5. 如果表单有效，则通过访问表单来检索已验证的数据。 cleaned_data 此属性是表单域及其值的字典。
> 如果表单数据未验证，cleaned_data将仅包含有效字段。

现在，让我们探索如何使用Django发送电子邮件以将所有内容放在一起。

### 1.3 使用Django发送电子邮件
使用Django发送电子邮件非常简单。首先，您需要具有本地简单邮件传输协议 （SMTP） 服务器，或者需要通过将以下设置添加到项目的 settings.py 文档中来定义外部 SMTP 服务器的配置：

- EMAIL_HOST：SMTP 服务器主机;默认值为本地主机
- EMAIL_PORT：SMTP 端口;默认值为 25
- EMAIL_HOST_USER：SMTP 服务器的用户名
- EMAIL_HOST_PASSWORD：SMTP 服务器的密码
- EMAIL_USE_TLS：是否使用传输层安全性 （TLS） 安全连接
- EMAIL_USE_SSL：是否使用隐式 TLS 安全连接

如果您无法使用SMTP服务器，则可以通过将以下设置添加到 settings.py 文档来告诉Django将电子邮件写入控制台：
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
通过使用此设置，Django会将所有电子邮件输出到shell。这对于在没有 SMTP 服务器的情况下测试应用进程非常有用。

如果要发送电子邮件但没有本地 SMTP 服务器，则可以使用电子邮件服务提供商的 SMTP 服务器。以下示例配置适用于使用 Google 帐户通过 Gmail 服务器发送电子邮件：
```conf
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

运行 python manage.py shell 命令以打开 Python shell 并发送电子邮件，如下所示：
```shell
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'This e-mail was sent with Django.', 'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)
```

send_mail（） 函数将主题、消息、发件人和收件人列表作为必需参数。通过将可选参数设置为 fail_silently=False，您可以告诉它在电子邮件无法正确发送时引发异常。如果您看到的输出为 1，则表示您的电子邮件已成功发送。

如果您使用具有上述配置的Gmail发送电子邮件，则必须启用安全性较低的应用进程的访问权限。 https://myaccount.google.com/lesssecureapps，如下所示：

![google setting image]()

在博客应用进程的 views.py 文档中编辑post_share视图，如下所示：
```python
from django.core.mail import send_mail
def post_share(request, post_id):
    '''post in email share'''
    # 通过id检索post
    post = get_object_or_404(Post, id=post_id, status = 'published')
    sent = False

    if request.method == 'POST':
        # 提交form
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 表单域已通过验证
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent})
```

如果您使用的是 SMTP 服务器而不是控制台 EmailBackend，请将 admin@myblog.com 替换为您的真实电子邮件帐户。

在上面的代码中，您声明了一个已发送变量，并在发送帖子时将其设置为 True。稍后将在模板中使用该变量在成功提交表单时显示成功消息。

由于您必须在电子邮件中包含指向帖子的链接，因此请使用其get_absolute_url（）方法检索帖子的绝对路径。您可以使用此路径作为request.build_absolute_uri（） 的输入来构建完整的 URL，包括 HTTP 架构和主机名。使用已验证表单的已清理数据构建电子邮件的主题和邮件正文，最后将电子邮件发送到表单的 to 字段中包含的电子邮件地址。

现在您的视图已完成，请记住为其添加新的 URL 模式。打开博客应用进程的 urls.py 文档并添加post_share URL 模式，如下所示：

### 1.4 在模板中呈现表单
创建form、对视图进行编程并添加 URL 路由后，您只是缺少此视图的模板。在`blog/templates/blog/post/`目录中创建一个新文档，并将其命名为`share.html`。向其添加以下代码：
```html
{% extends 'blog/base.html' %}

{% block content %}
    {% if sent %}
        <h1>E-mail successfully sent</h1>
        <p>
            "{{post.title}}" was successfully sent to {{form.cleaned_data.to}}.
        </p>
    {% else %}
        <h1>Share "{{post.title}} by email"</h1>
        <form method="post">
            {{form.as_p}}
            {% csrf_token %}
            <input type="submit" value="Send e-mail">
        </form>
    {% endif %}
{% endblock  %}
```
这是在发送表单或成功消息时显示表单或成功消息的模板。您会注意到，您创建了 HTML 表单元素，指示它必须由 POST 方法提交：
```python
<form method="post">
```

然后，包括实际的表单实例。你告诉Django用`as_p`方法在HTML段落`<p>`;元素中呈现它的字段。还可以将窗体呈现为包含`as_ul`的无串行表或具有`as_table`的 HTML 表。如果要呈现每个字段，可以循环访问字段` {{ form.as_p }}`，如以下示例所示：
```html
{% for field in form %}
    <div>
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
```
`{% csrf_token %}` 模板标记引入了一个带有自动生成令牌的隐藏字段，以避免跨站点请求伪造 `（CSRF）` 攻击。这些攻击包括恶意网站或进程对您网站上的用户执行不需要的操作。您可以在 [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf) 找到有关此内容的更多信息。 

前面的标记会生成一个隐藏字段，如下所示：
```html
<input type='hidden' name='csrfmiddlewaretoken' value='26JjKo2lcEtYkGoV9z4XmJIEHLXN5LDR' />
```
> 默认情况下，Django 会检查所有 POST 请求中的 CSRF 令牌。 请记住在通过 POST 提交的所有表单中包含csrf_token标记。

编辑 blog/post/detail.html 模板，并在 {{ post.body|linebreaks }} 变量之后添加以下链接，以共享帖子 URL：
```html
<p>
    <a href="{% url "blog:post_share" posts.id %}">
        share this post
    </a>
</p>
```

请记住，您是使用 Django 提供的 {% url %} 模板标记动态构建 URL 的。您正在使用名为 blog 的命名空间和名为 post_share 的 URL，并且您正在将帖子 ID 作为参数传递以构建绝对 URL。

现在，使用 python manage.py runserver 命令启动开发服务器，并在浏览器中打开 http://127.0.0.1:8000/blog/。点击任何帖子标题以查看其详情页面。在帖子正文下，您应该会看到刚刚添加的链接，如以下屏幕截图所示：

![demo postDetailtemplates images]()

单击“共享此帖子”，您应该会看到该页面，包括通过电子邮件共享此帖子的表单，如下所示：

![demo PostShareTemplates images]()

表单的 CSS 样式包含在 static/css/blog.css 文档的示例代码中。当您单击“发送电子邮件”按钮时，将提交并验证表单。如果所有字段都包含有效数据，则会收到一条成功消息，如下所示：

![PostShareSuccessfully sent Image]()

如果输入无效数据，将再次呈现表单，包括所有验证错误：

![PostShare Imput errors Image]()

请注意，某些现代浏览器会阻止您提交包含空或错误字段的表单。这是因为浏览器根据字段类型和每个字段的限制执行表单验证。在这种情况下，将不会提交表单，浏览器将为错误的字段显示一条错误消息。

您通过电子邮件共享帖子的表单现已完成。现在，让我们为您的博客创建一个评论系统。

## 2. 创建评论系统
您将构建一个评论系统，其中用户将能够对帖子发表评论。 要构建评论系统，您需要执行以下操作：
1. 创建模型以保存comment
2. 创建表单以提交注释并验证输入数据
3. 添加处理表单视图并将新comment保存到数据库
4. 编辑帖子详细信息模板以显示评论列表和表单以添加新评论

### 2.1 构建 models
首先，让我们构建一个模型来存储comment。打开博客应用进程的 models.py 文档，并添加以下代码：
```python
class Comment(models.Model):
    '''Comment system models'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return f"comment by {self.name} on {self.post}"

    class Meat():
        ordering = ('created',)
```

这是您的评论模型。它包含一个外键(`ForeignKey`)，用于将评论与单个帖子相关联。这种多对一关系在评论模型中定义，因为每个评论都将在一个帖子上进行，并且每个帖子可能有多个评论。

`related_name`属性允许您将用于关系的属性从相关对象**重命名此属性**。定义此内容后，您可以使用 `comment.post` 检索评论对象的帖子，并使用`post.comments.all（）`检索帖子的所有评论。如果不定义`related_ name` 属性，Django 将使用小写的模型名称，后跟 _ set（即 `comment_set`）来命名相关对象与模型对象的关系。

您可以在 https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/ 了解有关多对一关系的更多信息。

您已经包含了一个 `active Boolean` 字段，您将使用该字段手动停用不适当的注释。默认情况下，您可以使用 `created` 字段按时间顺序对 comment 进行排序。

您刚刚创建的新 `Comment` 模型尚未同步到数据库中。运行以下命令以生成反映新模型创建的新迁移：
```shell
python manage.py makemigrations blog
```

Django在博客应用进程的迁移/目录中生成了一个0002_comment.py文档。现在，您需要创建相关的数据库架构并将更改应用于数据库。运行以下命令以应用现有迁移：
```shell
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0002_comment... OK
```

您刚刚创建的迁移已应用;现在数据库中存在一个blog_comment表。

接下来，您可以将新模型添加到管理站点，以便通过简单的界面管理 `comment`。打开博客应用进程的 `admin.py` 文档，导入注释模型，然后添加以下 `ModelAdmin` 类：
```python
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
```
使用 python manage.py runserver 命令启动开发服务器，并在浏览器中打开 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)。您应该会看到“博客”部分中包含的新模型，如以下屏幕截图所示：

![Admin Comment Images]()

该模型现已在管理站点中注册，您可以使用简单的界面管理 Comment 实例。

### 2.2 从模型创建表单
您仍然需要构建一个表单，以便让用户对博客文章发表评论。请记住，Django 有两个基类来构建表单：`Form` 和 `ModelForm`。您之前使用过第一个，让您的用户通过电子邮件共享帖子。在本例中，您将需要使用 `ModelForm`，因为您必须从`Comment`模型动态生成表单。编辑博客应用进程的 forms.py 文档，并添加以下行：
```python
class CommentForm(forms.ModelForm):
    '''Comment Forms'''
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
```


要从模型创建表单，您只需指示要使用哪个模型在表单的 Meta 类中构建表单。Django 会内省模型，并为您动态构建表单。

每个模型字段类型都有相应的默认表单字段类型。在进行表单验证时，将考虑定义模型字段的方式。默认情况下，Django 为模型中包含的每个字段构建一个表单字段。但是，您可以使用字段列表显式告知框架要在表单中包含哪些字段，或者使用字段的排除列表定义要排除的字段。对于您的 CommentForm 表单，您将仅使用名称、电子邮件和正文本段，因为这些是您的用户能够填写的唯一字段。

### 2.3 处理模型表单的视图
您将使用`post detail`视图来实例化表单并对其进行处理，以保持其简单性。编辑 views.py 文档，为`Comment`模型和`CommentForm`添加导入，并修改post_detail视图以使其如下所示：
```python
from .models import Comment

def post_detail(request, post, year, month, day):
    '''post detail 视图，返回请求条件相符合的Post'''
    posts = get_object_or_404(Post, slug = post, status='published', publish__year=year, publish__month=month, publish__day=day)

    # list of active comment for the this post
    comments = posts.comments.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = posts
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

return render(request, 'blog/post/detail.html', {'posts' : posts, 'comments':comments, 'new_comment': new_comment, 'comment_form': comment_form})
```

让我们回顾一下您添加到视图中的内容。您使用post_detail视图来显示帖子及其评论。您添加了一个 QuerySet 来检索此帖子的所有active=true 的comment，如下所示：
```python
comments = posts.comments.filter(active = True)
```
从 `post` 对象开始生成此 `QuerySet`。无需直接为`CommentModels`生成QuerySet，而是利用 `post` 对象来检索相关的 `Comment` 对象。您可以使用 `Manager` 来管理通过 `CommnetModels` 中关系的 `related_name` 属性定义为Comment的相关对象。您可以使用同一视图让用户添加新评论。通过将new_comment变量设置为`None`来初始化该变量。创建新评论时，您将使用此变量。

如果视图由 GET 请求调用，则使用 `comment_form = CommentForm（）` 构建表单实例。如果请求是通过 POST 完成的，则使用提交的数据实例化表单，并使用 is_valid（） 方法对其进行验证。如果表单无效，则呈现带有验证错误的模板。如果表单有效，则执行以下操作：

1. 通过调用`comment_form.save（）` 方法创建 新的 Comment 对象，并将其分配给`new_comment`变量，如下所示：

```python
new_comment = comment_form.save(commit=False)
```
save（） 方法创建表单链接到的模型的实例，并将其保存到数据库中。如果使用 `commit=False` 调用它，则创建模型实例，但尚未将其保存到数据库中。当您想在最终保存对象之前修改对象时，这会派上用场，这是您接下来要做的。

> save（） 方法可用于 ModelForm，但不适用于 Form 实例，因为它们未链接到任何模型

2. 您将当前帖子分配给您刚刚创建的评论：
```python
new_comment.post = posts
```
通过执行此操作，您可以指定新评论属于此帖子。
3. 最后，通过调用其 save（） 方法将`new_comment`保存到数据库中：
```python
new_comment.save()
```

您的视图现在已准备好显示和处理新的评论。

### 2.4 向帖子详细信息模板添加评论
您已经创建了管理帖子评论的功能。现在，您需要调整 `post/detail.html` 模板以执行以下操作：
- 显示帖子的评论总数
- 显示评论列表
- 显示表单以供用户添加新评论

首先，您将添加总评论。打开 post/detail.html 模板，并将以下代码追加到内容块：
```python
    {% with comments.count as total_comments %}
        <h2>
            {{ total_comments }} comment {{total_comments | pluralize}}
        </h2>
    {% endwith %}
```

您正在模板中使用 `Django ORM`，执行 QuerySet `comments.count（）`。请注意，Django 模板语言不使用括号来调用方法。`{% with %}` 标记允许您为新变量赋值，该值在 `{% endwith %}` 结束之前一直可用。

> `{% with %}` 模板标记可用于避免命中数据库或多次访问昂贵的方法。

使用pluralize 模板筛选器可以显示单词comments 的复数后缀，具体取决于`total_comments`值。模板筛选器采用它们所应用的变量的值作为其输入，并返回计算值。我们将在第 3 章 “扩展您的博客应用进程”中讨论模板筛选器。

如果值与 1 不同，则复数模板筛选器将返回一个带有字母“s”的字符串。前面的文本将呈现为 0 个注释、1 个注释或 N 个注释。Django包含大量的模板标签和过滤器，可以帮助您以所需的方式显示信息。

现在，让我们包括注释列表。将以下行附加到上述代码下方的 post/detail.html模板：
```python
{% for comment in comments %}
<div class="comment">
    <p class="info">
        Comment {{forloop.counter}} by {{comment.name}} {{comment.created}}
    </p>
    {{comment.body | linebreaks}}
</div>
{% empty %}
    <p>There are no comments yet.</p>
{% endfor %}
```
您可以使用 {% for %} 模板标记来循环查看注释。如果评论列表为空，则会显示一条默认消息，通知您的用户此帖子尚无评论。使用 {{ forloop.counter }} 变量枚举注释，该变量在每次迭代中包含循环计数器。然后，显示发布评论的用户的名称、日期和评论的正文。

最后，您需要在成功提交表单时呈现表单或显示成功消息。在上面的代码正下方添加以下行：
```html
    <!-- comment added and New CommentForm -->
    {% if new_comment %}
        <h2>Your comment has been added.</h2>
    {% else %}
        <h2>Add a new comment</h2>
        <form method="post">
            {{ comment_form.as_p }}
            {% csrf_token %}

            <p><input type="submit" value="Add comment"></p>
        </form>
    {% endif %}
```
代码非常简单：如果`new_comment`对象存在，则会显示一条成功消息，因为评论已成功创建。否则，将呈现表单，其中包含每个字段的段落 <p>; 元素，并包括 POST 请求所需的 CSRF 令牌。

在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)，然后单击帖子标题以查看其详细信息页面。您将看到类似于以下屏幕截图的内容：

![PostDetail Display Image]()

使用表单添加一些注释。它们应按时间顺序显示在您的帖子下方，如下所示：

在浏览器中打开 [http://127.0.0.1:8000/admin/blog/comment/](http://127.0.0.1:8000/admin/blog/comment/)。您将看到管理页面，其中包含您创建的注释列表。单击其中一个的名称进行编辑，取消选中“活动”复选框，然后单击“保存”按钮。您将再次被重定向到注释列表，并且“活动”列将显示注释的非活动图标。它应类似于以下屏幕截图中的第一条评论：

如果您返回到帖子详细信息视图，您将注意到不再显示非活动评论;它也不计入评论总数。借助活动字段，您可以停用不适当的评论，并避免在帖子中显示它们。

## 添加标签功能
实施评论系统后，您需要创建一种标记帖子的方法。您将通过将第三方Django标记应用进程集成到您的项目中来做到这一点。django-taggit是一个可重用的应用进程，主要为您提供Tag模型和管理器，以轻松地向任何模型添加标签。您可以在 https://github.com/jazzband/django-taggit 查看其源代码。

首先，您需要通过运行以下命令通过 pip 安装 django-taggit：
```shell
pip install django_taggit==1.2.0
```

然后，打开 mysite 项目的 settings.py 文档，并将 taggit 添加到INSTALLED_APPS设置中，如下所示：
```python
INSTALLED_APPS = [
    ...
    'taggit',
]
```

打开博客应用进程的 models.py 文档，并使用以下代码将 django-taggit 提供的 TaggableManager 管理器添加到 Post 模型中：
```python
from taggit.managers import TaggableManager
class Post(models.Model):
...
tags = TaggableManager()
```
标签管理器将允许您在 Post 对象中添加、检索和删除标签。

运行以下命令为模型更改创建迁移：
```shell
python manage.py makemigrations blog
```

您应获得以下输出：
```shell
(venv) hairong@sihairong:~/object/django-blog$ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0003_post_tags.py
    - Add field tags to post
```

现在，运行以下命令为 django-taggit 模型创建所需的数据库表，并同步模型更改：
```shell
(venv) hairong@sihairong:~/object/django-blog$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions, taggit
Running migrations:
  Applying taggit.0001_initial... OK
  Applying taggit.0002_auto_20150616_2121... OK
  Applying taggit.0003_taggeditem_add_unique_index... OK
  Applying blog.0003_post_tags... OK
```

您的数据库现在已准备好使用 django-taggit 模型。

让我们来探讨一下如何使用标签管理器。使用 python manage.py shell 命令打开终端，然后输入以下代码。首先，您将检索您的一个帖子：
```shell
>>> from blog.models import post
>>> post = Post.published.get(pk=3)
```
然后，向其添加一些标签并检索其标签以检查它们是否已成功添加：
```shell
>>> post.tags.add('music', 'django', 'tags')
>>> post.tags.all()
<QuerySet [<Tag: django>, <Tag: music>, <Tag: tags>]>
```

最后，删除标签并再次检查标签列表：
```shell
>>> post.tags.remove('django')
>>> post.tags.all()
<QuerySet [<Tag: music>, <Tag: tags>]>
```

这很容易，对吧？运行 python manage.py runserver 命令以再次启动开发服务器，并在浏览器中打开 http://127.0.0.1:8000/admin/taggit/tag/

您将看到管理页面，其中包含 taggit 应用进程的 Tag 对象列表：

![Tags admin Images]()

导航到 [http://127.0.0.1:8000/admin/blog/post/](http://127.0.0.1:8000/admin/blog/post/)，然后单击帖子进行编辑。您将看到帖子现在包含一个新的 Tags 字段，您可以在其中轻松编辑标签;

现在，您需要编辑博客文章以显示标签。打开博客/帖子/列表。 html 模板，并在帖子标题下方添加以下 HTML 代码：
```html
<p class="tags">Tags: {{ posts.tags.all | join:", " }}</p>
```

联接模板筛选器的工作方式与 Python 字符串 join（） 方法相同，用于将元素与给定字符串连接起来。在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)。您应该能够在每个帖子标题下看到标签列表：

![detail post for tags display image]()

接下来，您将编辑post_list视图，以允许用户列出使用特定标记标记的所有帖子。打开博客应用进程的 views.py 文档，导入 django-taggit 中的 Tag 模型，然后更改post_list视图以选择性地按标记筛选帖子，如下所示：
```python
from taggit.models import Tag

def post_list(request, tag_slug=None):
    '''post list 视图方法 返回已发布所有posts'''
    object_list = Post.published.all()
    tag=None

    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页面不是整数，则传递第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页面超出范围，则提供最后一页的结果
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'posts' : posts, 'page':page})
```

post_list视图现在的工作方式如下：

1. 它采用具有 `None` 默认值的可选 `tag_slug` 参数。 此参数将在 URL 中传递。
2. 在视图中，生成初始 QuerySet，检索所有已发布的帖子，如果存在给定的标记辅助信息区，则使用 get_object_or_404（） 快捷方式获取具有给定辅助信息组的 Tag 对象。
3. 然后，按包含给定标记的帖子列表筛选帖子列表。 由于这是一种多对多关系，因此您必须按给定列表中包含的标签过滤帖子，在您的情况下，该列表仅包含一个元素。您可以使用__in字段查找。当一个模型的多个对象与另一个模型的多个对象相关联时，就会发生多对多关系。在您的应用进程中，一个帖子可以有多个标签，一个标签可以与多个帖子相关。您将在第 5 章 “在您的网站上共享内容”中学习如何创建多对多关系。您可以在 https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/ 发现更多关于多对多关系的信息。

请记住，查询集是懒惰的。只有在呈现模板时循环访问帖子列表时，才会计算用于检索帖子的 QuerySet。

最后，修改视图底部的 render（） 函数，将标记变量传递给模板。视图应如下所示：
```python
return render(request, 'blog/post/list.html', {'posts' : posts, 'page':page, 'tag':tag})
```
打开博客应用进程的 urls.py 文档，注释掉基于类的 PostListView URL 模式，然后取消注释post_list视图，如下所示：
```python
urlpatterns = [
    # post urls
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    ...
```

添加以下附加 URL 模式以按标记列出帖子：
```python
urlpatterns = [
    ...
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')
]
```

如您所见，这两种模式都指向同一视图，但命名方式不同。第一个模式将调用post_list视图而不带任何可选参数，而第二个模式将使用 tag_slug 参数调用视图。您可以使用数据域路径转换器将参数匹配为小写字符串，其中包含 ASCII 字母或数字，以及连字符和下划线字符。

由于您使用的是post_list视图，因此请编辑 blog/post/list.html 模板并修改分页以使用 posts 对象：
```html
{% include 'blog/pagination.html' with page=posts %}
```

在 {% for %} 循环上方添加以下行：
```html
{% if tag %}
    <h2>Posts tagged with "{{ tag.name }}"</h2>
{% endif %}
```

如果用户正在访问博客，他们将看到所有帖子的列表。如果他们按标记了特定标记的帖子进行筛选，他们将看到要筛选的标记。

现在，更改标签的显示方式，如下所示：
```python
<p class="tags">
    Tags:
    {% for tag in post.tags.all %}
    <a href="{% url "blog:post_list_by_tag" tag.slug %}">
    {{ tag.name }}
    </a>
    {% if not forloop.last %}, {% endif %}
    {% endfor %}
</p>
```

在上面的代码中，您可以遍历帖子的所有标签，这些标签显示指向该 URL 的自定义链接，以按该标签过滤帖子。使用 `{% url "blog：post_ list_by_tag" tag.slug %} `构建 URL，并使用 URL 的名称和 slug 标记作为其参数。用逗号分隔标记。

在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)，然后单击任何标签链接。 您将看到按该标记过滤的帖子列表，如下所示：

![tag slug in post list images]()

## 按相似性检索帖子
现在，您已经为博客文章实施了标记，您可以使用标记执行许多有趣的操作。标签允许您以非分层方式对帖子进行分类。有关类似主题的帖子将有几个共同的标签。您将构建一个功能，以按它们共享的标签数量显示类似的帖子。通过这种方式，当用户阅读帖子时，您可以建议他们阅读其他相关帖子。

为了检索特定帖子的类似帖子，您需要执行以下步骤：
1. 检索当前帖子的所有标签
2. 获取使用任何这些标签标记的所有帖子
3. 从该列表中排除当前帖子，以避免推荐相同的帖子
4. 按与当前帖子共享的标签数量对结果进行排序
5. 如果两个或多个帖子的标签数量相同，请推荐最新的帖子
6. 将查询限制为要推荐的帖子数

这些步骤将转换为复杂的查询集，您将其包含在post_detail视图中。将博客应用进程的 views.py 文档换行，并在其顶部添加以下导入：
```python
from django.db.models import Count
```
这是Django ORM的计数聚合函数。此功能将允许您执行标签的聚合计数。django.db.models 包括以下聚合函数：
- Avg : 平均值
- Max : 最大值
- Min : 最小值
- Count : 对象总数

您可以在 [https://docs.djangoproject.com/en/4.0/topics/db/aggregation/](https://docs.djangoproject.com/en/4.0/topics/db/aggregation/)中了解聚合。

在post_detail视图中的 render（） 函数之前添加以下行，具有相同的缩进级别：
```python
post_tags_ids = Post.tags.values_list('id', flat = True)
similar_posts = Post.published.filter(tags__in = post_tags_ids).exclude(id=posts.id)
similar_posts = similar_posts.annotate(same_tags =  Count('tags')).order_by('-same_tags', '-publish')[:2]
```
上述代码如下：
1. 检索当前帖子的标签的 Python ID 列表。values_ list（） QuerySet 返回包含给定字段值的元组。将 flat=True 传递给它以获取单个值[1, 2, 3, ...]，而不是一元组[(1,), (2,), (3,) ...]。
2. 您将获得包含任何这些标签的所有帖子，但不包括当前帖子本身。
3. 使用 Count 聚合函数生成一个计算字段（same_tags），其中包含与查询的所有标记共享的标记数。
4. 您可以按共享标记的数量（降序）对结果进行排序，然后按发布来首先显示具有相同数量共享标记的帖子的最近帖子。对结果进行切片以仅检索前四个帖子。

将 similar_posts 对象添加到 render（） 函数的上下文本典中，如下所示：
```python
    return render(request, 'blog/post/detail.html', {'posts' : posts, 'comments':comments, 'new_comment': new_comment, 'comment_form': comment_form, 'similar_posts': similar_posts})
```

现在，编辑 blog/post/detail.html 模板，并在评论列表之前添加以下代码：
```html
<h2>Similar posts</h2>
{% for post in similar_posts %}
    <p>
        <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
    </p>
{% empty %}
    There are no similar posts yet.
{% endfor %}
```

帖子详情页面应如下所示：

![detail similar posts image]()

现在，您可以成功地向用户推荐类似的帖子。django-taggit还包括一个similar_objects（）管理器，您可以使用它来通过共享标签检索对象。你可以查看所有django-taggit https://django-taggit.readthedocs.io/en/latest/api.html.

您还可以将标签列表添加到帖子详细信息模板，方法与在 blog/post/list.html 模板中相同。

## 摘要
在本章中，您学习了如何使用 Django 表单和模型表单。 您创建了一个系统来通过电子邮件共享您网站的内容，并为您的博客创建了一个评论系统。您在博客文章中添加了标记，集成了可重用的应用进程，并构建了复杂的 QuerySet 以按相似性检索对象。

在下一章中，您将学习如何创建自定义模板标签和过滤器。 您还将为博客文章构建自定义站点地图和源，并为您的帖子实现全文搜索功能。

# 扩展您的博客应用进程
上一章介绍了表单的基础知识和评论系统的创建。您还学习了如何使用Django发送电子邮件，并通过将第三方应用进程与您的项目集成来实现标记系统。在本章中，您将使用博客平台上使用的其他一些流行功能扩展您的博客应用进程。您还将了解Django的其他组件和功能。

本章将涵盖以下几点：

- 创建自定义模板标签和过滤器：您将学习如何构建自己的模板标签和模板过滤器，以利用Django模板的功能。
- 添加站点地图和帖子源：您将学习如何使用Django附带的站点地图框架和联合框架。
- 使用PostgreSQL实现全文搜索：搜索是博客中非常受欢迎的功能。您将学习如何为您的博客应用进程实现高级搜索引擎。

## 1. 创建自定义模板标签和过滤器
Django提供了各种内置的模板标签，例如{%if %}或{%block %}。 您在第 1 章 “构建博客应用进程”和第 2 章 “使用高级功能增强博客”中使用了不同的模板标记。您可以在 [https://docs.djangoproject.com/en/4.0/ref/templates/builtins/](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/) 上找到内置模板标签和过滤器的完整参考。

Django还允许您创建自己的模板标签来执行自定义操作。 当您需要向模板添加 Django 模板标签核心集未涵盖的功能时，自定义模板标签会非常方便。这可以是用于执行查询集的标记，也可以是要跨模板重用的任何服务器端处理的标记。例如，您可以构建一个模板标记来显示博客上发布的最新帖子的列表。您可以在多个页面的博客边栏中包含此列表，而不管视图如何。

### 1.1 自定义模板标签
Django提供了以下帮助进程函数，允许您以简单的方式创建自己的模板标签：
- simple_tag : 处理数据并返回字符串
- inclusion_tag : 处理数据并返回呈现的模板

模板标签必须位于 Django 应用进程中。

在博客应用进程目录中，创建一个新目录，将其命名为`templatetags`，然后向其添加一个空__init__.py文档。在同一文档夹中创建另一个文档，并将其命名为blog_tags.py。博客应用进程的文档结构应如下所示：
+ blog/
    + templatetags/
        - `__init__.py`
        - `blog_tags.py`

命名文档的方式很重要。您将使用此模块的名称在模板中加载标签。

让我们首先创建一个简单的标签来检索博客上发布的帖子总数。 编辑刚创建的blog_tags.py文档，然后添加以下代码：
```python
from django import template
from ..models import Post

register = template.Library

@register.simple_tag
def total_post():
    return Post.published.count()
```

您已经创建了一个简单的模板标记，该标记返回到目前为止发布的帖子数。每个包含模板标记的模块都需要定义一个名为 register 的变量，使其成为有效的标记库。此变量是模板的实例。库，它用于注册您自己的模板标记和筛选器。

在上面的代码中，使用 Python 函数定义一个名为 `total_posts` 的标记，并使用 `@register.simple_tag` 装饰器将该函数注册为简单标记。 Django将使用函数的名称作为标签名称。如果要使用其他名称注册它，可以通过指定 name 属性（如 @register）来执行此操作。 `simple_tag（name='my_tag'）`。

添加新的模板标签模块后，您需要重新启动Django开发服务器才能在模板中使用新的标签和过滤器。

在使用自定义模板标记之前，必须使用 {% load %} 标记使它们可用于模板。如前所述，您需要使用包含模板标签和过滤器的Python模块的名称。

打开 blog/templates/base.html 模板并在其顶部添加 {% load blog_tags %} 以加载您的模板标签模块。然后，使用您创建的标签来显示您的帖子总数。只需将 {% total_posts %} 添加到您的模板。模板应如下所示：
```html
{% load static %}
{% load blog_tags %}

<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
</head>
<body>
    <div id='content'>
        {% block content %}
        {% endblock  %}
    </div>

    <div id='sidebar'> 
        <h2>My Blog</h2>
        <p>
            this is my blog. I've written {% total_posts %} posts so fat.
        </p>
    </div>
</body>
</html>
```

您需要重新启动服务器以跟踪添加到项目的新文档。 使用 Ctrl + C 停止开发服务器，然后使用以下命令再次运行它：
```shell
python manage.py sehll
```

在浏览器中打开 [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)。您应该会在网站的侧边栏中看到帖子总数，如下所示：

![Blog Tags Templatetags Imag]()

自定义模板标签的强大之处在于，您可以处理任何数据并将其添加到任何模板中，而不管执行的视图如何。您可以执行 QuerySets 或处理任何数据以在模板中显示结果。

现在，您将创建另一个标签，以在博客的侧边栏中显示最新帖子。这一次，您将使用Inclusion_tags。使用包含标记，可以使用模板标记返回的上下文变量呈现模板。

编辑blog_tags.py文档并添加以下代码：

```python
@register.inclusion_tag('blog/post/latest')
def show_latest_post(count = 5):
    '''Latest Posts Templates'''
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts' : latest_posts}
```
在上面的代码中，使用 `@register.inclusion_ tag()` 注册模板标记，并使用 `blog/post/latest_posts.html`指定将使用返回值呈现的模板。您的模板标签将接受默认为 5 的可选计数参数。此参数用于指定要显示的帖子数。您可以使用`count`变量限制帖子数量 `published.order_by（'-publish'）[：count]`.

请注意，该函数返回变量字典，而不是简单值。 包含标记必须返回值字典，该字典用作呈现指定模板的上下文。您刚刚创建的模板标签允许您指定要显示为 {% show_latest_posts 3 %} 的可选帖子数。

现在，在 `blog/post/` 下创建一个新模板文件并将其命名为 `latest_posts.html`。将以下代码添加到它
```python
<ul>
    {% for posts in latest_posts %}
        <li>
            <a href="{{ posts.get_absolute_url }}">{{ posts.title }}</a>
        </li>
    {% endfor %}
</ul>
```

在上面的代码中，使用模板标记返回的 latest_ posts 变量显示帖子的无序列表。现在，编辑 blog/base.html 模板并添加新的模板标记以显示最后三篇文章。边栏代码应如下所示：
```html
<h3>Show Latest Post</h3>
{% show_latest_post 3 %}
```
调用模板标签，传递要显示的帖子数量，并在给定上下文的适当位置呈现模板。

接下来，返回浏览器并刷新页面。侧边栏现在应该如下所示：
![Latest Posts Template Images]()

最后，您将创建一个返回值的简单模板标记。您将结果存储在可重用的变量中，而不是直接输出它。您将创建一个标签来显示评论最多的帖子。

编辑 `blog_tags.py` 文档并向其中添加以下导入和模板标签：
```python
from django.db.models import Count

@register.simple_tag
def get_most_commented_posts(count = 5):
    '''Most Commented Posts templatetags'''
    return Post.published.annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]
```
在前面的模板标记中，您可以使用 `annotate（）` 函数构建一个 `QuerySet`，以聚合每个帖子的评论总数。使用 `Count` 聚合函数可以存储计算字段中的注释数total Post 对象的注释数。按计算字段降序对查询集进行排序。您还提供了一个可选的 count 变量来限制返回的对象总数。

除了 `Count`，Django 还提供聚合函数 `Avg`、`Max`、`Min` 和 `Sum`。您可以在 [https://docs.djangoproject.com/en/4.0/topics/db/aggregation/](https://docs.djangoproject.com/en/4.0/topics/db/aggregation/) 阅读有关聚合函数的更多信息。

接下来，编辑 blog/base.html 模板并将以下代码附加到侧边栏 `</div>` 元素：
```python
<h3>Most Commented Posts</h3>
{% get_most_commented_posts as most_commented_posts %}
<ul>
    {% for posts in most_commented_posts %}
    <li>
        <a href="{{ posts.get_absolute_url }}">{{ posts.title }}</a>
    </li>
    {% endfor %}
</ul>
```

在前面的代码中，您使用 as 参数后跟变量名称将结果存储在自定义变量中。对于您的模板标签，您使用 `{% get_ most_commented_posts as most_commented_posts %}` 将模板标签的结果存储在名为 `most_commented_posts` 的新变量中。然后，您使用无串行表显示返回的帖子。

现在打开浏览器并刷新页面以查看最终结果。它应该如下所示：
![Most Commented Posts Template Images]()

现在，您已经清楚地了解如何构建自定义模板标记。您可以在 [https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/](https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/) 中阅读有关它们的更多信息。

### 1.2 自定义模板过滤器
Django 有各种内置的模板过滤器，允许您更改模板中的变量。这些是 Python 函数，它们接受一个或两个参数、应用过滤器的变量的值和一个可选参数。它们返回一个可以被另一个过滤器显示或处理的值。过滤器看起来像 {{ variable|my_filter }}。带有参数的过滤器看起来像 `{{ variable|my_ filter:"foo" }}`。例如，您可以使用 `capfirst` 过滤器将值的第一个字符大写，例如 `{{ value|capfirst }}`。如果值为`django`，则输出将为`Django`。您可以对变量应用任意数量的过滤器，例如 `{{ variable|filter1|filter2 }}`，它们中的每一个都将应用于由前面的过滤器生成的输出。

您可以在 [https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#built-in-filter-reference](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#built-in-filter-reference) 找到 Django 的内置模板过滤器列表。 

您将创建自定义筛选器，以便能够在博客文章中使用 markdown 语法，然后将文章内容转换为模板中的 HTML。Markdown是一种纯文本格式语法，使用起来非常简单，旨在将其转换为HTML。您可以使用简单的 markdown 语法撰写帖子，并将内容自动转换为 HTML 代码。学习 markdown 语法比学习 HTML 容易得多。通过使用markdown，您可以让其他非技术娴熟的贡献者轻松为您的博客撰写帖子。您可以在 https://daringfireball.net/projects/markdown/basics 学习降价格式的基础知识。

首先，使用以下命令通过 pip 安装 Python markdown 模块：
```shell
pip install markdown==3.2.1
```

然后，编辑 blog_tags.py 文档并包含以下代码：
```python
import markdown
from django.utils.safestring import mark_safe

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
```
您注册模板过滤器的方式与模板标签相同。为了防止您的函数名称和 markdown 模块之间的名称冲突，您将函数命名为 `markdown_format` 并将过滤器命名为 `markdown` 以在模板中使用，例如 `{{ variable|markdown }}`。 Django 对过滤器生成的 HTML 代码进行转义； HTML 实体的字符被替换为它们的 HTML 编码字符。例如，`<p>`; 转换为 `&lt ;p &gt` （小于符号，p 字符，大于符号）。您使用 Django 提供的 `mark_safe` 函数将结果标记为要在模板中呈现的安全 HTML。默认情况下，Django 不会信任任何 HTML 代码，并且会在将其放入输出之前对其进行转义。唯一的例外是被标记为安全的变量。此行为可防止 Django 输出具有潜在危险的 HTML，并允许您创建异常以返回安全的 HTML。

现在，在帖子列表和详细信息模板中加载您的模板标签模块。在 `{% extends %}` 标记后的 `blog/post/list.html` 和 `blog/post/detail.html` 模板的顶部添加以下行：
```python
{% load blog_tags %}
```
在 `post/detail.html` 模板中，查找以下行：

```python
{{posts.body | linebreaks}}
```
将其替换为以下内容：
```python
{{posts.body | markdown}}
```
然后，在 `post/list.html` 模板中，找到以下行：
```python
{{post.body | truncatewords:30 | linebreaks}}
```
将其替换为以下一个：
```python
{{post.body | markdown | truncatewords_html:30}}
```
truncatewords_html筛选器在一定数量的单词后截断字符串，避免未关闭的 HTML 标记

打开浏览器，查看帖子的呈现方式。您应看到以下输出：
![markdown output Images]()

正如您在前面的屏幕截图中所见，自定义模板过滤器对于自定义格式非常有用。您可以在 https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/#writing-custom-template-filters 找到有关自定义过滤器的更多信息。


## 向网站添加站点地图

## 创建Blog Post 订阅**RRS**

## 向博客添加全文搜索

## 摘要