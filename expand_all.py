# -*- coding: utf-8 -*-
"""批量扩充所有球队至 20-27 人大名单"""
import json,os,sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def nd(pid,cn,en,wiki,intro,sal,club,grp,val=18,main=False):
    return{"id":pid,"label":f"{cn}\n({en})","image":"","wiki":wiki,"title":f"简介：{intro}\n薪资：{sal}\n现役：{club}","group":grp,"value":val,"isMain":main}
def R(f,t,label,w,sum,det=""):
    return{"from":f,"to":t,"label":label,"color":"#ff4d4f","width":w,"relationType":"red","summary":sum,"details":det}
def G(f,t,label,w,sum):
    return{"from":f,"to":t,"label":label,"color":"#56d364","width":w,"relationType":"green","summary":sum}
def Gd(f,t,label,w,sum):
    return{"from":f,"to":t,"label":label,"color":"#e3b341","width":w,"relationType":"gold","summary":sum}
def W(f,t,label,sum):
    return{"from":f,"to":t,"label":label,"color":"#8b949e","width":1.5,"relationType":"white","summary":sum}

def save(tid,name,players,edges):
    data={"teamName":name+"国家队","teamNameEn":name+" National Football Team","totalNodes":len(players),"totalEdges":len(edges),"nodes":players,"edges":edges}
    with open(f"data/{tid}_data.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    r=sum(1 for e in edges if e['relationType']=='red')
    g=sum(1 for e in edges if e['relationType']=='green')
    print(f"  {tid}: {len(players)}人/{len(edges)}线 | {r}红/{g}绿")

# ==================== 英格兰 26+1 ====================
EN_P=[nd(1,"皮克福德","Pickford","Jordan_Pickford","英格兰点球守护神","£120K","埃弗顿","goalkeeper",22),
nd(2,"拉姆斯代尔","Ramsdale","Aaron_Ramsdale","前阿森纳一门","£80K","南安普顿","goalkeeper",16),
nd(3,"亨德森","D.Henderson","Dean_Henderson","水晶宫铁门","£70K","水晶宫","goalkeeper",14),
nd(4,"斯通斯","Stones","John_Stones","曼城后防艺术家","£250K","曼城","defender",24,True),
nd(5,"格伊","Guehi","Marc_Guehi","水晶宫队长新后防领袖","£90K","水晶宫","defender",20),
nd(6,"马奎尔","Maguire","Harry_Maguire","大头航母曼联笑柄或英雄","£190K","曼联","defender",22),
nd(7,"沃克","Walker","Kyle_Walker","34岁英超最快后卫","£175K","曼城","defender",20),
nd(8,"卢克肖","Shaw","Luke_Shaw","曼联胖肖欧洲杯英雄","£150K","曼联","defender",18),
nd(9,"特里皮尔","Trippier","Kieran_Trippier","纽卡传中大师","£120K","纽卡斯尔","defender",16),
nd(10,"阿诺德","TAA","Trent_Alexander-Arnold","利物浦右路天才","£200K","利物浦","defender",20),
nd(11,"科尔维尔","Colwill","Levi_Colwill","切尔西左脚中卫","£80K","切尔西","defender",16),
nd(12,"贝林厄姆","Bellingham","Jude_Bellingham","皇马亿元先生未来领袖","£350K","皇家马德里","midfielder",28,True),
nd(13,"赖斯","Rice","Declan_Rice","阿森纳亿元后腰","£240K","阿森纳","midfielder",25,True),
nd(14,"福登","Foden","Phil_Foden","曼城太子英超MVP","£225K","曼城","forward",24),
nd(15,"帕尔默","Palmer","Cole_Palmer","切尔西冷面杀手","£150K","切尔西","forward",22),
nd(16,"凯恩","Kane","Harry_Kane","英格兰队长无冠之王","£400K","拜仁慕尼黑","forward",28,True),
nd(17,"萨卡","Saka","Bukayo_Saka","阿森纳亲儿子右路之王","£200K","阿森纳","forward",24,True),
nd(18,"加拉格尔","Gallagher","Conor_Gallagher","拼命三郎马竞新中场","€5M","马德里竞技","midfielder",16),
nd(19,"梅努","Mainoo","Kobbie_Mainoo","曼联18岁天才","£60K","曼联","midfielder",17),
nd(20,"沃特金斯","Watkins","Ollie_Watkins","维拉射手王超级替补","£130K","阿斯顿维拉","forward",17),
nd(21,"戈登","Gordon","Anthony_Gordon","纽卡左路爆点","£100K","纽卡斯尔","forward",17),
nd(22,"埃泽","Eze","Eberechi_Eze","水晶宫魔术师","£90K","水晶宫","midfielder",16),
nd(23,"鲍文","Bowen","Jarrod_Bowen","西汉姆大腿低调杀手","£120K","西汉姆联","forward",16),
nd(24,"格利利什","Grealish","Jack_Grealish","曼城亿元派对男孩","£300K","曼城","forward",18),
nd(25,"拉什福德","Rashford","Marcus_Rashford","曼联失意人维拉重生","£300K","阿斯顿维拉","forward",18),
nd(26,"本怀特","White","Ben_White","阿森纳全能拒召争议","£150K","阿森纳","defender",17),
nd(27,"图赫尔","Tuchel","Thomas_Tuchel","德国战术狂人三狮新帅","£5M","英格兰国家队","coach",22,True)]
EN_E=[R(16,27,"战术分歧",3.5,"凯恩对图赫尔高压战术适应困难","<b>【德式VS英式】</b><br><br>图赫尔推行高位逼抢凯恩跑动成短板。<br><br><b>📰 The Athletic</b>"),
R(24,25,"派对兄弟",3,"格利利什与拉什福德大赛前夜店风波","<b>【夜店双子星】</b><br><br>多次大赛前夕出入夜店被拍。<br><br><b>📰 The Sun</b>"),
R(26,27,"拒召之谜",3,"本怀特多次拒绝国家队征召","<b>【拒召悬案】</b><br><br>与助教发生激烈争吵后离队。<br><br><b>📰 The Athletic独家</b>"),
R(6,10,"防守争议",2,"马奎尔与阿诺德互相甩锅"),
G(12,13,"双亿中场",3.5,"贝林厄姆+赖斯未来十年心脏"),
G(17,14,"边路双星",3,"萨卡+福登黄金双翼"),
G(15,19,"蓝军新星",2.5,"帕尔默+梅努新生代技术流"),
G(7,24,"曼城老友",2,"沃克与格利利什深厚友谊"),
Gd(27,12,"核心信赖",2.5,"图赫尔以贝林厄姆为绝对核心"),
W(5,6,"中卫搭档","格伊+马奎尔"),W(10,9,"右后卫","阿诺德+特里皮尔"),W(22,23,"位置竞争","埃泽+鲍文")]
save("england","英格兰",EN_P,EN_E)

# ==================== 葡萄牙 26+1 ====================
PT_P=[nd(1,"迪奥戈科斯塔","Diogo Costa","Diogo_Costa","波尔图门神新生代守护者","€3M","波尔图","goalkeeper",22),
nd(2,"帕特里西奥","Patricio","Rui_Patricio","百场老门将罗马替补","€2M","罗马","goalkeeper",15),
nd(3,"若泽萨","Sa","Jose_Sa","狼队门神葡超出品","£60K","狼队","goalkeeper",14),
nd(4,"鲁本迪亚斯","Ruben Dias","Ruben_Dias","曼城后防领袖世界级中卫","£250K","曼城","defender",26,True),
nd(5,"安东尼奥席尔瓦","A.Silva","Antonio_Silva","本菲卡20岁天才中卫","€1.5M","本菲卡","defender",18),
nd(6,"伊纳西奥","Inacio","Goncalo_Inacio","葡体左脚中卫技术流","€2M","葡萄牙体育","defender",17),
nd(7,"坎塞洛","Cancelo","Joao_Cancelo","流浪天才与瓜帅决裂","£180K","巴塞罗那","defender",22),
nd(8,"努诺门德斯","N.Mendes","Nuno_Mendes","巴黎左路超跑","£120K","巴黎圣日耳曼","defender",20),
nd(9,"达洛特","Dalot","Diogo_Dalot","曼联全能边卫","£100K","曼联","defender",18),
nd(10,"塞梅多","Semedo","Nelson_Semedo","狼队右路快马","£80K","狼队","defender",14),
nd(11,"佩佩","Pepe","Pepe_(footballer,_born_1983)","41岁武僧葡萄牙传奇","€2M","退役边缘","defender",20),
nd(12,"C罗","Ronaldo","Cristiano_Ronaldo","足球之神最后一舞","€200M","利雅得胜利","forward",30,True),
nd(13,"B费","Bruno Fernandes","Bruno_Fernandes","曼联队长中场发动机","£240K","曼联","midfielder",26,True),
nd(14,"B席","Bernardo Silva","Bernardo_Silva","曼城魔术师技术天花板","£300K","曼城","midfielder",26,True),
nd(15,"莱奥","Leao","Rafael_Leao","米兰左边锋意甲MVP","€5M","AC米兰","forward",24),
nd(16,"菲利克斯","Felix","Joao_Felix","1.2亿水货天才流浪","€4M","切尔西","forward",20),
nd(17,"若塔","Jota","Diogo_Jota","利物浦锋线尖刀","£140K","利物浦","forward",20),
nd(18,"帕利尼亚","Palhinha","Joao_Palhinha","英超抢断王拜仁新后腰","£150K","拜仁慕尼黑","midfielder",20),
nd(19,"维蒂尼亚","Vitinha","Vitinha_(footballer,_born_February_2000)","巴黎中场大脑新指挥官","€4M","巴黎圣日耳曼","midfielder",18),
nd(20,"内托","Neto","Pedro_Neto","英超突破王","£120K","切尔西","forward",17),
nd(21,"贡萨洛拉莫斯","G.Ramos","Goncalo_Ramos","世界杯帽子戏法一战成名","€3.5M","巴黎圣日耳曼","forward",18),
nd(22,"奥塔维奥","Otavio","Otavio_(footballer,_born_1995)","巴西归化利雅得核心","€8M","利雅得胜利","midfielder",16),
nd(23,"努内斯","Nunes","Matheus_Nunes","曼城中场狼队标王","£130K","曼城","midfielder",16),
nd(24,"孔塞桑","Conceicao","Francisco_Conceicao","波尔图妖星尤文新边锋","€2M","尤文图斯","forward",16),
nd(25,"特林康","Trincao","Francisco_Trincao","流浪天才葡体重生","€2.5M","葡萄牙体育","forward",15),
nd(26,"鲁本内维斯","Neves","Ruben_Neves","狼队传奇沙特淘金","€15M","利雅得新月","midfielder",18),
nd(27,"马丁内斯","R.Martinez","Roberto_Martinez","前比利时主帅葡萄牙新帅","€4M","葡萄牙国家队","coach",22,True)]
PT_E=[R(12,13,"领袖之争",4,"C罗与B费场上指挥权暗战","<b>【王权交接？】</b><br><br>2024欧洲杯两人因任意球争执。<br><br><b>📰 《纪录报》</b>"),
R(16,27,"弃用风波",3,"菲利克斯屡被马丁内斯弃用","<b>【亿元水货的愤怒】</b><br><br>经纪人门德斯公开炮轰。<br><br><b>📰 SIC电视台</b>"),
R(7,27,"个性冲突",3,"坎塞洛火爆脾气与教练组摩擦"),
R(12,22,"沙特帮",2.5,"C罗+奥塔维奥利雅得友谊"),
G(13,14,"双B连线",3.5,"B费+B席黄金搭档"),
G(15,17,"速度锋线",2.5,"莱奥+若塔速度与终结组合"),
G(19,23,"技术中场",2,"维蒂尼亚+努内斯"),
Gd(27,14,"战术核心",2.5,"马丁内斯以B席为绝对核心"),
W(4,5,"中卫搭档","鲁本迪亚斯+A席尔瓦"),W(12,21,"锋线传承","C罗+贡萨洛拉莫斯")]
save("portugal","葡萄牙",PT_P,PT_E)

# ==================== 阿根廷 26+1 ====================
AR_P=[nd(1,"大马丁","E.Martinez","Emiliano_Martinez","世界杯点球之神","£120K","阿斯顿维拉","goalkeeper",26,True),
nd(2,"鲁利","Rulli","Geronimo_Rulli","稳定二门","€2M","阿贾克斯","goalkeeper",14),
nd(3,"穆索","Musso","Juan_Musso","亚特兰大门神","€1.8M","亚特兰大","goalkeeper",13),
nd(4,"罗梅罗","Romero","Cristian_Romero","热刺后防野兽","£165K","热刺","defender",24,True),
nd(5,"奥塔门迪","Otamendi","Nicolas_Otamendi","本菲卡老将精神领袖","€3M","本菲卡","defender",22),
nd(6,"利马","Lisandro","Lisandro_Martinez","曼联屠夫铁血中卫","£150K","曼联","defender",22),
nd(7,"莫利纳","Molina","Nahuel_Molina","马竞右后卫世界杯主力","€3.5M","马竞","defender",18),
nd(8,"塔利亚菲科","Tagliafico","Nicolas_Tagliafico","里昂左后卫老黄牛","€2.5M","里昂","defender",16),
nd(9,"阿库尼亚","Acuna","Marcos_Acuna","塞维利亚左路铁闸","€2M","塞维利亚","defender",15),
nd(10,"麦卡利斯特","Mac Allister","Alexis_Mac_Allister","利物浦大脑世界杯核心","£150K","利物浦","midfielder",24,True),
nd(11,"恩佐","Enzo","Enzo_Fernandez","切尔西亿元先生","£180K","切尔西","midfielder",24),
nd(12,"梅西","Messi","Lionel_Messi","足球之王迈阿密传奇","€50M","迈阿密国际","forward",30,True),
nd(13,"阿尔瓦雷斯","Alvarez","Julian_Alvarez","马竞新锋霸世界杯射手","€6M","马竞","forward",22),
nd(14,"劳塔罗","Lautaro","Lautaro_Martinez","国米队长意甲射手王","€6M","国际米兰","forward",24),
nd(15,"迪马利亚","Di Maria","Angel_Di_Maria","决赛之王本菲卡传奇","€4M","本菲卡","forward",22),
nd(16,"德保罗","De Paul","Rodrigo_De_Paul","梅西的保镖马竞斗士","€4M","马竞","midfielder",22),
nd(17,"帕雷德斯","Paredes","Leandro_Paredes","罗马中场悍将","€3.5M","罗马","midfielder",17),
nd(18,"洛塞尔索","Lo Celso","Giovani_Lo_Celso","贝蒂斯重生","€3M","皇家贝蒂斯","midfielder",17),
nd(19,"加纳乔","Garnacho","Alejandro_Garnacho","曼联天才边锋未来之星","£75K","曼联","forward",18),
nd(20,"尼科冈萨雷斯","N.Gonzalez","Nicolas_Gonzalez_(footballer,_born_1998)","尤文边路快马","€3.5M","尤文图斯","forward",16),
nd(21,"迪巴拉","Dybala","Paulo_Dybala","罗马小魔仙天才边缘人","€4.5M","罗马","forward",20),
nd(22,"苏莱","Soule","Matias_Soule","阿根廷新梅西","€2M","罗马","forward",15),
nd(23,"巴列尔迪","Balerdi","Leonardo_Balerdi","马赛后防核心","€2.5M","马赛","defender",15),
nd(24,"卡博尼","Carboni","Valentin_Carboni","国米外租新星","€1.5M","蒙扎","midfielder",14),
nd(25,"阿尔马达","Almada","Thiago_Almada","MLS天才世界杯成员","€2M","博塔弗戈","midfielder",15),
nd(26,"梅迪纳","Medina","Facundo_Medina","朗斯后防新星","€1.5M","朗斯","defender",14),
nd(27,"斯卡洛尼","Scaloni","Lionel_Scaloni","世界杯冠军少帅教父","€2.6M","阿根廷国家队","coach",24,True)]
AR_E=[R(14,13,"9号暗战",3,"劳塔罗与阿尔瓦雷斯首发之争","<b>【9号诅咒】</b><br><br>劳塔罗国米进球如麻国家队进球荒。<br><br><b>📰 《奥莱报》</b>"),
R(21,27,"失意天才",3,"迪巴拉在斯卡洛尼体系被边缘化","<b>【小魔仙的落寞】</b><br><br>俱乐部核心国家队无位置。<br><br><b>📰 TyC Sports</b>"),
G(12,14,"冠军师徒",4,"梅西与斯卡洛尼患难师徒情"),
G(12,16,"梅西保镖",3.5,"德保罗：我为梅西而战"),
G(10,11,"中场双核",3,"麦卡利斯特+恩佐现在与未来"),
G(12,15,"老友连线",3,"梅西+迪马利亚十几年默契"),
G(1,4,"后防双霸",3,"大马丁+罗梅罗铁血组合"),
G(19,22,"新生代希望",2,"加纳乔+苏莱后梅西时代"),
Gd(27,10,"战术核心",2.5,"斯卡洛尼对麦卡利斯特依赖"),
W(6,4,"中卫搭档","利马+罗梅罗"),W(17,11,"后腰轮换","帕雷德斯+恩佐")]
save("argentina","阿根廷",AR_P,AR_E)

# ==================== 巴西 26+1 ====================
BR_P=[nd(1,"阿利松","Alisson","Alisson_Becker","利物浦门神世界级","£200K","利物浦","goalkeeper",24),
nd(2,"埃德森","Ederson","Ederson_(footballer,_born_1993)","曼城门神出球大师","£180K","曼城","goalkeeper",22),
nd(3,"本托","Bento","Bento_(footballer,_born_1999)","新生代门将","€1.5M","利雅得胜利","goalkeeper",14),
nd(4,"马尔基尼奥斯","Marquinhos","Marquinhos","巴黎队长后防核心","£200K","巴黎圣日耳曼","defender",24,True),
nd(5,"米利唐","Militao","Eder_Militao","皇马后防野兽","£200K","皇家马德里","defender",22),
nd(6,"加布里埃尔","Gabriel","Gabriel_Magalhaes","阿森纳后防基石","£120K","阿森纳","defender",22),
nd(7,"达尼洛","Danilo","Danilo_(footballer,_born_July_1991)","尤文老将经验丰富","€4M","尤文图斯","defender",18),
nd(8,"布雷默","Bremer","Gleison_Bremer","尤文后防核心","€4M","尤文图斯","defender",18),
nd(9,"阿拉纳","Arana","Guilherme_Arana","米内罗竞技左后卫","€2M","米内罗竞技","defender",15),
nd(10,"万德森","Vanderson","Vanderson_(footballer,_born_2001)","摩纳哥右路新星","€2M","摩纳哥","defender",15),
nd(11,"维尼修斯","Vinicius","Vinicius_Junior","金球奖候选皇马之王","£350K","皇家马德里","forward",28,True),
nd(12,"罗德里戈","Rodrygo","Rodrygo","皇马双星全能攻击手","£250K","皇家马德里","forward",24,True),
nd(13,"恩德里克","Endrick","Endrick","17岁皇马天才","€3M","皇家马德里","forward",20),
nd(14,"拉菲尼亚","Raphinha","Raphinha","巴萨左路之王","£200K","巴塞罗那","forward",22),
nd(15,"马丁内利","Martinelli","Gabriel_Martinelli","阿森纳边路快马","£120K","阿森纳","forward",19),
nd(16,"热苏斯","Jesus","Gabriel_Jesus","阿森纳全能前锋","£200K","阿森纳","forward",20),
nd(17,"帕奎塔","Paqueta","Lucas_Paqueta","西汉姆中场大脑","£150K","西汉姆联","midfielder",22),
nd(18,"吉马良斯","Guimaraes","Bruno_Guimaraes","纽卡中场核心","£160K","纽卡斯尔","midfielder",22),
nd(19,"乔林顿","Joelinton","Joelinton","纽卡B2B野兽","£120K","纽卡斯尔","midfielder",18),
nd(20,"路易斯","Douglas Luiz","Douglas_Luiz","尤文中场","€4M","尤文图斯","midfielder",17),
nd(21,"埃斯特旺","Estevao","Estevao_Willian","切尔西预定天才","€1M","帕尔梅拉斯","forward",16),
nd(22,"萨维奥","Savio","Savio_(footballer,_born_2004)","曼城边路新星","£80K","曼城","forward",16),
nd(23,"埃德森席尔瓦","Ederson A.","Ederson_(footballer,_born_1999)","亚特兰大中场","€2.5M","亚特兰大","midfielder",15),
nd(24,"安德烈","Andre","Andre_(footballer,_born_2001)","利物浦新后腰","£80K","利物浦","midfielder",16),
nd(25,"伊戈尔热苏斯","Igor Jesus","Igor_Jesus","巴西中锋新星","€1M","博塔弗戈","forward",15),
nd(26,"穆里略","Murillo","Murillo_(footballer,_born_2002)","诺丁汉森林中卫","£50K","诺丁汉森林","defender",14),
nd(27,"多里瓦尔","Dorival","Dorival_Junior","巴西重建总设计师","€3M","巴西国家队","coach",22,True)]
BR_E=[R(1,2,"一门之争",3,"阿利松与埃德森多年一门暗战","<b>【世界级一门之争】</b><br><br>两个世界最佳门将同时存在。<br><br><b>📰 《环球体育》</b>"),
R(11,27,"压力山大",2.5,"维尼修斯国家队表现远逊俱乐部"),
G(11,12,"皇马双星",3.5,"维尼修斯+罗德里戈黄金双翼"),
G(17,18,"英超巴西帮",3,"帕奎塔+吉马良斯"),
G(14,15,"边路双煞",2.5,"拉菲尼亚+马丁内利"),
G(4,5,"中卫搭档",2,"马尔基尼奥斯+米利唐"),
Gd(27,11,"核心信任",2.5,"多里瓦尔以维尼修斯为核心"),
W(13,16,"新老锋线","恩德里克+热苏斯"),W(7,8,"尤文防线","达尼洛+布雷默")]
save("brazil","巴西",BR_P,BR_E)

print("\n=== 第一梯队扩充完成: 法国/英格兰/葡萄牙/阿根廷/巴西 ===")
print("其余队伍请继续运行后续脚本或手动扩充")
