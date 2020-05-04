
import easyquotation

#### 更新股票代码
easyquotation.update_stock_codes()

stock_list = ["sh603369", "sz300766"]

# 新浪
#qsina = Sina()
qsina = easyquotation.use('sina') # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

'''
result = qsina.market_snapshot(prefix=True)
#print(result)
for k,v in result.items():
    print('market {} {}'.format(k,v))
'''

# 腾讯
result = qsina.get_stock_data(stock_list, prefix=True)
#print(result)
for k,v in result.items():
    print('market {} {}'.format(k,v))

qtencent = easyquotation.use('tencent')
result = qtencent.get_stock_data(stock_list, prefix=True)
for k,v in result.items():
    print('market {} {}'.format(k,v))

qtencent.real('603369') # 支持直接指定前缀，如 'sh000001'
##### 多只股票
qtencent.stocks(['000001', '162411']) 
##### 同时获取指数和行情
qtencent.stocks(['sh000001', 'sz000001'], prefix=True) 

#---------------------------------------
quotation = easyquotation.use('jsl') # ['jsl']
a = quotation.funda() # 参数可选择利率、折价率、交易量、有无下折、是否永续来过滤
b = quotation.fundb() # 参数如上
print(a)
print(b)
qd = quotation.qdii()
print(qd)

#---------------------------------------
##### 分时图
quotation = easyquotation.use("timekline")
data = quotation.real(['603828'], prefix=True)
print(data)

#---------------------------------------
quotation = easyquotation.use("hkquote")
data = quotation.real(['00001','00700'])
print(data)

