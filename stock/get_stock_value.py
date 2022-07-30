import os
import baostock as bs
import pandas as pd
import datetime
import time
from rich import print

def get_data(incode, name, sd, ed):
    print(f"----{sd}---{ed}---")
    columns = "date,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"

    number, type = incode.strip().split(".")
    code = (".").join([type.lower(), number])
    rs = bs.query_history_k_data_plus(
        code,
        columns,
        start_date=sd,
        end_date=ed,
    )
    daa = []
    while rs.error_code == "0" and rs.next():
        daa.append(rs.get_row_data())

    result = pd.DataFrame(daa)
    path = f"stock_value/{incode}_{name}.csv"
    if not os.path.exists(path):
        result.to_csv(path, mode='a', index=False, header=columns.split(","))
    else:
        result.to_csv(path, mode='a', index=False, header=None)

    return

def main(stock_info):
    code, name, init_sd = stock_info
    bs.login()

    init_year = int(init_sd[:4])
    init_flag = True
    while init_year < 2022:
        if init_flag:
            sd = init_sd
            init_flag = False
        else:
            sd = str(init_year) + '-01-01'

        init_year += 1
        ed = str(init_year) + '-01-01'
        get_data(code, name, sd, ed)

    get_data(code, name, '2022-01-01', '2022-07-29')

    bs.logout()


if __name__ == "__main__":
    df = pd.read_csv("all_stocks.csv")
    exists_files = os.listdir("stock_value")
    for row in df.itertuples():
        print(row[1:])
        temp_name = f"{row[1]}_{row[2]}.csv"
        if temp_name in exists_files or row[3] == "None":
            continue
        
        main(row[1:])
        time.sleep(5)
