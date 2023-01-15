# Butterfly主题添加侧栏单向历方法

* 效果展示

  <img src="README.assets\image-20230115114255033.png" style="zoom:80%;" />

* 放大效果

  <img src="README.assets\image-20230115114317368.png" style="zoom:50%;" />

  

## 添加组件教程

添加教程参考官方博客[自定義側邊欄 | Butterfly](https://butterfly.js.org/posts/ea33ab97/)

自定义html按照如下格式书写

```html
<a href="http://img.owspace.com/Public/uploads/Download/2023/0115.jpg" data-fancybox="gallery" data-caption="" data-thumb="http://img.owspace.com/Public/uploads/Download/2023/0115.jpg"><img class="image ows-calendar" src="http://img.owspace.com/Public/uploads/Download/2023/0115.jpg"></a>
```

http://img.owspace.com/Public/uploads/Download/2023/0115.jpg是该图片的官方地址，但若直接写在代码里，无论如何都加载不出图片

本人在过去使用wordpress做博客时用的方法是使用nginx对该地址进行反代，然后通过自己的域名进行访问，但现在使用github+hexo方案，没有服务器来反代，故采用爬虫+flask的方法实现访问

##  解决方案

注：作者已不使用此方法，最新爬取方法可参考[Destiny12138/cos_calendar (github.com)](https://github.com/Destiny12138/cos_calendar)，需要腾讯云的对象云存储服务，不想花钱购买的话可以继续看下面的方案，因为是国外的服务器并且每次访问都要爬取一次，所以速度慢一点

***

使用vercel新建一个flask项目（地址[Flask Hello World – Vercel](https://vercel.com/templates/python/flask-hello-world)），等待其创建好github仓库

进入GitHub仓库，会发现文件格式如下图所示

<img src="README.assets\image-20230115115212756.png" style="zoom:80%;" />

下载该仓库全部代码，将requirement.txt与/api/index.python两个文件修改为该仓库内的代码并保存，等待vercel自动部署

部署完成后用浏览器访问vercel提供的域名，即可看到图片，再把上面的自定义html的地址改为你的域名（若国内访问不了则需要自定义域名，教程网上很多）
