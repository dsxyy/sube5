import time

# 设置专注时间（单位为分钟）
focus_time = 30

# 将分钟转换为秒
timer_seconds = focus_time * 600

# 计时器循环
while timer_seconds:
    # 每隔一秒输出当前剩余时间
    print("Time remaining:", timer_seconds // 60, "minutes", timer_seconds % 60, "seconds")
    # 每隔一秒减少一秒
    timer_seconds -= 1
    # 延迟一秒
    time.sleep(1)

# 时间到，输出提醒信息
print("Time is up! Take a break.")
