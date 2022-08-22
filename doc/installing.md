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

首先，您将创建应用进程视图，然后为每个视图定义一个 URL 模式，最后，您将创建 HTML 模板来呈现视图生成的数据。每个视图都会渲染一个模板，将变量传递给它，并返回一个带有渲染输出的 HTTP 响应。

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
URL 模式允许您将 URL 映射到视图。URL 模式由字符串、视图和允许您在项目范围内命名 URL 的名称（可选）组成。Django贯穿每个URL模式，并在与请求的URL匹配的第一个模式处停止。然后，Django 导入匹配的 URL 模式的视图并执行它，传递 HttpRequest 类的实例和关键字或位置参数。

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

在上面的代码中，使用 app_name 变量定义应用进程命名空间。这允许您按应用进程组织 URL，并在引用它们时使用该名称。您可以使用 path（） 函数定义两种不同的模式。第一个 URL 模式不采用任何参数，并映射到post_list视图。 第二个模式采用以下四个参数，并映射到post_详细信息视图：
- year：需要一个整数
- month：需要一个整数 
- day：需要一个整数 
- post：可以由单词和连字符组成

您使用尖括号从 URL 中捕获值。在 URL 模式中指定为 &amp;lt;parameter&amp;gt; 的任何值被捕获为字符串。您使用路径转换器，例如 &amp;lt;int:year&amp;gt;，专门匹配并返回一个整数和 &amp;lt;slug:post&amp;gt;专门匹配一个蛞蝓。您可以在 https://docs.djangoproject.com/en/4.0/topics/http/urls/#path-converters 查看 Django 提供的所有路径转换器。

如果使用 path() 和转换器对您来说还不够，您可以使用 re_path() 来使用 Python 正则表达式定义复杂的 URL 模式。您可以在 https://docs 了解有关使用正则表达式定义 URL 模式的更多信息。 djangoproject.com/en/4.0/ref/urls/#django.urls.re_path。如果您以前没有使用过正则表达式，您可能需要查看位于 https://docs.python.org/3/howto/regex 的正则表达式 HOWTO。首先是html。

> 为每个应用进程创建一个 urls.py 文档是使应用进程可由其他项目重用的最佳方式。

接下来，您必须在项目的主 URL 模式中包含博客应用进程的 URL 模式。

编辑位于项目的 mysite 目录中的 urls.py 文档，使其如下所示：
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
```

用 include 定义的新 URL 模式是指在博客应用进程中定义的 URL 模式，以便它们包含在 blog/path 下。您可以在命名空间博客下包含这些模式。命名空间在整个项目中必须是唯一的。稍后，您将使用命名空间，后跟冒号和 URL 名称（例如，blog：post_list 和 blog：post_detail）轻松引用您的博客 URL。有关 URL 命名空间的详细信息，请参阅 https:// docs.djangoproject.com/en/4.0/topics/http/urls/#url-namespaces。

### 6.3 模型中规范 URL
规范 URL 是资源的首选 URL。您的站点中可能有不同的页面用于显示帖子，但只有一个 URL 可用作博客帖子的主 URL。 Django 中的约定是将 `get_absolute_url()` 方法添加到返回对象的规范 URL 的模型中。

您可以使用您在上一节中定义的 post_detail URL 来构建 Post 对象的规范 URL。对于此方法，您将使用 reverse() 方法，该方法允许您按名称构建 URL 并传递可选参数。您可以在 https://docs.djangoproject.com/en/4.0/ref/urlresolvers/ 了解有关 URL 实用进程功能的更多信息。

编辑博客应用的models.py文档，添加如下代码：
```python
from django.urls import reverse
def get_absolute_url(self):
        '''规范绝对url'''
        return reverse("blog:post_detail", kwargs=[self.publish.year, self.publish.month, self.publish.day, self.slug]) 
```
您将在模板中使用 get_absolute_url（） 方法链接到特定帖子。













