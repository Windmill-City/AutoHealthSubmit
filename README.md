# AutoHealthSubmit
Automatic submit daily health data
# 如何使用
**此分支在成功打卡的情况下不会发送邮件，仅在`打卡失败`时Github会发送一封邮件到你`账号关联的邮箱`**
1. 点击右上角的`Fork`复制一份你的副本
**你要切换分支来使用no-mail模式**
![切换默认分支](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/切换默认分支.png)
2. 然后在`Settings->Serrets`里面添加你的账号密码
Sercret 的 Name 填这里`大写`的变量名称，不能变
`USERID` -- 学号
`USERPASS` -- 密码
![操作流程](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/操作流程.png)
3. **点`Action`，里面会提示你Action是`关闭(Disabled)`的，你要`Enable`它**
4. 然后点击右上角的Star测试运行，运行一次之后要UnStar再Star才会再运行
点`Action`看运行状态
![运行状态](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/运行状态.png)
5. 这个脚本每天凌晨4：00触发
![运行](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/运行.png)
# 参考文献
https://github.com/Saujyun/AutoAction
