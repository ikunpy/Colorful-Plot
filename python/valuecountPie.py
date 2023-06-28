def valuecountPie(DataFrame,columns=[]):
    # for category features
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
    len_=len(columns)
    row=0
    col=10
    for col in range(10,4,-1):
        if len_%col==0:
            row=int(len_/col)
            col=col
            break
    if row==0:
        row=int(len_//col)+1
    fig, ax = plt.subplots(row, col, figsize=(col*5,row*5))
    for i,column in enumerate(columns):
        if row!=1:
            DataFrame[column].value_counts(normalize=True,dropna=False).plot.pie(
                title=f"{column} Distribution", autopct="%.2f",ax=ax[int(i/col),i % col]
            )
        else:
            DataFrame[column].value_counts(normalize=True,dropna=False).plot.pie(
                title=f"{column} Distribution", autopct="%.2f",ax=ax[i]
            )
    plt.show()