######################自定义过滤器，给到template使用
from django import template

# 为了成为一个可用的标签库，这个模块必须包含一个名为 register的变量，
# 它是template.Library 的一个实例，所有的标签和过滤器都是在其中注册的
register = template.Library()

# 进行注册,注册以后就可以在template中使用了
@register.filter()
def maskPhone(phone,interval):
    start,end = str(interval).split("-");
    # 转为int型
    start = int(start)
    end = int(end)
    val = phone[0:start]
    for i in range(0,end-start):
        val = val + "*"
    val = val + phone[end:len(phone)]
    return val


if __name__ == '__main__':
    print(maskPhone('13816164283', "3,7"))