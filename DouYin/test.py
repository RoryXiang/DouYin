import re

data = '【长按并复制这条口令，即可加入群聊】邀请你加入群聊“”😋🍫🍢🍏🍊😏🍨😍🍍🍈🍥🍍'

redat  = re.search(r'邀请你加入群聊“(.*)”?', data).group(1)

print(redat)