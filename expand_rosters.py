# -*- coding: utf-8 -*-
"""
扩充所有16支球队的球员名单至26+1完整大名单
使用 Wikipedia 页面名实现客户端头像加载
运行: PYTHONIOENCODING=utf-8 python scripts/expand_rosters.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def nd(pid,cn,en,wiki,intro,sal,club,grp,val=18,main=False):
    return{"id":pid,"label":f"{cn}\n({en})","image":"","wiki":wiki,
    "title":f"简介：{intro}\n薪资：{sal}\n现役：{club}","group":grp,"value":val,"isMain":main}
def red(f,t,label,w,sum,det=""):
    return{"from":f,"to":t,"label":label,"color":"#ff4d4f","width":w,"relationType":"red","summary":sum,"details":det}
def grn(f,t,label,w,sum):
    return{"from":f,"to":t,"label":label,"color":"#56d364","width":w,"relationType":"green","summary":sum}
def gld(f,t,label,w,sum):
    return{"from":f,"to":t,"label":label,"color":"#e3b341","width":w,"relationType":"gold","summary":sum}
def wht(f,t,label,sum):
    return{"from":f,"to":t,"label":label,"color":"#8b949e","width":1.5,"relationType":"white","summary":sum}

with open('teams.json','r',encoding='utf-8') as f: ts=json.load(f)

# ==================== 法国队 26+1 ====================
FR_P=[
nd(1,"迈尼昂","Maignan","Mike_Maignan","米兰门神扑点专家","周薪 £150K","AC米兰","goalkeeper",22),
nd(2,"阿雷奥拉","Areola","Alphonse_Areola","西汉姆联二门","周薪 £80K","西汉姆联","goalkeeper",14),
nd(3,"桑巴","Samba","Brice_Samba","朗斯钢门","年薪 €2M","朗斯","goalkeeper",13),
nd(4,"特奥","Theo Hernandez","Theo_Hernandez","左路超跑攻防一体","周薪 £200K","AC米兰","defender",22,True),
nd(5,"萨利巴","Saliba","William_Saliba","阿森纳后防基石","周薪 £190K","阿森纳","defender",22),
nd(6,"于帕梅卡诺","Upamecano","Dayot_Upamecano","拜仁铁塔偶有短路","周薪 £180K","拜仁慕尼黑","defender",20),
nd(7,"科纳特","Konate","Ibrahima_Konate","利物浦铁卫伤病缠身","周薪 £120K","利物浦","defender",18),
nd(8,"孔德","Kounde","Jules_Kounde","巴萨全能后卫","周薪 £180K","巴塞罗那","defender",19),
nd(9,"克劳斯","Clauss","Jonathan_Clauss","马赛右路传中机器","年薪 €2.5M","马赛","defender",15),
nd(10,"卢卡斯","Lucas H.","Lucas_Hernandez","世界杯冠军左后卫","周薪 £200K","巴黎圣日耳曼","defender",18),
nd(11,"帕瓦尔","Pavard","Benjamin_Pavard","世界杯最佳进球后卫","年薪 €4M","国际米兰","defender",17),
nd(12,"姆巴佩","Mbappe","Kylian_Mbappe","法国队长足坛第一人","周薪 £600K","皇家马德里","forward",30,True),
nd(13,"格列兹曼","Griezmann","Antoine_Griezmann","法国真核马竞队魂","周薪 £300K","马德里竞技","forward",26,True),
nd(14,"登贝莱","Dembele","Ousmane_Dembele","玻璃人天才爆破手","周薪 £250K","巴黎圣日耳曼","forward",20),
nd(15,"穆阿尼","Kolo Muani","Randal_Kolo_Muani","世界杯决赛单刀遗恨","周薪 £200K","巴黎圣日耳曼","forward",18),
nd(16,"图拉姆","M.Thuram","Marcus_Thuram","名将之后国米锋线尖刀","年薪 €4M","国际米兰","forward",19),
nd(17,"巴尔科拉","Barcola","Bradley_Barcola","巴黎青训瑰宝左路新星","年薪 €2M","巴黎圣日耳曼","forward",16),
nd(18,"楚阿梅尼","Tchouameni","Aurelien_Tchouameni","皇马亿元后腰中场屏障","周薪 £200K","皇家马德里","midfielder",22),
nd(19,"卡马文加","Camavinga","Eduardo_Camavinga","皇马万金油天才","周薪 £180K","皇家马德里","midfielder",20),
nd(20,"拉比奥","Rabiot","Adrien_Rabiot","免费之王加盟马赛","年薪 €5.5M","马赛","midfielder",18),
nd(21,"埃梅里","Z.Emery","Warren_Zaire-Emery","18岁巴黎太子","年薪 €3M","巴黎圣日耳曼","midfielder",18),
nd(22,"福法纳","Y.Fofana","Youssouf_Fofana","摩纳哥钢铁后腰","年薪 €2.5M","摩纳哥","midfielder",16),
nd(23,"科曼","Coman","Kingsley_Coman","决赛之王拜仁边路尖刀","周薪 £200K","拜仁慕尼黑","forward",20),
nd(24,"吉鲁","Giroud","Olivier_Giroud","法国队史射手王","年薪 €3M","洛杉矶FC","forward",20),
nd(25,"恩昆库","Nkunku","Christopher_Nkunku","切尔西魔术师伤愈归来","周薪 £180K","切尔西","forward",18),
nd(26,"门迪","F.Mendy","Ferland_Mendy","皇马低调左闸","周薪 £120K","皇家马德里","defender",15),
nd(27,"德尚","Deschamps","Didier_Deschamps","铁腕治军二十载","年薪 €4.5M","法国国家队","coach",22,True),
]
FR_E=[
red(12,27,"话语权之争",4,"姆巴佩成为队长后与德尚的权力博弈","<b>【队长VS主帅：姆巴佩与德尚的暗战】</b><br><br>2023年姆巴佩成为队长后与德尚关系从师徒变为微妙权力博弈。姆巴佩多次公开暗示对战术有不同看法。<br><br><b>📰 实锤：L'Equipe；RMC Sport</b>"),
red(20,21,"马赛-巴黎对立",2.5,"拉比奥自由身加盟马赛引发巴黎系球员不满","<b>【俱乐部恩怨蔓延到国家队】</b><br><br>拉比奥加盟巴黎死敌马赛引发姆巴佩登贝莱等巴黎系球员强烈不满。<br><br><b>📰 实锤：Le Parisien</b>"),
red(13,20,"中场派系",2,"格列兹曼核心派与拉比奥自由派的摩擦"),
red(6,7,"中卫搭档之争",2,"于帕和科纳特在国家队主力位置的暗战"),
grn(12,13,"核心连线",3.5,"姆巴佩+格列兹曼法国黄金组合"),
grn(18,19,"皇马双星",3,"楚阿梅尼+卡马文加皇马中场双子星"),
grn(12,14,"巴黎帮",3,"姆巴佩+登贝莱巴黎双翼"),
grn(13,24,"老友组合",2.5,"格列兹曼与吉鲁的黄金搭档"),
grn(17,25,"新生代",2,"巴尔科拉+恩昆库法国新生代锋线"),
gld(27,24,"冠军信任",2.5,"德尚对吉鲁的绝对信任"),
wht(4,10,"左后卫之争","特奥与卢卡斯的兄弟位置竞争"),
wht(15,16,"锋线轮换","穆阿尼与图拉姆的9号位竞争"),
wht(14,23,"边锋轮换","登贝莱与科曼的右路轮换"),
wht(5,6,"中卫搭档","萨利巴+于帕梅卡诺"),
wht(27,18,"重点培养","德尚对楚阿梅尼的特别信任"),
wht(21,22,"中场新星","埃梅里+福法纳"),
]

# 保存法国
data={"teamName":"法国国家队","teamNameEn":"France National Football Team","totalNodes":27,"totalEdges":len(FR_E),"nodes":FR_P,"edges":FR_E}
with open("data/france_data.json","w",encoding="utf-8") as f:json.dump(data,f,ensure_ascii=False,indent=2)
print(f"🇫🇷 法国: {len(FR_P)}人/{len(FR_E)}线 已保存到 data/")

# 更新 teams.json 中的路径
for t in ts['teams']:
    t['dataFile'] = 'data/' + t['dataFile']
with open('teams.json','w',encoding='utf-8') as f:json.dump(ts,f,ensure_ascii=False,indent=2)
print("teams.json 路径已更新为 data/ 子目录")

# 移动现有数据文件到 data/
import shutil
for fname in os.listdir('.'):
    if fname.endswith('_data.json') and fname != 'team_data.json':
        src=os.path.join('.',fname)
        dst=os.path.join('data',fname)
        if os.path.exists(dst): os.remove(dst)
        shutil.move(src,dst)
        # 不打印太多

print("数据文件已移至 data/ 目录")
print("\n法国队已完成 27 人扩充。其他队伍需逐队扩充，请继续运行后续脚本。")
