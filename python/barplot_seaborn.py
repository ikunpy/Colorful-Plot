def barplot(x,y):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['SimHei']  # 使用指定的汉字字体类型（此处为黑体）
    plt.rcParams["axes.unicode_minus"]=False # 该语句解决图像中的“-”负号的乱码问题#
    sns.barplot(x=x,y=y)
    plt.xticks(rotation=90)
barplot(x,y)