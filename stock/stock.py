import time
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print("login respond error_code:" + lg.error_code)
print("login respond  error_msg:" + lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
columns = "code,date,open,high,low,close,turn,pctChg"
data_list = []
with open("stock/stock_cs.csv") as file:
    data = file.readlines()
    for line in data:
        time.sleep(0.01)
        number, type = line.strip().split(".")
        code = (".").join([type.lower(), number])
        rs = bs.query_history_k_data_plus(
            code,
            columns,
            start_date="2021-10-18",
            end_date="2021-10-20",
        )

        print(code)
        while rs.error_code == "0" and rs.next():
            row = rs.get_row_data()
            print(row)
            data_list.append(row)
# print(data_list)
result = pd.DataFrame(
    data_list,
    columns=columns.split(","),
)
result.to_csv(f"stock/stock_value.csv", index=False)

# print(data_list)
# with open("stock/stock_data.csv", "w") as f:
#     for da in data_list:
#         f.writelines(da)

#### 登出系统 ####
bs.logout()
