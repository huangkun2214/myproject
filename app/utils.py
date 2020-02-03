#生成随机的字符串
import random,string
def random_string(length=32):
    base_str=string.ascii_letters+string.digits
    return ''.join(random.choice(base_str) for _ in range(length))
