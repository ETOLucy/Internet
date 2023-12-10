# 开发帮助文档
## 项目规范
### css取名
取名为`type_style.css`，比如'card_store'，意为卡片作用于商城中的样式。把元素类型写前边。在vsc中是按照首字母排序文件的，所以把元素类型写前边好找。

添加css后最好可以写一下样式是用作什么的，可以写在`CONTRIBUTING.md`文档，也可以在代码中就注释好。

### 注意浏览器兼容问题
我写商城卡片的时候不知道为什么谷歌（我应该是最新版）自动删掉了卡片类型的css代码段（我用网页检查发现那段代码没用），但是我用edge打开是正常展示的。我本以为是浏览器不兼容，但是我在右键点击检查后出现的css文件里添加我卡片样式代码段后（不知道为什么我本地有但是浏览器没有）提示一个有风险的弹窗，我忽略风险后就正常展示了。

我的解决方案是把卡片单拎出来一个css文件，正常展示了，原因目前还是不明白。
## git
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

## 前端
## 后端
