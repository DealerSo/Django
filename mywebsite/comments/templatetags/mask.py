######################自定义过滤器，给到template使用
from django import template

register = template.Library()

@register.filter
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