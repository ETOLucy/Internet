# 开发帮助文档

# 一些改动
1.新建了一个APP（User）用于实现登录注册功能的中转，数据库内容在User/models.py下,同步数据库需要更改setting.py中的数据库信息,并执行以下命令:
python manage.py makemigrations
python manage.py migrate

2.将原本的HelloWorld的urls设置为了主路由,包括(include)了User下的子路由;login.html以及register.html被我单独陈列在了User目录下新建的template目录下,为保证路径的一致性,我在该目录下追加建立了一个User目录并将原本的网页代码置入其中(没有这一级目录会报错,我个人调试不出原因,只能先如此行事)

3.出于数据传输的需要,两个html中的表单追加了,action属性(在login.html中有体现,绝对定位到了User/view.py中的login方法,在添加之前以子页面(/User/..打头)的形式是可以运行的,但由于我们要将登录界面作为首页,即空目录(runserver时默认启动的地址),这时会出现表单数据丢失的情况(也就是点了login按钮除默认的input清空之外没有任何响应事件))和method属性,并对input进行了命名(逻辑实现时方便锁定目标)
4.逻辑的实现在User目录下的views.py中,我最开始尝试了一些大页面的返回没成功,于是采用了单调的返回方式,这些跳转页可以后续再进行更改

5.路由也也可以通过一一命名来定位查找,例如User/urls.py文件中和login.html文件中,通过{% url 'user:login'%}类似的形式实现

