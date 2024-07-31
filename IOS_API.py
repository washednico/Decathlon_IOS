import requests
from bs4 import BeautifulSoup as bs
import threading
from datetime import datetime
import time
from time import sleep
import copy
from discord_webhook import DiscordEmbed, DiscordWebhook
import random



















def api(url_to_send,file,delay,mode,tasks,role_tag,webhook_url,pid,name,image):

    time.sleep(random.randint(0,3))
    headers_api = {
    "Host": "iec6q6rv56.execute-api.eu-west-1.amazonaws.com",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-api-key": "fpaU3F5Xjw5H5SovhDziv1H5o4UiTTRV563FntAH",
    "x-mobileapp-os": "ios",
    "x-mobileapp-version": "4.11.1",
    
    "Accept-Language": "it-it",
    "User-Agent": "Decathlon/4487 CFNetwork/1206 Darwin/20.1.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
    }

    try:
        file_to_open = open(file,"r+")
        initial_stock = int(file_to_open.read())
        file_to_open.close()
    except:
        file_to_open = open(file,"w+")
        file_to_open.write("5")
        initial_stock = 5
        file_to_open.close()

    
    list_proxy_good = []
    file_proxy = open("proxy.txt","r+")
    list_proxy = file_proxy.read()
    file_proxy.close()
    list_proxy = list_proxy.split("\n")

    for i in list_proxy:
        info = i.split(":")
        proxie = "http://"+info[2]+":"+info[3]+"@"+info[0]+":"+info[1]
        list_proxy_good.append(proxie)



    while True:

        

        while True:
            try:
                
                
                
                time.sleep(delay)
                
                url = "https://iec6q6rv56.execute-api.eu-west-1.amazonaws.com/v1/stocks/env/5/skus/"+pid
                proxie_to_use_info = random.choice(list_proxy_good)
                proxies = {"https" : proxie_to_use_info.replace("https","http")}
                
                scrape = requests.get(url,timeout=(2,3),headers=headers_api,proxies=proxies)
                
                if scrape.status_code==200:
                    page_content = str(bs(scrape.content,"lxml"))
                    print(page_content)
                    
                    index_value = page_content.find("stock\":")
                    
                    value_text = page_content[index_value+7:index_value+12]
                    
                    
                    
                    value = int(value_text.replace(",","").replace("\"","").replace("a","").replace("v","").replace("u","").replace("I",""))
                
                    break
                
                else:
                    status_send = str(scrape.status_code)
                    webhook = DiscordWebhook(url="xxxx", content = status_send)
                    
                    webhook.execute()
                    time.sleep(1)
                    try:
                        command_print = "["+datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')+"]"+"  [TASK "+tasks+"]"+"  [STATUS "+str(scrape.status_code)+"]  "+"[STOCK "+str(value)+"]"
                        print(command_print)
                    except:
                        None

            except Exception as e:
                error = str(e)+"\n"+str(page_content)+str(scrape)
                webhook = DiscordWebhook(url="xxxxx", content = error)
                            
                webhook.execute()
                time.sleep(1)
                try:
                    command_print = "["+datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')+"]"+"  [TASK "+tasks+"]"+"  [STATUS "+str(scrape.status_code)+"]  "+"[STOCK "+str(value)+"]"
                    print(command_print)
                except:
                    None
                
        
        
        try:
            command_print = "["+datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')+"]"+"  [TASK "+tasks+"]"+"  [STATUS "+str(scrape.status_code)+"]  "+"[STOCK "+str(value)+"]"
            print(command_print)
        except:
            None
        
        
        
        #webhookkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
        
        
        if (value != initial_stock and initial_stock == 0) or (value!=initial_stock and value==0) :
            
                if (value != initial_stock and initial_stock == 0):
                        message = "**"+"RESTOCK DETECTED ON API ENDPOINT"+"**\n"+"NEW STOCK: "+str(value)+"\n\nCheck frontpage monitor"
                        webhook = DiscordWebhook(url=webhook_url)
                        embed = DiscordEmbed(title=name.upper(), description=message, color=16776960,url = url_to_send)
                        embed.set_thumbnail(url=image)
                        embed.set_footer(text='Developed by Sugo with API endpoint\nSugochat exclusive V. 0.7.1 | proxy: on', icon_url='')
                        webhook.add_embed(embed)
                        response = webhook.execute()
                        if (value != initial_stock and initial_stock == 0):
                            file_to_open = open(file,"r+")
                            initial_stock = int(file_to_open.read())
                            file_to_open.close()
                            if (value != initial_stock and initial_stock == 0):

                            
                                webhook = DiscordWebhook(url=webhook_url, content = role_tag)
                                
                                response = webhook.execute()
                                try:
                                    webhook = DiscordWebhook(url="xxxx", content = page_content)
                                    
                                    response = webhook.execute()
                                except:
                                    None

                        
                        
                
                
                initial_stock = copy.deepcopy(value)
                file_to_open = open(file,"w+")
                file_to_open.write(str(initial_stock))
                file_to_open.close()
                time.sleep(5)
        
        
        
        
        


                

    

def start():
    pw = input()
    if pw == "1":
        print("",end="\r")
        
        file = open("TASKS.CSV","r+")
        lines = file.readlines()
        counter=0
        for i in lines:
            if counter == 0:
                counter=counter+1
                None
            else:
                info = i.split(",")
                url = info[0]
                mode = info[1]
                tasks = info[2] 
                delay = float(info[3])
                file = info[4]
                role = info[5].replace("\n","")
                webhook_url = info[6].replace("\n","")
                pid = info[7].replace("\n","")
                name = info[8].replace("\n","")
                image = info[9].replace("\n","")
                
                

                if role=="MANUBRI":
                    role_tag="<@&12233233233>"
                if role=="BILANCIERE":
                    role_tag="<@&1223323362333>"
                if role=="ALTRO":
                    role_tag="<@&122334233233>"
                if role=="PANCA":
                    role_tag="<@&122332335233>"
                if role== "DISCHI":
                    role_tag ="<@&122337233233>"
                

                file_to_open = str(file+".txt").replace("\n","")
                
                
                threading.Thread(target=api, kwargs={
                                                    "url_to_send":url,
                                                    "file":file_to_open,
                                                    "delay":delay,
                                                    "mode":mode,
                                                    "tasks":tasks,
                                                    
                                                    "role_tag":role_tag,
                                                    "webhook_url": webhook_url,
                                                    "pid":pid,
                                                    "image":image,
                                                    "name":name
                                                    
                    }).start()

            





start()