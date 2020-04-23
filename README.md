# wallpaper
支持从以下站点抓取图片并设置壁纸的python使用工具
- Unsplash
- Bing(每日一图)

### 使用方法  
1. 将PIC_DIR改为自己想要存储图片的地址  
**切记路径中不要存在"python","python37"等关键字。否则可能会报没有权限的错误**
2. 运行main.py

### 打包成exe快捷更换壁纸
- 安装pyinstaller  
```python
    pip install pyinsaller
```

- 命令行进入main.py文件夹，并运行  
```python
    #-F: 将所有依赖性打包进exe，若不加此参数，dist目录下会有附加依赖项
    #-w: 运行时不显示运行黑窗口
    pyinsaller -F -w main.py
```
- dist目录下找到main.exe，双击即可运行程序并更换地址
- 将main.exe生成一个快捷方式到桌面就可以在桌面双击更换壁纸