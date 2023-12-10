# 开发帮助文档
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
