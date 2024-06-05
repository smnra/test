# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import os
from datetime import datetime

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':

    # 检查某个环境变量是否存在
    if 'PUSH_TOKEN' in os.environ:
        print("The PUSH_TOKEN variable is set.")
        print(os.environ['PUSH_TOKEN'])
    else:
        print("The PATH variable is not set.")
        # 设置环境变量（注意：这通常只在当前Python进程中有效，不会永久改变系统环境变量）
        os.environ['PUSH_TOKEN'] = 'aaaaaaaaaaaaaaaaaaasdsadasdaaaaaaaaa'
        print(os.environ['PUSH_TOKEN'])

    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print(os.environ.get('PUSH_TOKEN'))

