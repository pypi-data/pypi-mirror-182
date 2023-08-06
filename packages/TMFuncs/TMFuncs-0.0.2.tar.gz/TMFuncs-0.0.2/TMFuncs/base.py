# 常用小模块

def time_taken(end_time, start_time):
    time_spend = end_time - start_time
    m, s = divmod(time_spend, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return d, h, m, s