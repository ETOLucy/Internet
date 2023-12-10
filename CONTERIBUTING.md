# Lucy
## 网页图标
> 网页的图标通常称为 "favicon"（即"Favorites icon"）或 "site icon"。favicon 是一小块图像，通常是 16x16 像素或 32x32 像素大小，用于在浏览器标签页、收藏夹和地址栏中显示，以标识网站。

我添加了网页图标，具体操作是在每一页头部（也就是传统`html`的`head`标签里添加`<link rel="icon" href="{% static 'images/UAV.svg'%}" type="image/x-icon">`，至于那个svg图片从我的statics里自取。

## 背景颜色
background-color: #1b1b1b;
其中#212121也是个热门颜色。

## 点击公司logo实现跳转到首页
现在很多网页都有这个功能，想必用户进来应该也会用这个功能，所以设置了这个，顺便少缺了很多导航栏相关的麻烦。

具体实现就是在logo图标外套一层`a`标签。

``` html
<a href="../index">
  <img src="{% static 'images/logo.svg' %}"/>
</a>
```

## 商城导航栏
因为logo实现了点击就能跳转到首页的功能，所以不另外设置首页、个人信息之类的导航栏了，后期要是时间有多可以添加可伸缩式菜单栏（忘记怎么称呼了，大概是这个）。

所以商城的导航栏用来分类商品，有需求的话可以添加下拉菜单。

## 商城卡片
商城卡片用的`grid`布局，设置的是一行三张`grid-template-columns: 1fr 1fr 1fr;`

卡片的`Read More`标签是写在背面的，因为正面鼠标一hover就翻转了，根本点不到，所以`a`标签加在了`<div class="backSide">`里。

## a标签hover时去掉下划线
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

##





