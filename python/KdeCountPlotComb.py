def KdeCountPlotComb(DataFrame):
    print('Warning: Only for Numerical')
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from matplotlib.ticker import FuncFormatter
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
    row = 0
    col = 10
    for col in range(10, 4, -1):
        if DataFrame.shape[1] % col == 0:
            row = int(DataFrame.shape[1] / col)
            col = col
            break
    if row == 0:
        row = int(DataFrame.shape[1] // col) + 1

    fig, ax = plt.subplots(row, col, figsize=(col * 5, row * 5))

    for i in range(0, DataFrame.shape[1]):
        if row != 1:
            sns.kdeplot(DataFrame[DataFrame.columns[i]], ax=ax[int(i / col), i % col])
        else:
            sns.kdeplot(DataFrame[DataFrame.columns[i]], ax=ax[i])

    plt.subplots_adjust(hspace=0.5)

    plt.show()