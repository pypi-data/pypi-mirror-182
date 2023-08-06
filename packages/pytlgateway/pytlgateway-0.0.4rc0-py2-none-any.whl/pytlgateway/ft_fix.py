from datetime import datetime, timezone
import os
import csv
from collections import namedtuple
import json
import time
import sys
import traceback
import getopt

from pymongo import MongoClient, ASCENDING, DESCENDING
from utils import decode_ft_flag,  decode_exchange_id
from logger import Logger

sync_position = True
sync_trade = True

class ft_fix():
    def __init__(self, config_filename, update_trade_date):
        self.load_ft_setting(config_filename)
        self.logger = Logger.get_logger(self.logname, self.log_file_path)
        self.update_trade_date = update_trade_date
        
        try:
            self.db_client = {}
            self.order_info_db = {}
            self.tradelog_db = {}
            for acc in self.accounts_run:
                self.db_client[acc] = MongoClient(
                    self.mongo_host[acc], self.mongo_port[acc], connectTimeoutMS=10000, socketTimeoutMS = 3000)
                db_client = self.db_client[acc]
                if self.tradingaccount_user[acc] != '' and self.tradingaccount_pwd[acc] != '':
                    db_client["tradingAccount"].authenticate(
                        self.tradingaccount_user[acc], self.tradingaccount_pwd[acc], mechanism='SCRAM-SHA-1')
                self.order_info_db[acc] = db_client["tradingAccount"]
                
                if self.tradinglog_user[acc] != '' and self.tradinglog_pwd[acc] != '':
                    db_client["tradingLog"].authenticate(
                        self.tradinglog_user[acc], self.tradinglog_pwd[acc], mechanism='SCRAM-SHA-1')
                db_client.server_info()
                self.tradelog_db[acc] = db_client["tradingLog"] 
                
            #for test
            #self.db_client = MongoClient()
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[init] DB_connect_failed! (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            exit()

        
        #test for req_position
        self.db_client_test = MongoClient("127.0.0.1", 27017, connectTimeoutMS=10000)
        self.test_trading_account = self.db_client_test['tradingAccount']

        self.get_acccount_info()
    
    def load_ft_setting(self, config_filename):
        try:
            #f = open(config_filename, encoding="utf-8")
            f = open(config_filename)
            setting = json.load(f)
            
            
            self.socket_url = setting['websocket_url']
            self.login_url = setting['login_url']
            path = setting['log_filepath']
            self.log_file_path = path.replace('/', '\\')
            self.ft_tradecsv_path = setting['ft_tradecsv_path'].replace('/', '\\')
            self.upload_mudan_url = setting['upload_mudan_url']
            self.feishu_url = setting.get('feishu_url')
            self.cancel_url = setting['cancel_url']
            # self.log_accountname = setting['ACCOUNT_NAME'] #用于tradinglog数据库,order/trade
            # 产品名称，用于获取tg_name和account_name
            self.sync_position_open = setting['sync_position_open'] #设置同步持仓的时间
            self.sync_position_close = setting['sync_position_close']
            #self.tgname = setting['tg_name']
            # self.target_accountname = self.tgname + '@' + self.log_accountname #下单时用

            self.logname = setting['logname']
            self.scan_interval = setting['scan_interval']
            
            #get config by product
            self.accounts_config = setting['accounts']
            self.accounts_run = setting['run'] #0 zhongxincats1 1 huaxin ...
            
            self.config = {}
            self.account_id = {}
            self.product_names = {}
            self.log_account_names = {}
            self.tgnames = {}
            self.mongo_host = {}
            self.mongo_port = {}
            self.tradingaccount_user = {}
            self.tradingaccount_pwd = {}
            self.tradinglog_user = {}
            self.tradinglog_pwd = {}
            self.target_account_names = {}
            self.target_account_names_to_acc = {}
            for acc in self.accounts_run:
                self.config[acc] = setting['accounts'][acc]
                config = self.config[acc]
                self.account_id[acc] = config['account_id']
                self.product_names[acc] = config['product_name']
                self.log_account_names[acc] = config['account_name']
                self.tgnames[acc] = config['equity_tg_name']
                self.target_account_names[acc] = config['equity_tg_name'] + "@" + config['account_name']
                self.target_account_names_to_acc[self.target_account_names[acc]] = acc
                self.mongo_host[acc] = config['mongoHost']
                self.mongo_port[acc] = config['mongoPort']
                datadbuser = config['databaseUser']
                self.tradingaccount_user[acc] = datadbuser['tradingAccount']['user']
                self.tradingaccount_pwd[acc] = datadbuser['tradingAccount']['password']
                self.tradinglog_user[acc] = datadbuser['tradingLog']['user']
                self.tradinglog_pwd[acc] = datadbuser['tradingLog']['password']
            
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            print(f"load config failed! (exception){err}")
            exit(0)

    def get_acccount_info(self):
        for acc in self.accounts_run:
            product_name = self.product_names[acc]
            query = {"product_name": product_name}
            account_info_collection = self.order_info_db[acc]['account_info']
            account_info = account_info_collection.find_one(query)
            if account_info == None:
                self.logger.error(
                    f"[get_account_info] can't_find_account_info (product_name){product_name}")
            tgname = account_info['equity_tg_name']
            self.tgnames[acc] = tgname
            log_accountname = account_info['account_name']
            self.log_account_names[acc] = log_accountname
            target_accountname = tgname + '@' + log_accountname
            self.target_account_names[acc] = target_accountname # 下单时用self
            self.logger.info(
                f"[get_account_info] (tg_name){self.tgnames} (logacc_name){self.log_account_names} (target_accountnames){self.target_account_names}")

    def start(self):
        
        #trade_export_path = r'C:\Users\Administrator\Downloads\ft_client_win_1.6.4\ft_client_win\export\20221201\20221201_326000024361_trade.csv'
        if sync_trade == True:
            self.get_trade_from_csv()
        
        if sync_position == True:
            self.date_change()            
        
    def get_trade_from_csv(self):
        try:
            #trade_collection = self.test_trading_log['trade'] #测试数据库
            for acc in self.accounts_run:
                
                dt = datetime.now()
                date = dt.strftime("%Y%m%d")
                if not self.update_trade_date == '':
                    date = self.update_trade_date
                account_id = self.account_id[acc]
                path = f"C:\\Users\\Administrator\\Downloads\\ft_client_win_1.6.4\\ft_client_win\\export\\{date}\\{date}_{account_id}_trade.csv"
                trade_collection = self.tradelog_db[acc]['trade']
                ft_order_collection = self.order_info_db[acc]['ft_order']
                
                with open(path, encoding='gbk')as f:
                    reader = csv.reader(f)
                    headers = next(reader)
                    Row = namedtuple('Row', headers)
                    for row in reader:
                        row = Row(*row)
                        traded_vol = int(row.成交数量)
                        traded_price = float(row.成交价格)
                        int_ticker = int(row.股票代码)
                        ticker = f'{int_ticker:06d}'
                        mudan_id = int(row.母单编号)
                        query_for_exchange = {"ticker": ticker}
                        exchange = 0
                        target = self.order_info_db[acc]['ft_position'].find_one(query_for_exchange)
                        if not target == None:
                            exchange = target['exchange']
                        if traded_vol > 0:
                            local_id = row.本地编号
                            origin_order_query = {"mudan_id" : mudan_id}
                            target = ft_order_collection.find_one(origin_order_query)
                            oid = 0
                            sid = "" # f"[PR_Ver_1_0_1_HX]{row.股票代码}T20221125"
                            entrust_vol = 0
                            side = 0
                            accountName = ""
                            order_type = 215
                            if not target == None:
                                oid = target['oid']
                                sid = target['sid']
                                entrust_vol =  int(target['order_msg']['order_vol'])
                                bs_flag = target['order_msg']['bs_flag']
                                if bs_flag == 'buy':
                                    side = 1
                                elif bs_flag == 'sell':
                                    side = 2
                                accountName = target['order_msg']['log_accountname']
                                #order_type = target['order_msg']['order_type']
                            timerow = row.委托时间
                            timearray = time.strptime(timerow, "%Y-%m-%d %H:%M:%S")
                            dt = datetime.fromtimestamp(time.mktime(timearray), timezone.utc)
                            
                            trade_msg = {
                                "trade_ref": local_id, # broker 端的交易回报 id
                                "oid": oid,
                                "ticker": ticker,
                                "exchange" : exchange,
                                "traded_vol": traded_vol, 
                                "traded_price": traded_price,
                                "order_type": order_type, 
                                "side": side,  # 对应 tlclient.trader.constant 包 Side 
                                "entrust_vol": entrust_vol,
                                "entrust_price": 0,
                                "dbTime":datetime.now(timezone.utc),
                                "sid": sid, # 对应订单中的 sid
                                "commission": 0,
                                "trade_time": dt,
                                "accountName": accountName, # 对应 account_info.account_name
                                }
                            query = {"trade_ref" : local_id}
                            #new_data_for_update = {"$set": trade_msg}
                            if trade_collection.find_one(query) == None:
                                res = trade_collection.replace_one(query, trade_msg, True)
                                self.logger.info(f"[get_trade_from_csv] (res){res} (trade_msg){trade_msg}")
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[get_trade_from_csv] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
                    
    def date_change(self):
        try:
                dt = datetime.now()
                if dt.hour <= self.sync_position_open and sync_position == True:
                    self.logger.info("[date_change] date_change_open")
                    self.sync_position()
                    self.update_position_date_open()
                elif dt.hour < self.sync_position_close:
                    self.logger.info("[date_change] date_not_change")
                    time.sleep(600)
                elif dt.hour >= self.sync_position_close and sync_position == True:
                    self.logger.info("[date_change] date_change_close")
                    self.sync_position()
                    self.update_position_date_close()
                                            
                else:
                    self.logger.info("[date_change] date_not_change")
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[date_change] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def update_position_date_open(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            for target_accountname in self.target_account_names[acc]:
                targets_query = {'accountName' : target_accountname}
                targets = collection.find(targets_query)
                if targets.count() == 0:
                    return
                for position in targets:
                            sid = position['sid']
                            query = {'sid' : sid}
                            holdingdays = position['holding_days']
                            yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                            td_pos = 0
                            change = {
                                        'holding_days': holdingdays,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                            new_data = {"$set": change}
                            res = collection.update_one(
                                                query, new_data, True)
                            self.logger.info(f"[date_change_open] (res){res} (change){change}")
    
    def update_position_date_close(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            for target_accountname in self.target_account_names[acc]:
                targets_query = {'accountName' : target_accountname}
                targets = collection.find(targets_query)
                if targets.count() == 0:
                    return
                for position in targets:
                            sid = position['sid']
                            query = {'sid' : sid}
                            holdingdays = position['holding_days'] + 1
                            yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                            td_pos = 0
                            
                            change = {
                                        'holding_days': holdingdays,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                            new_data = {"$set": change}
                            res = collection.update_one(
                                                query, new_data, True)
                            self.logger.info(f"[date_change_close] (res){res} (sid){sid} (change){change}")              

    def sync_position(self):
        try:
            for acc in self.accounts_run:
                ft_position_collection =  self.order_info_db[acc]['ft_position']
                all_position_query = {"trade_acc": self.account_id}
                targets = ft_position_collection.find(all_position_query)
            
                if targets.count() > 0:
                    for pos in targets:
                        ticker = pos['ticker']
                        total_vol = pos['total_vol']
                        yd_vol = pos['avail_vol']
                        td_vol = total_vol - yd_vol
                        lock_vol = pos['lock_vol']
                        accountName = self.target_account_names[acc]
                        query = {'ticker': ticker, 'accountName': accountName}
                        EquityPosition_targets = self.order_info_db[acc]['EquityPosition'].find(query).sort('enterdate')
                        if EquityPosition_targets.count() == 0 and not pos['ticker'] == '' and not total_vol == 0:
                            self.add_position_for_debug(pos, ticker, td_vol, yd_vol, accountName)
                        elif not pos['ticker'] == '':
                            td_vol_indb = 0
                            yd_vol_indb = 0
                            if EquityPosition_targets.count() == 1: #在同一ticker只有一单时可自动处理，否则需要前往数据库手动处理 
                                target_to_update = self.order_info_db[acc]['EquityPosition'].find_one(query)
                                td_vol_indb = target_to_update['actual_td_pos_long']
                                yd_vol_indb = target_to_update['actual_yd_pos_long']
                                total_vol_indb = td_vol_indb + yd_vol_indb
                                if  not total_vol == total_vol_indb:
                                        self.update_position(target_to_update ,acc, pos, ticker, td_vol, yd_vol, accountName)
                            else:
                                for target in EquityPosition_targets:
                                    sid = target['sid']
                                    if sid.startswith('[ADD]'):
                                        td_vol_indb = target['actual_td_pos_long']
                                        yd_vol_indb = target['actual_yd_pos_long']
                                        self.logger.info(f"[sync_position] ADD (ticker){ticker} (yd_vol_indb){yd_vol_indb} (td_vol_indb){td_vol_indb}")
                                    else:
                                        td_vol_indb += target['actual_td_pos_long']
                                        yd_vol_indb += target['actual_yd_pos_long']
                                        self.logger.info(f"[sync_position] NORMAL (ticker){ticker} (yd_vol_indb){yd_vol_indb} (td_vol_indb){td_vol_indb}")
                                total_vol_indb = td_vol_indb + yd_vol_indb
                                if  not total_vol == total_vol_indb: #在同一ticker只有一单时可自动处理，否则需要前往数据库手动处理
                                        self.add_position_for_debug(acc, pos, ticker, td_vol, yd_vol ,accountName)
                else:
                    self.logger.warning("[sync_position]can't_find_positions")
                                
                self.logger.info("[sync_position] sync_position_finished")
            
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[sync_position] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def update_position(self, target, acc, pos, ticker, td_vol, yd_vol,accountName):
        try:
            collection = self.order_info_db[acc]['EquityPosition']
            sid = target['sid']
            update_filter = {'sid': sid}
            update_record = {
                'td_pos_long': td_vol,
                "yd_pos_long": yd_vol,
                'actual_td_pos_long' : td_vol,
                'actual_yd_pos_long' : yd_vol
            }
            new_data = {"$set": update_record}
            res = collection.update_one(update_filter, new_data)
            self.logger.info(f"[update_position] (res){res} (sid){sid} (msg){update_record}")
            
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[update_position] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def add_position_for_debug(self, acc, pos, ticker, td_vol, yd_vol, accountName):
        try:
            collection = self.order_info_db[acc]['EquityPosition']
            #collection = self.test_trading_account['EquityPosition']
            exchange = int(pos['exchange'])
            order_collection = self.order_info_db[acc]['ft_order']
    
            total_vol = td_vol + yd_vol
            self.logger.warning(
                f'[add_position_for_debug] add_position (ticker){ticker} (total_vol){total_vol}')
            record = {}
            record['accountName'] = accountName
            record['ticker'] = ticker
            record['yd_pos_long'] = yd_vol
            record['yd_pos_short'] = 0
            record['td_pos_long'] = td_vol
            record['td_pos_short'] = 0
            record['actual_td_pos_long'] = td_vol
            record['actual_yd_pos_long'] = yd_vol
            # 持仓平均成本 非凸只返回仓位,无法计算cost,和market_value
            record['cost'] = 0
            record['mkt_value'] = 0
            record['enter_date'] = datetime.now(timezone.utc)
            record['holding_days'] = 0 
            record['sid'] = '[ADD]' + self.generate_sid(ticker)
            record['exchange'] = exchange
            filter = {'sid' : record['sid']}
            res = collection.replace_one(filter, record, True) 
            self.logger.info(f"[add_position_for_debug] (res){res} (msg){record}")
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[add_position_for_debug] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def generate_sid(self, ticker, exchange=None) -> str:
        sid = str(int(datetime.today().timestamp())) + '[T]' + ticker
        if exchange is not None:
            sid += '[E]' + str(exchange)
        return sid
   
def decode_args(argv) -> str:
    global sync_position
    global sync_trade
    update_trade_date = ''
    try:
      opts, args = getopt.getopt(argv,"het:p:",["help", "--update_trade_date", "sync_position"])
    except getopt.GetoptError:
        print ('ft_fix.py -e 20221201 -c T')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('ft_fix.py -e 20221201 -t T -p T')
            sys.exit()
        elif opt in ("-e", "--update_trade_date"):
            update_trade_date = arg
        elif opt in ("-p" "sync_position"):
            if arg == 'T' or arg == 't':
                sync_position = True
            elif arg == 'F' or arg == 'f':
                sync_position = False
            else:
                print("input T/F")
                sys.exit()
        elif opt in ("-t" "sync_trade"):
            if arg == 'T' or arg == 't':
                sync_trade = True
            elif arg == 'F' or arg == 'f':
                sync_trade = False
            else:
                print("input T/F")
                sys.exit()
            
    print (f"update_trade_date={update_trade_date}")
    return update_trade_date
                
if __name__ == "__main__":
    update_trade_date = decode_args(sys.argv[1:])
    configfilename = 'ft_fix_setting.json'
    path = os.path.dirname(os.path.abspath(__file__))
    config_filename = os.path.abspath(
        os.path.join(path, './', configfilename))  # 配置文件名&路径

    td = ft_fix(config_filename, update_trade_date)
    td.start()  
