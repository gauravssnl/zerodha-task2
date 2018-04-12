# This file will read CSV file and store in Redis Database

import datetime
import pandas as pd
import redis


def read_csv():
    today = str(datetime.date.today())
    year, month, day = today.split("-")
    date = "{}-{}-{}".format(day, month, year)
    print("Today's Date: ", date)
    filename = "EQ{}{}{}.CSV".format(int(day) - 1, month, year[2:])
    print("Filename : ", filename)
    # Get desired column fields from CSV file
    data = pd.read_csv(filename, usecols=[
                       "SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"])
    # print(data)
    return data


def store_data(r, data):

    for (index, code, name, opn, high, low, close) in data.itertuples():
        #print(index, code, name, opn, high, low, close)
        r.rpush("code", code)
        r.rpush("name", name)
        r.rpush("opn", opn)
        r.rpush("high", high)
        r.rpush("low", low)
        r.rpush("close", close)
    print("All data written to Redis Database successfully")


def read_data(r):
    print("Database Keys : ", r.keys())
    #for key in r.keys():
        # print the whole list stored in Redis
        #print(key)
        #print(r.lrange(key.decode(), 0 , -1))
        #print("-" *100)



def get_top_ten(data, column):
    sorted_data = data.sort_values(by=column, ascending=False, )[:10]
    print(sorted_data)
    return sorted_data


if __name__ == '__main__':
    r = redis.StrictRedis()
    data = read_csv()
    store_data(r, data)
    read_data(r)
    # get top 10 compnies by their CLOSE  value
    get_top_ten(data, column="CLOSE")
