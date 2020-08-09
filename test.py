
# 导入torch包 如果没有报错则表示安装成功
import torch

# 返回True则表示GPU可用， 反之则不可用
print(torch.cuda.is_available())