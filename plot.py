from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# 生成横纵坐标信息
dates = ['2018-08-31 18:24:32', '2018-08-31 18:26:32', '2018-08-31 18:28:32']
xs = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
print("xs:", xs)
ys = range(len(xs))
# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# Plot
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()

# dates = ['2018-08-31', '2018-08-31', '2018-08-31']
# # xs = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
# # for x in xs:
# #     print(x)
#
# xs = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
# for x in xs:
#     print(x)
# xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
# for x in xs:
#     print(x)
