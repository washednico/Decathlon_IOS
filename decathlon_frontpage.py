import requests
from bs4 import BeautifulSoup as bs
import threading
from datetime import datetime
import time
from time import sleep
import copy
from discord_webhook import DiscordEmbed, DiscordWebhook
import random
from fake_headers import Headers




def sugo(url,delay,file,mode,tasks,role,role_tag,webhook_url):
    
    
    list_proxy_good = []
    file_proxy = open("proxy.txt","r+")
    list_proxy = file_proxy.read()
    file_proxy.close()
    list_proxy = list_proxy.split("\n")

    for i in list_proxy:
        info = i.split(":")
        proxie = "http://"+info[2]+":"+info[3]+"@"+info[0]+":"+info[1]
        list_proxy_good.append(proxie)


    proxie_to_use_info = random.choice(list_proxy_good)
    proxies = {"https" : proxie_to_use_info.replace("https","http")}


    
    
    try:
        file_to_open = open(file,"r+")
        initial_stock = int(file_to_open.read())
        file_to_open.close()
        if mode == "M":
            total_initial_stock_M = []
    
    except:
        file_to_open = open(file,"w+")
        file_to_open.write("5")
        initial_stock = 5
        print(initial_stock)
        file_to_open.close()
        if mode == "M":
            total_initial_stock_M = []
    
    sex = requests.session()
    while True:
        try:
            headers = Headers(os="mac", headers=True).generate()
            
            scrape = sex.get(url,timeout=5,headers=headers,proxies=proxies)
            page_content = bs(scrape.content,"lxml")
            print(page_content)
            image = page_content.find("source", {"type":"image/webp","media":"(min-width: 1080px)"})['srcset']
            title_name = page_content.find("h1", {'class': 'title--main product-title-right'}).text
            break
        except:
            None
            time.sleep(5)
    
    
    
    
    
    time.sleep(random.randint(0,3))
    if mode == "M":

            while True:
                while True:
                    try:
                        time.sleep(delay)
                        headers = Headers(os="mac", headers=True).generate()
                        scrape = sex.get(url,timeout=5,headers=headers,proxies=proxies)

                        page_content = bs(scrape.content,"lxml")
                        break
                    except Exception as e:
                        try:
                            webhook = DiscordWebhook(url="", content = str(e))

                            response = webhook.execute()
                        except:
                            None
                        
                
                
                try:
                    single_stock=""
                    single_kg=""
                    stock_info = page_content.find_all("li", {"class":"sizes__size"})
                    new_stock_M = []
                    x=0
                    for i in stock_info:
                        if x>1:
                            single_stock= single_stock+i["data-available-quantity"]+"\n"
                            single_kg = single_kg+i["data-weight"]+"\n"
                            if len(total_initial_stock_M) <4:
                                total_initial_stock_M.append(int(i["data-available-quantity"]))

                            new_stock_M.append(int(i["data-available-quantity"]))
                        else:
                            x=x+1
                        
                        
                        
                except Exception as e:
                    try:
                        webhook = DiscordWebhook(url="", content = str(e))

                        response = webhook.execute()
                    except:
                        None
                
                command_print = "["+datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')+"]"+"  [TASK "+tasks+"]"+"  [STATUS "+str(scrape.status_code)+"]  "+"[STOCK "+str(sum(new_stock_M))+"]"
                print(command_print)
                
                if (new_stock_M.count(0) != total_initial_stock_M.count(0)) or (sum(new_stock_M)>sum(total_initial_stock_M)+100 or(sum(new_stock_M)<sum(total_initial_stock_M)-100)):


                    #nostro
                    message = "NEW STOCK: "+str(sum(new_stock_M))
                    webhook = DiscordWebhook(url=webhook_url)
                    embed = DiscordEmbed(title="STOCK LIVE", description=message, color=16384771,url = url)
                    embed.set_thumbnail(url=image)
                    embed.set_footer(text='Developed by Sugo with sugo\nSugochat exclusive V. 0.7 | proxy: on', icon_url='png')
                    embed.add_embed_field(name="KG",value=single_kg,inline=True)
                    embed.add_embed_field(name="STOCK",value=single_stock,inline=True)
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    
                    

                
                    
                

                    total_initial_stock_M = copy.deepcopy(new_stock_M)
                    file_to_open = open(file,"w+")
                    file_to_open.write(str((sum(new_stock_M))))
                    file_to_open.close()
    
    
    if mode == "S":
        while True:
            while True:
                try:
                        
                    time.sleep(delay)
                    headers = Headers(os="mac", headers=True).generate()
                    scrape = sex.get(url,timeout=5,headers=headers,proxies=proxies)
                    page_content = bs(scrape.content,"lxml")
                    stock_info = page_content.find("input", {"type":"hidden","id":"pdm_productdetailsmaincartridge"})['data-pdmjsmodels']
                    index_value = stock_info.find("availableQuantity")
                    value = stock_info[index_value+19:index_value+24]
                    value = int(value.replace(",","").replace("\"","").replace("b","").replace("a",""))
                    command_print = "["+datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')+"]"+"  [TASK "+tasks+"]"+"  [STATUS "+str(scrape.status_code)+"]  "+"[STOCK "+str(value)+"]"
                    print(command_print)
                    
                    break
                except Exception as e:
                    try:
                        webhook = DiscordWebhook(url="", content = str(e))

                        response = webhook.execute()
                    except:
                        None
                                
                        
                

            
            if (initial_stock!=value and value==0) or (initial_stock!=value and initial_stock==0):


                    #nostro
                    message = "**"+title_name.upper()+"**\n"+"NEW STOCK: "+str(value)
                    webhook = DiscordWebhook(url=webhook_url)
                    embed = DiscordEmbed(title="STOCK LIVE", description=message, color=16384771,url = url)
                    embed.set_thumbnail(url=image)
                    embed.set_footer(text='Developed by Sugo with sugo\nSugochat exclusive V. 0.7 | proxy: on', icon_url='')
                    
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    if (value != initial_stock and initial_stock == 0):
                                webhook = DiscordWebhook(url=webhook_url, content = role_tag)
                                
                                response = webhook.execute()
                    
                    

                
                    
                

                    initial_stock = copy.deepcopy(value)
                    file_to_open = open(file,"w+")
                    file_to_open.write(str(initial_stock))
                    file_to_open.close()

        
        
        


                

    

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
                

                if role=="MANUBRI":
                    role_tag="<@&4378487834>"
                if role=="BILANCIERE":
                    role_tag="<@&39430494344>"
                if role=="ALTRO":
                    role_tag="<@&34990349483>"
                if role=="PANCA":
                    role_tag="<@&34983949439>"
                if role== "DISCHI":
                    role_tag ="<@&349394305030494>"
                

                file_to_open = str(file+".txt").replace("\n","")
                
                
                threading.Thread(target=sugo, kwargs={
                                                    "url":url,
                                                    "file":file_to_open,
                                                    "delay":delay,
                                                    "mode":mode,
                                                    "tasks":tasks,
                                                    "role":role,
                                                    "role_tag":role_tag,
                                                    "webhook_url": webhook_url

                    }).start()

            





start()
 


