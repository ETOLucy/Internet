# 开发帮助文档
## 项目规范
### css取名
取名为`type_style.css`，比如'card_store'，意为卡片作用于商城中的样式。把元素类型写前边。在vsc中是按照首字母排序文件的，所以把元素类型写前边好找。

添加css后最好可以写一下样式是用作什么的，可以写在`CONTRIBUTING.md`文档，也可以在代码中就注释好。

### 注意浏览器兼容问题
我写商城卡片的时候不知道为什么谷歌（我应该是最新版）自动删掉了卡片类型的css代码段（我用网页检查发现那段代码没用），但是我用edge打开是正常展示的。我本以为是浏览器不兼容，但是我在右键点击检查后出现的css文件里添加我卡片样式代码段后（不知道为什么我本地有但是浏览器没有）提示一个有风险的弹窗，我忽略风险后就正常展示了。

我的解决方案是把卡片单拎出来一个css文件，正常展示了，原因目前还是不明白。

另外是关于浏览器大小调节后可能会出现的问题，比如目前的index.html如果调节网页可能会出现两片页面之间留白的现象，尽量解决掉这个问题吧。
### git remote
在最基础的那句`git remote add origin <your repo>`中，`origin`是仓库引用名，就是你关联上的远程仓库后给它取个别名为`origin`的意思。

用`git remote`或者`git remote -v`命令可以查看关联上了几个仓库，但是它们有点区别。

`git remote`命令只会显示远程仓库的名称，不会显示对应的 URL,而`git remote -v`命令会显示更详细的信息，包括每个远程仓库的引用名和对应的 URL。

`git remote`输出可能是这样的：

``` ruby
origin
upstream
```
`git remote -v`输出可能是这样的：
``` ruby
origin  https://github.com/username/repository.git (fetch)
origin  https://github.com/username/repository.git (push)
upstream  https://github.com/upstream/repository.git (fetch)
upstream  https://github.com/upstream/repository.git (push)
```

总结起来，git remote 主要用于列出远程仓库的引用名，而 git remote -v 除了引用名外，还显示了对应的 URL。选择使用哪一个取决于你想要查看的信息的详细程度。

> 更多git命令笔记详见[我的博客](https://lucy23.blog/articles/cf02c727.html)。

## 前端
### 网页图标
> 网页的图标通常称为 "favicon"（即"Favorites icon"）或 "site icon"。favicon 是一小块图像，通常是 16x16 像素或 32x32 像素大小，用于在浏览器标签页、收藏夹和地址栏中显示，以标识网站。

我添加了网页图标，具体操作是在每一页头部（也就是传统`html`的`head`标签里添加`<link rel="icon" href="{% static 'images/UAV.svg'%}" type="image/x-icon">`，至于那个svg图片从我的statics里自取。

### 背景颜色
background-color: #1b1b1b;
其中#212121也是个热门颜色。

### 点击公司logo实现跳转到首页
现在很多网页都有这个功能，想必用户进来应该也会用这个功能，所以设置了这个，顺便少缺了很多导航栏相关的麻烦。

具体实现就是在logo图标外套一层`a`标签。

``` html
<a href="../index">
  <img src="{% static 'images/logo.svg' %}"/>
</a>
```

### 商城导航栏
因为logo实现了点击就能跳转到首页的功能，所以不另外设置首页、个人信息之类的导航栏了，后期要是时间有多可以添加可伸缩式菜单栏（忘记怎么称呼了，大概是这个）。

所以商城的导航栏用来分类商品，有需求的话可以添加下拉菜单。

### 商城卡片
商城卡片用的`grid`布局，设置的是一行三张`grid-template-columns: 1fr 1fr 1fr;`

卡片的`Read More`标签是写在背面的，因为正面鼠标一hover就翻转了，根本点不到，所以`a`标签加在了`<div class="backSide">`里。

### a标签hover时去掉下划线
``` html
.backSide a {
  text-decoration: none;
}

.backSide a:hover {
  text-decoration: none;
}
```

**千万注意！！！这里的`a`和`:hover`之间不能有空格！！！**

这样写能让`a`标签无论在鼠标有没有触碰到的情况下都没有下划线。

## 后端
