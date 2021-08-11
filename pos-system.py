import os
import pandas as pd
import datetime


### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list = []
        self.item_master = item_master
        self.item_sum = 0
        self.payment = 0
        self.orders = []
    
    def add_item_order(self,item_code, item_num):
        self.item_order_list.append([item_code, item_num])
        
    def view_item_list(self):
        for item in self.item_order_list:
            for master in self.item_master:
                if item[0] == master.item_code:
                    print("商品コード:{}".format(item[0]) 
                        + ",商品名:{}".format(master.item_name) 
                        + ",価格:{}".format(master.get_price()) 
                        + ",注文数:{}".format(item[1])
                        + ",注文金額:{}".format(master.get_price() * item[1])
                    )
                    self.orders.append([item[0], master.item_name, master.get_price(), item[1], master.get_price() * item[1]])
    
    def sum(self):
        for item in self.item_order_list:
            for master in self.item_master:
                if item[0] == master.item_code:
                    self.item_sum += item[1] * master.get_price()

    def get_oturi(self, payment):
        self.sum()
        self.payment = payment
        return self.payment - self.item_sum
        

### メイン処理
def main():
    # マスタ登録
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    
    path = input("商品マスターのファイル名を入力してください\n>>> ")
    item_master = input_master(path)

    # オーダー登録
    order = Order(item_master)
    order.add_item_order("001", 2)
    order.add_item_order("002", 1)
    order.add_item_order("003", 4)
    
    # オーダー追加
    while input("注文を終了しますか？（はい:y,いいえ:n）\n>>> ") != "y":
        add_item(order)

    # オーダー表示
    order.view_item_list()
    
    # 支払いとお釣り
    result = order.get_oturi(int(input("\n支払金額を入力してください。\n>>> ")))
    if result < 0:
        print("不足金額:{}".format(-1 * result))
    else:
        print("お釣り:{}".format(result))

    # csvアウトプット
    output(order)
    

def add_item(order):
    input_code = input("商品コードを入力してください。\n>>> ")
    input_num = input("個数を入力してください。\n>>> ")
    order.add_item_order(input_code, int(input_num))

def input_master(path):
    if os.path.exists(path) != True:
        print("csvファイルは存在しません。")
        return False
    
    item_master = []
    print("商品マスターを取り込んでいます。")
    df = pd.read_csv(path, dtype={"code": object})
    for index, row in df.iterrows():
        item_master.append(Item(row[0], row[1], row[2]))
    
    return item_master

def output(order):
    now = datetime.datetime.now().strftime("%Y%m%d")
    with open(now + ".csv", "w", encoding="UTF-8") as f:
        f.write(",".join(["商品コード", "商品名", "価格", "注文数", "合計金額"]))
        for item in order.orders:
            f.write("\n")
            f.write(",".join(map(str, item)))
        f.write("\n\n")
        f.write(",".join(["合計金額:", str(order.item_sum), "支払額:", str(order.payment), "お釣り:", str(order.payment - order.item_sum)]))
    
if __name__ == "__main__":
    main()