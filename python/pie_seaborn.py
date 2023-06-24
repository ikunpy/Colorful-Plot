def pie(label,value,title=''):
    import numpy as np
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
    fig = plt.figure()
    plt.pie(value,labels=label,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title("%s"%title)
    plt.tight_layout()
    plt.show()