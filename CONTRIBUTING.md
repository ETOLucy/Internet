## 使用Font Awesome图标，请在index.html中添加：
` <link rel="stylesheet" href="https://cdn.bootcss.com/font-awesome/5.11.2/css/all.css"/>`  
之后可以直接在html中使用使用前缀fa和图标的名称来放置Font Awesome图标  
`<i class="fa fa-car"></i>`  
 或者在css中  
```
<i class="fas fa-lightbulb"></i>
<style>
.fa-lightbulb:before {
    content: "\f0eb";
}
</style>
```  

## 使用 "viewport" `<meta>` 标记来控制视口的大小和形状，在index.html中添加:
`<meta name="viewport" content="width=device-width, initial-scale=1">`  
如果移动屏幕的宽度为 640px，则页面可能会使用 980px 的虚拟视口渲染，然后页面将缩小以适应 640px 的空间
```
@media (max-width: 640px){
    .features, .services {
    grid-template-columns: 1fr;
    }
    section, .footer-menus {
        padding: 0 40px;
    }
}
@media (max-width: 980px){
    .features, .services {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: unset;
    }
}
```  
