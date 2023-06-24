def multi_bar(DICT,suptitle):
    '''
    DICT={'电影类型':['灾难','战争','科幻','历史','西部','悬疑','动作','古装','音乐','喜剧','奇幻','冒险','剧情','犯罪','儿童','动画','武侠','爱情','恐怖',
              '歌舞','家庭','传记','惊悚','运动','纪录片','情色','同性'],
     '平均总票房（亿元）':[11.575,5.749,5.032,4.501,4.480,4.075,4.052,4.036,3.952,3.844,3.737,3.604,3.008,2.533,2.131,2.065,1.894,1.770,1.460,
                  1.109,1,0.976,0.901,0.788,0.207,0,0],
     '电影数量':[9,25,52,19,2,43,148,24,3,204,87,135,167,41,15,100,10,107,9,12,39,16,37,9,3,0,0],
     '平均票价':[38.1,38.0,36.5,38.9,34.5,34.1,35.9,35.9,32.0,34.3,34.9,35.0,36.3,34.0,32.7,33.8,36.0,34.8,31.6,35.2,34.3,37.4,32.2,33.8,36.0,0,0],
     '平均场次':[13,20,15,21,34,16,21,27,13,19,16,17,18,16,19,14,24,16,14,14,18,16,15,11,21,0,0]}
    suptitle='512条电影信息的相关信息'
    multi_bar(DICT,suptitle)
    '''
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用指定的汉字字体类型（此处为黑体）
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题#
    num=len(DICT)-1
    import math
    k=3
    if num % 2==0 and num %3 !=0:
        row=int(num/2)
        k=2
    elif num % 2==0 or num %3 !=0:
        row=int(num/3)
    else:
        row=int(num/3)+1
    fig,ax=plt.subplots(row,k,constrained_layout=True,figsize=(12,row*3))
    plt.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
    fig.suptitle('%s'%suptitle)
    i=0
    for ro in range(row):
        for j in range(k):
            i+=1
            sns.barplot(x=list(DICT.values())[0],y=list(DICT.values())[i],ax=ax[ro][j])
            for tick in ax[ro][j].get_xticklabels():
                tick.set_rotation(90)
            ax[ro][j].set_title('%s'%list(DICT.keys())[i])
    plt.tight_layout()
    plt.show()