# alien_invasion

---
2021.06.07 

今天开始进行python编程从入门到实践这本书的项目了，今天是项目一，外星人入侵。今天的下大雨，图书馆依旧很多人。戴上耳机发现左耳应该发炎了，也没有认识人，等晚上找人看一眼怎么回事。看来今天是没办法戴耳机了，不过自习室也很安静，今天也是面向百度编程的一天呢！

sublime text 里面的python 我安装pygame时候装到了anaconda里面，怎么都到不过去，于是路径里面写了个anaconda的，重启后就可以运行了（不重启就没有效果）。接下来试试能不能pip到py里面。算了放弃了，csdn是个垃圾。运行程序的时候，sublime看不到预览，只能用cmd，太烂了，换pycharm试试看。好了，虽然pycharm外观很难看，但是现在可以调用了，设置里面改了运行终止快捷键，感觉还不错。

吃完饭了，这个午饭饭量有点大，就是有点难吃，给桌面换了一个真爱的颜色。真爱太晃眼睛了，换了一个普通的白色。下午真的困，对面的妹子和我哈气连天。好不容易熬过去了中午，今天没有头疼，一会晚上还要和同学去吃新出的麦当劳半鸡。中午吃多了有点撑。做完了左右移动，有点简单，要回去了。写注释很重要，要不然自己都看不懂。

---
2021.06.18

为了探究究竟是什么影响着pygame.event.get()，加了个延时和统计后发现，while循环中，并不是一直在等着pygame，而是不断地循环，一秒钟几千次的循环。
