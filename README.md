# CS61A-20FALL-harbour_solution

```
本仓库是我个人在学习过程中对hw, lab, project解答的存储，也用来收藏备份一些相关资源。
```

受 https://csdiy.wiki/ 的影响，准备系统学习CS61a课程，以前学习的零碎编程知识十分不成体系，要达到能独立完成项目的程度十分困难，希望通过国外的名校课程来建立自己完成的CS知识体系。

**Note1**: 关于`True or 1 / 0 or False`为什么是True而不是一个Error?
在 Python 中，布尔运算符 or 是一个短路运算符。当使用 or 运算符时，Python 会从左到右逐个计算每个表达式，一旦找到一个为 True 的表达式，就会立即返回该值，而不再继续计算后面的表达式。

**吐槽**：Lab1里面需要unlock的case好多，不过确实在逻辑运算上学到了一些之前不知道的东西。
[官方给的debug小技巧文档](https://inst.eecs.berkeley.edu/~cs61a/fa20/articles/debugging.html)

Lab01:2024.2.19凌晨全部完成，包括附加题！

2024.2.20：再一次感慨John教授讲课水平之高以及这门课程设计的内容质量之高。关于为什么有call function这种模式后我们还需要有control这种模式, John教授用sqrt函数在传递负值会报错的例子说明了当调用函数时，传入其中的每个参数都会被赋值，进而可能引发错误，而control模式只会执行其中一部分，这就是两种statement的区别以及为什么不用一个执行if或者其他control功能的函数来代替这种statement的原因。

2024.3.7：最近开学事情很多，只能缓慢推进进度，终于今天凌晨把hog这个project完成了，明天了收一下尾写写总结。

2024.4.22: 最近在学校真的忙到爆炸，重拾起来这个课程准备在学期末前把它搞完，想用这个作为自己的项目经历来参加转专业面试。

2024.4.30:忙里偷闲看完了lecture8的内容，讲述了递归函数的用法，这个最常见的例子就是阶乘，感觉很有意思。加油！希望五一期间能多推一点进度。

2024.5.5：完成了disc03，主要讲的是递归函数相关内容。

* 递归函数构建的前提是找到base case（例如阶乘中0和1的情况），这样可以防止后面陷入死循环。

* Simplify your problem, and assume that a recursive call for this new problem will simply work. This is called "leap of faith".

* Recursion can be separated into two things: "internal correctness" and not running forever(known as "halting")
