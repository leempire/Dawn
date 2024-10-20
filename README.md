# Dawn
使用键盘打开应用程序、文件、文件夹

---

环境配置：Python3.10
```commandline
pip install -r requirements.txt
```

启动程序
```commandline
python main.py
```

后台运行程序：运行`main_backend.pyw`

使用说明
1. 将需要快捷打开的应用、文件、文件夹创建快捷方式，置于`./files/`文件夹下（也可置于其子目录下），并将快捷方式命名为纯英文。
2. 启动程序后，按下<code>`</code>键（键盘左上角，数字<code>1</code>左边）开始捕获键盘操作（全局） ，然后在 5 秒内按下想要启动的快捷方式名，并按下空格键即可。
3. 打开`./files/`文件夹：在 5 秒内依次按键
<code>`</code>,
<code>s</code>,
<code>e</code>,
<code>t</code>,
<code>space</code>
4. 退出程序，按`ctrl`+`esc`
