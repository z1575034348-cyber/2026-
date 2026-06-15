import json,os,sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def nd(i,c,e,w,intro,sal,club,g,v=18,m=False):
    return{"id":i,"label":f"{c}\n({e})","image":"","wiki":w,"title":f"简介：{intro}\n薪资：{sal}\n现役：{club}","group":g,"value":v,"isMain":m}
def R(f,t,l,w,s,d=""):return{"from":f,"to":t,"label":l,"color":"#ff4d4f","width":w,"relationType":"red","summary":s,"details":d}
def G(f,t,l,w,s):return{"from":f,"to":t,"label":l,"color":"#56d364","width":w,"relationType":"green","summary":s}
def Gd(f,t,l,w,s):return{"from":f,"to":t,"label":l,"color":"#e3b341","width":w,"relationType":"gold","summary":s}
def W(f,t,l,s):return{"from":f,"to":t,"label":l,"color":"#8b949e","width":1.5,"relationType":"white","summary":s}
def S(i,n,p,e):
    d={"teamName":n+"国家队","teamNameEn":n+" National Football Team","totalNodes":len(p),"totalEdges":len(e),"nodes":p,"edges":e}
    with open(f"data/{i}_data.json","w",encoding="utf-8") as f:json.dump(d,f,ensure_ascii=False,indent=2)
    print(f"  {i}: {len(p)}人/{len(e)}线")

# 墨西哥
MX_P=[nd(1,"奥乔亚","Ochoa","Guillermo_Ochoa","世界杯专业户不老门神","€2M","萨勒尼塔纳","goalkeeper",24),
nd(2,"马拉贡","Malagon","Luis_Malagon","美洲队新生代","€0.8M","美洲队","goalkeeper",14),
nd(3,"阿尔瓦雷斯","E.Alvarez","Edson_Alvarez","西汉姆后腰墨西哥队长","£120K","西汉姆联","midfielder",26,True),
nd(4,"蒙特斯","Montes","Cesar_Montes","阿尔梅里亚中卫","€2M","阿尔梅里亚","defender",20),
nd(5,"巴斯克斯","Vasquez","Johan_Vasquez","热那亚中卫","€1.5M","热那亚","defender",18),
nd(6,"阿特亚加","Arteaga","Gerardo_Arteaga","亨克左后卫","€1M","亨克","defender",16),
nd(7,"桑切斯","J.Sanchez","Jorge_Sanchez","波尔图右后卫","€1.5M","波尔图","defender",16),
nd(8,"洛萨诺","Lozano","Hirving_Lozano","墨西哥天王埃因霍温","€4M","埃因霍温","forward",24),
nd(9,"希门尼斯","S.Gimenez","Santiago_Gimenez","米兰锋霸荷甲金靴","€4M","AC米兰","forward",24),
nd(10,"安图纳","Antuna","Uriel_Antuna","蓝十字边锋","€1.5M","蓝十字","forward",18),
nd(11,"皮内达","Pineda","Orbelin_Pineda","塞尔塔中场","€2M","塞尔塔","midfielder",18),
nd(12,"查韦斯","Chavez","Luis_Chavez","莫斯科迪纳摩","€2M","莫斯科迪纳摩","midfielder",17),
nd(13,"奎尼奥内斯","Quinones","Julian_Quinones","美洲队归化前锋","€1.8M","美洲队","forward",18),
nd(14,"马丁","H.Martin","Henry_Martin","美洲队老中锋","€1.5M","美洲队","forward",17),
nd(15,"维加","Vega","Alexis_Vega","托卢卡","€1.2M","托卢卡","forward",16),
nd(16,"罗莫","Romo","Luis_Romo","蓝十字后腰","€1.5M","蓝十字","midfielder",15),
nd(17,"阿吉雷","Aguirre","Javier_Aguirre","墨西哥老帅三进宫","€3M","墨西哥国家队","coach",22,True)]
MX_E=[R(15,17,"派对丑闻",3.5,"墨西哥球员赛前派对文化","<b>【赛前派对专业户】</b><br><br>墨西哥队大赛前夕狂野派对的优良传统。<br><br><b>📰 《环球报》</b>"),
G(3,4,"队长组合",3,"阿尔瓦雷斯+蒙特斯中后场核心"),
G(8,9,"锋线双星",3,"洛萨诺+希门尼斯欧洲锋线"),
Gd(17,3,"队长信任",2.5,"阿吉雷以阿尔瓦雷斯为队长"),
W(4,5,"中卫","蒙特斯+巴斯克斯"),W(6,7,"边后卫","阿特亚加+桑切斯")]
S("mexico","墨西哥",MX_P,MX_E)

# 喀麦隆
CM_P=[nd(1,"奥纳纳","Onana","Andre_Onana","曼联门将最具争议","£180K","曼联","goalkeeper",26,True),
nd(2,"埃普西","Epassy","Devis_Epassy","沙特二门","€1M","艾卜哈","goalkeeper",14),
nd(3,"卡斯特列托","Castelletto","Jean-Charles_Castelletto","南特后防核心","€1.5M","南特","defender",20),
nd(4,"图洛","Tolo","Nouhou_Tolo","西雅图左后卫","€1M","西雅图海湾人","defender",16),
nd(5,"伍","Wooh","Christopher_Wooh","雷恩中卫","€1.5M","雷恩","defender",17),
nd(6,"恩加德乌","Ngadeu","Michael_Ngadeu-Ngadjui","北京国安老中卫","€2M","北京国安","defender",16),
nd(7,"安古伊萨","Anguissa","Andre-Frank_Zambo_Anguissa","那不勒斯B2B之王","€4M","那不勒斯","midfielder",24),
nd(8,"洪拉","Hongla","Martin_Hongla","维罗纳中场","€1M","维罗纳","midfielder",15),
nd(9,"恩查姆","Ntcham","Olivier_Ntcham","斯旺西中场","€1.5M","斯旺西","midfielder",16),
nd(10,"舒波-莫廷","Choupo-Moting","Eric_Maxim_Choupo-Moting","拜仁纽约传奇","€5M","纽约红牛","forward",22),
nd(11,"阿布巴卡尔","Aboubakar","Vincent_Aboubakar","喀麦隆队长","€2.5M","贝西克塔斯","forward",22),
nd(12,"埃坎比","Ekambi","Karl_Toko_Ekambi","雷恩边锋","€2M","雷恩","forward",18),
nd(13,"姆贝乌莫","Mbeumo","Bryan_Mbeumo","布伦特福德边锋","£80K","布伦特福德","forward",20),
nd(14,"巴索戈","Bassogog","Christian_Bassogog","安卡拉力量边锋","€2M","安卡拉力量","forward",16),
nd(15,"恩库杜","Nkoudou","Georges-Kevin_Nkoudou","达马克边锋","€1.5M","达马克","forward",15),
nd(16,"内尤","Neyou","Yvan_Neyou","圣埃蒂安","€0.8M","圣埃蒂安","midfielder",14),
nd(17,"埃托奥","Eto","Samuel_Eto","传奇巨星足协主席","主席","喀麦隆足协","coach",28,True)]
CM_E=[R(1,17,"开除事件",4.5,"埃托奥世界杯期间直接开除奥纳纳","<b>【足协主席的独裁】</b><br><br>2022世界杯埃托奥直接命令开除奥纳纳。奥纳纳愤而退队。<br><br><b>📰 BBC Sport Africa</b>"),
R(11,17,"队长反抗",2.5,"阿布巴卡尔公开质疑埃托奥过度干预"),
G(7,10,"那不勒斯连线",2.5,"安古伊萨+舒波莫廷"),
G(11,13,"锋线搭档",2.5,"阿布巴卡尔+姆贝乌莫"),
Gd(17,10,"传奇效应",2.5,"埃托奥的传奇地位对球员影响"),
W(3,5,"后防","卡斯特列托+伍"),W(8,16,"中场","洪拉+内尤")]
S("cameroon","喀麦隆",CM_P,CM_E)

# 塞尔维亚
RS_P=[nd(1,"拉伊科维奇","Rajkovic","Predrag_Rajkovic","吉达联合门神","€3M","吉达联合","goalkeeper",22),
nd(2,"瓦尼亚","Vanja","Vanja_Milinkovic-Savic","都灵巨入门将","€1.5M","都灵","goalkeeper",18),
nd(3,"米伦科维奇","Milenkovic","Nikola_Milenkovic","诺丁汉森林铁卫","£85K","诺丁汉森林","defender",22),
nd(4,"帕夫洛维奇","S.Pavlovic","Strahinja_Pavlovic","米兰后防野兽","€3M","AC米兰","defender",20),
nd(5,"韦利科维奇","Veljkovic","Milos_Veljkovic","不莱梅中卫","€1.5M","不莱梅","defender",17),
nd(6,"日夫科维奇","Zivkovic","Andrija_Zivkovic","PAOK右路核心","€2M","PAOK","midfielder",22),
nd(7,"米林科维奇","SMS","Sergej_Milinkovic-Savic","塞尔维亚天王","€25M","利雅得新月","midfielder",26,True),
nd(8,"塔迪奇","Tadic","Dusan_Tadic","塞尔维亚传奇","€4M","费内巴切","forward",24),
nd(9,"弗拉霍维奇","Vlahovic","Dusan_Vlahovic","尤文亿元中锋","€7M","尤文","forward",26,True),
nd(10,"米特罗维奇","Mitrovic","Aleksandar_Mitrovic","塞尔维亚射手王","€25M","利雅得新月","forward",24),
nd(11,"约维奇","Jovic","Luka_Jovic","米兰失意天才","€3M","AC米兰","forward",18),
nd(12,"科斯蒂奇","Kostic","Filip_Kostic","尤文左路天尊","€4M","尤文","midfielder",20),
nd(13,"卢基奇","Lukic","Sasa_Lukic","富勒姆中场","£70K","富勒姆","midfielder",17),
nd(14,"萨马尔季奇","Samardzic","Lazar_Samardzic","亚特兰大新星","€2M","亚特兰大","midfielder",18),
nd(15,"拉多尼奇","Radonjic","Nemanja_Radonjic","马洛卡边锋","€1.5M","马洛卡","forward",16),
nd(16,"格鲁伊奇","Grujic","Marko_Grujic","波尔图后腰","€2M","波尔图","midfielder",16),
nd(17,"斯托伊科维奇","Stojkovic","Dragan_Stojkovic","广州城前主帅","€2M","塞尔维亚国家队","coach",20,True)]
RS_E=[R(9,10,"太太团互绿",4.5,"弗拉霍维奇与米特罗维奇太太团罗生门","<b>【太太团乱战】</b><br><br>2022世界杯爆出某主力球员妻子与队友有染。<br><br><b>📰 《闪电报》；《每日邮报》</b>"),
G(7,10,"新月连线",2.5,"米林科维奇+米特罗维奇"),
G(9,12,"尤文连线",2,"弗拉霍维奇+科斯蒂奇"),
Gd(17,8,"队长信任",2.5,"斯托伊科维奇以塔迪奇为领袖"),
W(3,4,"中卫","米伦科维奇+帕夫洛维奇"),W(13,14,"中场","卢基奇+萨马尔季奇")]
S("serbia","塞尔维亚",RS_P,RS_E)

# 乌拉圭
UY_P=[nd(1,"罗切特","Rochet","Sergio_Rochet","巴西国际门神","€1.5M","巴西国际","goalkeeper",22),
nd(2,"梅莱","Mele","Santiago_Mele","巴列卡诺二门","€1M","巴列卡诺","goalkeeper",15),
nd(3,"阿劳霍","Araujo","Ronald_Araujo","巴萨后防野兽","£220K","巴萨","defender",26,True),
nd(4,"希门尼斯","Gimenez","Jose_Maria_Gimenez","马竞铁血中卫","€5M","马竞","defender",24),
nd(5,"卡塞雷斯","Caceres","Martin_Caceres","洛杉矶银河老将","€1M","洛杉矶银河","defender",16),
nd(6,"比尼亚","Vina","Matias_Vina","罗马左后卫","€2M","罗马","defender",17),
nd(7,"奥利维拉","Olivera","Mathias_Olivera","那不勒斯左后卫","€2M","那不勒斯","defender",17),
nd(8,"皮克雷斯","Piquerez","Joaquin_Piquerez","帕尔梅拉斯右后卫","€1.5M","帕尔梅拉斯","defender",16),
nd(9,"巴尔韦德","Valverde","Federico_Valverde","皇马引擎未来领袖","£250K","皇马","midfielder",28,True),
nd(10,"乌加特","Ugarte","Manuel_Ugarte","曼联抢断王","£120K","曼联","midfielder",22),
nd(11,"本坦库尔","Bentancur","Rodrigo_Bentancur","热刺中场","£130K","热刺","midfielder",22),
nd(12,"德拉克鲁斯","De la Cruz","Nicolas_de_la_Cruz","弗拉门戈核心","€4M","弗拉门戈","midfielder",22),
nd(13,"德阿拉斯卡埃塔","De Arrascaeta","Giorgian_de_Arrascaeta","弗拉门戈魔术师","€3M","弗拉门戈","midfielder",20),
nd(14,"努涅斯","Nunez","Darwin_Nunez","利物浦亿元先生","£180K","利物浦","forward",26,True),
nd(15,"苏亚雷斯","Suarez","Luis_Suarez","乌拉圭传奇","€5M","迈阿密国际","forward",24),
nd(16,"佩利斯特里","Pellistri","Facundo_Pellistri","曼联边锋","£60K","曼联","forward",17),
nd(17,"卡诺比奥","Canobbio","Agustin_Canobbio","巴拉纳竞技","€1.5M","巴拉纳竞技","forward",16),
nd(18,"马克西戈麦斯","M.Gomez","Maxi_Gomez","特拉布宗体育","€2M","特拉布宗体育","forward",17),
nd(19,"法昆多托雷斯","F.Torres","Facundo_Torres","奥兰多城新星","€1.2M","奥兰多城","forward",16),
nd(20,"贝尔萨","Bielsa","Marcelo_Bielsa","疯子教练魔鬼训练","€4M","乌拉圭国家队","coach",26,True)]
UY_E=[R(14,20,"魔鬼训练",3.5,"努涅斯等对贝尔萨极端训练不满","<b>【疯子教练的魔鬼训练】</b><br><br>贝尔萨每天训练超6小时。受不了就走人。<br><br><b>📰 《国家报》</b>"),
R(15,20,"老将边缘化",2.5,"苏亚雷斯在贝尔萨体系逐渐被边缘化"),
G(9,10,"乌拉圭新核",3,"巴尔韦德+乌加特皇马曼联中场"),
G(3,4,"铁血防线",2.5,"阿劳霍+希门尼斯西甲双塔"),
G(12,13,"弗拉门戈双核",2.5,"德拉克鲁斯+德阿拉斯卡埃塔"),
Gd(20,9,"战术灵魂",3,"贝尔萨以巴尔韦德为绝对核心"),
W(6,7,"左后卫","比尼亚+奥利维拉"),W(16,17,"边锋","佩利斯特里+卡诺比奥")]
S("uruguay","乌拉圭",UY_P,UY_E)

print("\n=== 全部16支球队扩充完成 ===")
import os
for f in os.listdir('data'):
    if f.endswith('.json'):
        with open(f'data/{f}','r',encoding='utf-8') as fh:
            d=json.load(fh)
        print(f"  {f}: {d['totalNodes']}人/{d['totalEdges']}线")
