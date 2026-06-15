# 扩充西班牙/德国/荷兰/意大利/美国/韩国至 20+ 人
import json,os,sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def nd(pid,cn,en,wiki,intro,sal,club,grp,val=18,main=False):
    return{"id":pid,"label":f"{cn}\n({en})","image":"","wiki":wiki,"title":f"简介：{intro}\n薪资：{sal}\n现役：{club}","group":grp,"value":val,"isMain":main}
def R(f,t,l,w,s,d=""):return{"from":f,"to":t,"label":l,"color":"#ff4d4f","width":w,"relationType":"red","summary":s,"details":d}
def G(f,t,l,w,s):return{"from":f,"to":t,"label":l,"color":"#56d364","width":w,"relationType":"green","summary":s}
def Gd(f,t,l,w,s):return{"from":f,"to":t,"label":l,"color":"#e3b341","width":w,"relationType":"gold","summary":s}
def W(f,t,l,s):return{"from":f,"to":t,"label":l,"color":"#8b949e","width":1.5,"relationType":"white","summary":s}
def S(tid,name,pl,el):
    d={"teamName":name+"国家队","teamNameEn":name+" National Football Team","totalNodes":len(pl),"totalEdges":len(el),"nodes":pl,"edges":el}
    with open(f"data/{tid}_data.json","w",encoding="utf-8") as f:json.dump(d,f,ensure_ascii=False,indent=2)
    print(f"  {tid}: {len(pl)}人/{len(el)}线")

# ===== 西班牙 27人 =====
ES_P=[nd(1,"乌奈西蒙","Unai Simon","Unai_Simon","毕尔巴鄂门神点球专家","€4M","毕尔巴鄂竞技","goalkeeper",22),
nd(2,"拉亚","Raya","David_Raya","阿森纳门神金手套","£100K","阿森纳","goalkeeper",18),
nd(3,"雷米罗","Remiro","Alex_Remiro","皇家社会一门","€2.5M","皇家社会","goalkeeper",14),
nd(4,"拉波尔特","Laporte","Aymeric_Laporte","利雅得胜利后防核心","€20M","利雅得胜利","defender",24,True),
nd(5,"勒诺尔芒","Le Normand","Robin_Le_Normand","马竞后防新核","€4M","马竞","defender",20),
nd(6,"库巴西","Cubarsi","Pau_Cubarsi","巴萨17岁天才中卫","€2M","巴萨","defender",18),
nd(7,"卡瓦哈尔","Carvajal","Dani_Carvajal","皇马传奇欧冠决赛之王","£200K","皇马","defender",22),
nd(8,"格里马尔多","Grimaldo","Alejandro_Grimaldo","勒沃库森左路魔术师","€4M","勒沃库森","defender",19),
nd(9,"库库雷利亚","Cucurella","Marc_Cucurella","切尔西左后卫一球成名","£175K","切尔西","defender",18),
nd(10,"维维安","Vivian","Dani_Vivian","毕尔巴鄂中卫新力量","€2M","毕尔巴鄂竞技","defender",15),
nd(11,"纳瓦斯","Navas","Jesus_Navas","39岁不老传说","€1.5M","塞维利亚","defender",16),
nd(12,"罗德里","Rodri","Rodri_(footballer,_born_1996)","金球奖后腰世界第一","£300K","曼城","midfielder",30,True),
nd(13,"佩德里","Pedri","Pedri","巴萨天才技术核心","£150K","巴萨","midfielder",24,True),
nd(14,"加维","Gavi","Gavi_(footballer)","巴萨斗牛犬最硬中场","£120K","巴萨","midfielder",22),
nd(15,"奥尔莫","Olmo","Dani_Olmo","巴萨新10号欧洲杯金靴","€6M","巴萨","midfielder",22),
nd(16,"梅里诺","Merino","Mikel_Merino","阿森纳中场悍将","£150K","阿森纳","midfielder",18),
nd(17,"法比安","Fabian Ruiz","Fabián_Ruiz_Peña","巴黎中场艺术家","€5M","巴黎","midfielder",19),
nd(18,"苏维门迪","Zubimendi","Martin_Zubimendi","拒绝利物浦的男人","€3.5M","皇家社会","midfielder",18),
nd(19,"莫拉塔","Morata","Alvaro_Morata","西班牙队长越位线上的男人","€5M","AC米兰","forward",22),
nd(20,"亚马尔","Yamal","Lamine_Yamal","17岁超新星欧洲杯最年轻","€3M","巴萨","forward",24,True),
nd(21,"尼科","Nico Williams","Nico_Williams","毕尔巴鄂边路超跑","€4M","毕尔巴鄂竞技","forward",22),
nd(22,"费兰","Ferran Torres","Ferran_Torres","巴萨边缘人国家队福将","£150K","巴萨","forward",17),
nd(23,"奥亚萨瓦尔","Oyarzabal","Mikel_Oyarzabal","皇社队长决赛英雄","€4M","皇家社会","forward",19),
nd(24,"何塞卢","Joselu","Joselu","草根射手传奇","€3M","加拉法","forward",16),
nd(25,"皮诺","Pino","Yeremy_Pino","黄潜边锋未来之星","€2.5M","比利亚雷亚尔","forward",16),
nd(26,"萨拉戈萨","Zaragoza","Bryan_Zaragoza","拜仁外租妖星","€2M","奥萨苏纳","forward",14),
nd(27,"德拉富恩特","De la Fuente","Luis_de_la_Fuente_(footballer,_born_1961)","欧洲杯冠军教头青训之父","€2M","西班牙国家队","coach",22,True)]
ES_E=[R(13,14,"巴萨帮vs皇马帮",3.5,"巴萨系与皇马系在国家队微妙角力","<b>【世纪恩怨延续】</b><br><br>巴萨和皇马球员在国家队微妙张力从未消失。<br><br><b>📰 《马卡报》</b>"),
R(19,27,"队长争议",2.5,"莫拉塔队长身份遭球迷媒体质疑","<b>【凭什么当队长？】</b><br><br>德转史上最贵累计转会费球员之一。<br><br><b>📰 《阿斯报》</b>"),
R(12,18,"后腰交替",2,"罗德里伤缺苏维门迪上位引发讨论"),
G(13,14,"巴萨DNA",3,"佩德里+加维黄金搭档"),
G(20,21,"边路双星",3.5,"亚马尔+尼科欧洲杯最恐怖双翼"),
G(21,23,"巴斯克连线",2.5,"尼科+奥亚萨瓦尔巴斯克兄弟"),
G(13,15,"技术双核",2.5,"佩德里+奥尔莫进攻双引擎"),
G(12,17,"世界级中场",2.5,"罗德里+法比安完美互补"),
Gd(27,12,"战术核心",2.5,"德拉富恩特以罗德里为攻防枢纽"),
W(4,5,"中卫搭档","拉波尔特+勒诺尔芒"),W(22,23,"锋线轮换","费兰+奥亚萨瓦尔"),W(6,10,"新中卫","库巴西+维维安")]
S("spain","西班牙",ES_P,ES_E)

# ===== 德国 27人 =====
DE_P=[nd(1,"特尔施特根","ter Stegen","Marc-Andre_ter_Stegen","巴萨门神终获一门","£220K","巴萨","goalkeeper",24),
nd(2,"努贝尔","Nubel","Alexander_Nubel","斯图加特新门神","€3M","斯图加特","goalkeeper",16),
nd(3,"鲍曼","Baumann","Oliver_Baumann","霍芬海姆老门将","€2M","霍芬海姆","goalkeeper",14),
nd(4,"吕迪格","Rudiger","Antonio_Rudiger","皇马后防野兽","£250K","皇马","defender",26,True),
nd(5,"施洛特贝克","Schlotterbeck","Nico_Schlotterbeck","多特后防核心","€4M","多特蒙德","defender",20),
nd(6,"塔","Tah","Jonathan_Tah","勒沃库森铁塔","€4M","勒沃库森","defender",20),
nd(7,"基米希","Kimmich","Joshua_Kimmich","拜仁全能战士","£300K","拜仁","defender",26,True),
nd(8,"亨里希斯","Henrichs","Benjamin_Henrichs","莱比锡右后卫","€3M","莱比锡","defender",17),
nd(9,"米特尔施塔特","Mittelstadt","Maximilian_Mittelstadt","斯图加特左后卫","€2M","斯图加特","defender",16),
nd(10,"劳姆","Raum","David_Raum","莱比锡左路超跑","€3M","莱比锡","defender",17),
nd(11,"穆西亚拉","Musiala","Jamal_Musiala","拜仁天选之子","£250K","拜仁","midfielder",28,True),
nd(12,"维尔茨","Wirtz","Florian_Wirtz","勒沃库森金童","€5M","勒沃库森","midfielder",28,True),
nd(13,"京多安","Gundogan","Ilkay_Gundogan","德国队长曼城传奇","£200K","曼城","midfielder",24,True),
nd(14,"格罗斯","Gross","Pascal_Gross","多特全能老妖","€3M","多特蒙德","midfielder",17),
nd(15,"安德里希","Andrich","Robert_Andrich","勒沃库森铁腰","€2.5M","勒沃库森","midfielder",17),
nd(16,"哈弗茨","Havertz","Kai_Havertz","阿森纳全能王","£280K","阿森纳","forward",24),
nd(17,"萨内","Sane","Leroy_Sane","拜仁边路快马","£300K","拜仁","forward",22),
nd(18,"格纳布里","Gnabry","Serge_Gnabry","拜仁边锋","£220K","拜仁","forward",20),
nd(19,"菲尔克鲁格","Fullkrug","Niclas_Fullkrug","德国大中锋","£130K","西汉姆联","forward",20),
nd(20,"翁达夫","Undav","Deniz_Undav","斯图加特射手","€2.5M","斯图加特","forward",17),
nd(21,"阿德耶米","Adeyemi","Karim_Adeyemi","多特速度狂魔","€3M","多特蒙德","forward",17),
nd(22,"穆勒","Muller","Thomas_Muller","拜仁传奇空间阅读者","£300K","拜仁","forward",22),
nd(23,"戈雷茨卡","Goretzka","Leon_Goretzka","拜仁边缘人心有不甘","£250K","拜仁","midfielder",19),
nd(24,"安东","Anton","Waldemar_Anton","多特中卫","€3M","多特蒙德","defender",15),
nd(25,"贝尔","Beier","Maximilian_Beier","多特新星","€1.5M","多特蒙德","forward",14),
nd(26,"帕夫洛维奇","Pavlovic","Aleksandar_Pavlovic_(footballer)","拜仁青训后腰新星","€1M","拜仁","midfielder",16),
nd(27,"纳格尔斯曼","Nagelsmann","Julian_Nagelsmann","天才少帅战术革新者","€5M","德国国家队","coach",22,True)]
DE_E=[R(7,27,"位置争议",3.5,"基米希不愿踢右后卫长期争议","<b>【我是中场不是右后卫！】</b><br><br>基米希多次公开表示不适合右后卫。<br><br><b>📰 《踢球者》</b>"),
R(23,27,"弃用愤懑",3,"戈雷茨卡被纳格尔斯曼边缘化"),
R(17,27,"态度质疑",2.5,"萨内训练态度屡遭教练组质疑"),
G(11,12,"双子星",4,"穆西亚拉+维尔茨未来十年双核"),
G(13,11,"师徒传承",2.5,"京多安老带新穆西亚拉"),
G(4,6,"后防搭档",2.5,"吕迪格+塔钢铁防线"),
G(7,22,"拜仁传奇",2.5,"基米希+穆勒深厚友谊"),
Gd(27,12,"战术核心",2.5,"纳格尔斯曼以维尔茨为战术引擎"),
W(5,6,"中卫轮换","施洛特贝克+塔"),W(17,18,"边锋轮换","萨内+格纳布里"),W(21,25,"新人竞争","阿德耶米+贝尔")]
S("germany","德国",DE_P,DE_E)

# ===== 荷兰 24人 =====
NL_P=[nd(1,"弗莱肯","Flekken","Mark_Flekken","布伦特福德门神","£60K","布伦特福德","goalkeeper",20),
nd(2,"比洛","Bijlow","Justin_Bijlow","费耶诺德一门","€1.5M","费耶诺德","goalkeeper",16),
nd(3,"奥莱","Olij","Nick_Olij","鹿特丹斯巴达","€0.8M","鹿特丹斯巴达","goalkeeper",13),
nd(4,"范迪克","Van Dijk","Virgil_van_Dijk","荷兰队长世界级中卫","£250K","利物浦","defender",28,True),
nd(5,"德弗赖","De Vrij","Stefan_de_Vrij","国米后防核心","€4M","国际米兰","defender",22),
nd(6,"阿克","Ake","Nathan_Ake","曼城全能后卫","£160K","曼城","defender",22),
nd(7,"德里赫特","De Ligt","Matthijs_de_Ligt","曼联后防新领袖","£200K","曼联","defender",22),
nd(8,"邓弗里斯","Dumfries","Denzel_Dumfries","国米右路超跑","€3.5M","国米","defender",20),
nd(9,"弗林蓬","Frimpong","Jeremie_Frimpong","勒沃库森右路妖星","€4M","勒沃库森","defender",20),
nd(10,"范德文","Van de Ven","Micky_van_de_Ven","热刺左脚超跑","£120K","热刺","defender",20),
nd(11,"德容","De Jong","Frenkie_de_Jong","巴萨中场灵魂","£350K","巴萨","midfielder",26,True),
nd(12,"赖因德斯","Reijnders","Tijjani_Reijnders","米兰中场核心","€3.5M","AC米兰","midfielder",22),
nd(13,"赫拉芬贝赫","Gravenberch","Ryan_Gravenberch","利物浦重生","£130K","利物浦","midfielder",20),
nd(14,"库普梅纳斯","Koopmeiners","Teun_Koopmeiners","尤文中场全能","€4M","尤文图斯","midfielder",20),
nd(15,"加克波","Gakpo","Cody_Gakpo","利物浦锋线多面手","£120K","利物浦","forward",24),
nd(16,"马伦","Malen","Donyell_Malen","维拉边锋","£100K","阿斯顿维拉","forward",19),
nd(17,"德佩","Depay","Memphis_Depay","荷兰队史射手王","€5M","科林蒂安","forward",22),
nd(18,"西蒙斯","Simons","Xavi_Simons","莱比锡天才","€4M","莱比锡","forward",22),
nd(19,"布罗比","Brobbey","Brian_Brobbey","阿贾克斯中锋","€2M","阿贾克斯","forward",18),
nd(20,"贝尔温","Bergwijn","Steven_Bergwijn","沙特淘金边锋","€6M","吉达联合","forward",17),
nd(21,"朗","Lang","Noa_Lang","埃因霍温边锋","€2M","埃因霍温","forward",16),
nd(22,"廷贝尔","Timber","Jurrien_Timber","阿森纳后防天才","£120K","阿森纳","defender",18),
nd(23,"海特勒伊达","Geertruida","Lutsharel_Geertruida","莱比锡后防","€2.5M","莱比锡","defender",16),
nd(24,"科曼","Koeman","Ronald_Koeman","荷兰铁血教头","€3M","荷兰国家队","coach",22,True)]
NL_E=[R(11,24,"战术分歧",3,"德容与科曼战术体系分歧","<b>【巴萨大脑VS荷兰铁腕】</b><br><br>德容坚持组织角色科曼要求防守。<br><br><b>📰 《电讯报》</b>"),
R(8,9,"右路之战",2,"邓弗里斯与弗林蓬首发之争"),
G(4,6,"后防搭档",3,"范迪克+阿克世界级防线"),
G(11,12,"中场双核",3,"德容+赖因德斯"),
G(18,15,"新生代锋线",2.5,"西蒙斯+加克波新黄金一代"),
Gd(24,4,"绝对信任",3,"科曼以范迪克为绝对领袖"),
W(5,7,"中卫","德弗赖+德里赫特"),W(16,21,"边锋","马伦+朗")]
S("netherlands","荷兰",NL_P,NL_E)

# ===== 意大利 24人 =====
IT_P=[nd(1,"多纳鲁马","Donnarumma","Gianluigi_Donnarumma","巴黎门神意大利队长","£250K","巴黎","goalkeeper",26,True),
nd(2,"维卡里奥","Vicario","Guglielmo_Vicario","热刺门神英超金手套","£100K","热刺","goalkeeper",18),
nd(3,"梅雷特","Meret","Alex_Meret","那不勒斯门将","€2M","那不勒斯","goalkeeper",15),
nd(4,"巴斯托尼","Bastoni","Alessandro_Bastoni","国米后防核心左脚将","€4.5M","国际米兰","defender",24,True),
nd(5,"卡拉菲奥里","Calafiori","Riccardo_Calafiori","阿森纳新星后防全能","£100K","阿森纳","defender",20),
nd(6,"迪洛伦佐","Di Lorenzo","Giovanni_Di_Lorenzo","那不勒斯队长右后卫","€3M","那不勒斯","defender",20),
nd(7,"迪马尔科","Dimarco","Federico_Dimarco","国米左路魔术师","€3M","国米","defender",20),
nd(8,"坎比亚索","Cambiaso","Andrea_Cambiaso","尤文边路全能","€2.5M","尤文图斯","defender",18),
nd(9,"布翁乔尔诺","Buongiorno","Alessandro_Buongiorno","那不勒斯后防领袖","€2M","那不勒斯","defender",17),
nd(10,"加蒂","Gatti","Federico_Gatti","尤文后防硬汉","€2M","尤文图斯","defender",17),
nd(11,"巴雷拉","Barella","Nicolo_Barella","国米中场引擎","€5M","国米","midfielder",26,True),
nd(12,"托纳利","Tonali","Sandro_Tonali","纽卡亿元先生禁赛归来","£180K","纽卡斯尔","midfielder",22),
nd(13,"弗拉泰西","Frattesi","Davide_Frattesi","国米中场新星","€3M","国米","midfielder",20),
nd(14,"佩莱格里尼","Pellegrini","Lorenzo_Pellegrini","罗马队长","€4M","罗马","midfielder",20),
nd(15,"若日尼奥","Jorginho","Jorginho_(footballer,_born_December_1991)","阿森纳老将经验丰富","£150K","阿森纳","midfielder",18),
nd(16,"基耶萨","Chiesa","Federico_Chiesa","利物浦失意欧洲杯英雄","£150K","利物浦","forward",22),
nd(17,"雷特吉","Retegui","Mateo_Retegui","归化中锋9号新选择","€2.5M","亚特兰大","forward",20),
nd(18,"拉斯帕多里","Raspadori","Giacomo_Raspadori","那不勒斯锋线尖刀","€2.5M","那不勒斯","forward",19),
nd(19,"扎卡尼","Zaccagni","Mattia_Zaccagni","拉齐奥队长边锋","€2.5M","拉齐奥","forward",18),
nd(20,"斯卡马卡","Scamacca","Gianluca_Scamacca","亚特兰大中锋","€3M","亚特兰大","forward",18),
nd(21,"基恩","Kean","Moise_Kean","佛罗伦萨重生","€2.5M","佛罗伦萨","forward",17),
nd(22,"乌多吉","Udogie","Destiny_Udogie","热刺左路天才","£80K","热刺","defender",17),
nd(23,"洛卡特利","Locatelli","Manuel_Locatelli","尤文中场","€3.5M","尤文图斯","midfielder",18),
nd(24,"斯帕莱蒂","Spalletti","Luciano_Spalletti","意甲冠军教头","€3M","意大利国家队","coach",22,True)]
IT_E=[R(16,24,"弃用风波",3.5,"基耶萨被斯帕莱蒂边缘化","<b>【欧洲杯英雄的坠落】</b><br><br>基耶萨状态低迷后失去主力。<br><br><b>📰 《米兰体育报》</b>"),
R(11,12,"双核共存",2.5,"巴雷拉与托纳利中场共存问题"),
G(11,13,"国米双星",3,"巴雷拉+弗拉泰西双重搭档"),
G(4,7,"国米防线",2.5,"巴斯托尼+迪马尔科左路黄金通道"),
G(17,18,"锋线搭档",2,"雷特吉+拉斯帕多里新生代锋线"),
Gd(24,11,"战术核心",2.5,"斯帕莱蒂以巴雷拉为引擎"),
W(5,4,"中卫","卡拉菲奥里+巴斯托尼"),W(19,16,"边锋","扎卡尼+基耶萨")]
S("italy","意大利",IT_P,IT_E)

# ===== 美国 23人 =====
US_P=[nd(1,"特纳","Turner","Matt_Turner_(soccer)","诺丁汉森林美国一门","£50K","诺丁汉森林","goalkeeper",20),
nd(2,"霍瓦斯","Horvath","Ethan_Horvath","加的夫城二门","€0.8M","加的夫城","goalkeeper",14),
nd(3,"斯特芬","Steffen","Zack_Steffen","科罗拉多急流","€1.5M","科罗拉多急流","goalkeeper",13),
nd(4,"罗宾逊","Robinson","Antonee_Robinson","富勒姆左路超跑","£80K","富勒姆","defender",22),
nd(5,"里姆","Ream","Tim_Ream","夏洛特FC老将","€1M","夏洛特FC","defender",17),
nd(6,"理查兹","Richards","Chris_Richards_(soccer)","水晶宫中卫","£60K","水晶宫","defender",18),
nd(7,"德斯特","Dest","Sergino_Dest","埃因霍温美国飞翼","€2.5M","埃因霍温","defender",20),
nd(8,"斯卡利","Scally","Joe_Scally","门兴右后卫","€1.5M","门兴","defender",16),
nd(9,"麦肯齐","McKenzie","Mark_McKenzie_(soccer,_born_1999)","图卢兹中卫","€1M","图卢兹","defender",14),
nd(10,"普利西奇","Pulisic","Christian_Pulisic","米兰队长美国队长","€5M","AC米兰","forward",28,True),
nd(11,"麦肯尼","McKennie","Weston_McKennie","尤文中场悍将","€3.5M","尤文","midfielder",22),
nd(12,"雷纳","Reyna","Giovanni_Reyna","失意天才禁赛归来","£80K","诺丁汉森林","midfielder",20),
nd(13,"穆萨","Musah","Yunus_Musah","米兰中场新星","€2M","AC米兰","midfielder",18),
nd(14,"卡多索","Cardoso","Johnny_Cardoso","贝蒂斯后腰","€1.5M","皇家贝蒂斯","midfielder",16),
nd(15,"亚当斯","Adams","Tyler_Adams","伯恩茅斯铁腰","£70K","伯恩茅斯","midfielder",19),
nd(16,"巴洛贡","Balogun","Folarin_Balogun","摩纳哥中锋","€3M","摩纳哥","forward",20),
nd(17,"佩皮","Pepi","Ricardo_Pepi","埃因霍温射手","€2M","埃因霍温","forward",18),
nd(18,"维阿","Weah","Timothy_Weah","传奇之子尤文","€2.5M","尤文","forward",17),
nd(19,"阿伦森","Aaronson","Brenden_Aaronson","利兹联攻击手","€2M","利兹联","midfielder",16),
nd(20,"萨金特","Sargent","Josh_Sargent","诺维奇中锋","€1.5M","诺维奇","forward",15),
nd(21,"赖特","Wright","Haji_Wright_(soccer)","考文垂黑又硬","€1.5M","考文垂","forward",16),
nd(22,"蒂尔曼","Tillman","Malik_Tillman","埃因霍温妖星","€1.8M","埃因霍温","midfielder",16),
nd(23,"波切蒂诺","Pochettino","Mauricio_Pochettino","美国新帅热刺切尔西前帅","€6M","美国国家队","coach",24,True)]
US_E=[R(12,23,"雷纳门",4,"雷纳被弃用父母揭主帅家暴丑闻","<b>【家庭伦理剧：雷纳门事件】</b><br><br>2022世界杯雷纳被弃用其父母向足协举报主帅30年前家暴丑闻。足球史上最轰动的家庭伦理剧！<br><br><b>📰 ESPN独家调查</b>"),
G(10,13,"米兰双星",3,"普利西奇+穆萨米兰美国帮"),
G(11,18,"尤文双星",2.5,"麦肯尼+维阿尤文连线"),
G(4,6,"英超防线",2,"罗宾逊+理查兹"),
Gd(23,10,"队长信任",3,"波切蒂诺以普利西奇为绝对核心"),
W(15,14,"后腰","亚当斯+卡多索"),W(16,17,"中锋","巴洛贡+佩皮")]
S("usa","美国",US_P,US_E)

# ===== 韩国 22人 =====
KR_P=[nd(1,"金承奎","Kim Seung-gyu","Kim_Seung-gyu","沙特老门将","€1.5M","利雅得青年","goalkeeper",18),
nd(2,"赵贤祐","Jo Hyeon-woo","Jo_Hyeon-woo","蔚山现代门神","€0.8M","蔚山现代","goalkeeper",17),
nd(3,"宋范根","Song Bum-keun","Song_Bum-keun","湘南比马","€0.5M","湘南比马","goalkeeper",13),
nd(4,"金玟哉","Kim Min-jae","Kim_Min-jae","拜仁铁塔亚洲第一中卫","£200K","拜仁","defender",28,True),
nd(5,"金英权","Kim Young-gwon","Kim_Young-gwon","蔚山老将","€1M","蔚山现代","defender",20),
nd(6,"权敬原","Kwon Kyung-won","Kwon_Kyung-won","水原FC","€0.8M","水原FC","defender",15),
nd(7,"薛英佑","Seol Young-woo","Seol_Young-woo","蔚山右后卫","€0.5M","蔚山现代","defender",14),
nd(8,"金珍洙","Kim Jin-su","Kim_Jin-su","全北左后卫","€0.5M","全北现代","defender",14),
nd(9,"李记帝","Lee Ki-je","Lee_Ki-je","水原左后卫","€0.5M","水原三星","defender",13),
nd(10,"孙兴慜","Son Heung-min","Son_Heung-min","亚洲之光热刺传奇","£200K","热刺","forward",30,True),
nd(11,"李刚仁","Lee Kang-in","Lee_Kang-in","巴黎天才乒乓球门主角","€4M","巴黎","forward",24,True),
nd(12,"黄喜灿","Hwang Hee-chan","Hwang_Hee-chan","狼队韩国前锋","£80K","狼队","forward",22),
nd(13,"李在城","Lee Jae-sung","Lee_Jae-sung","美因茨中场","€1.5M","美因茨","midfielder",18),
nd(14,"黄仁范","Hwang In-beom","Hwang_In-beom","贝尔格莱德红星","€1.5M","红星","midfielder",18),
nd(15,"郑优营","Jeong Woo-yeong","Jeong_Woo-yeong","斯图加特边锋","€1M","斯图加特","forward",16),
nd(16,"吴贤揆","Oh Hyeon-gyu","Oh_Hyeon-gyu","凯尔特人中锋","€0.8M","凯尔特人","forward",15),
nd(17,"曹圭成","Cho Gue-sung","Cho_Gue-sung","中日德兰中锋","€1M","中日德兰","forward",16),
nd(18,"洪铉锡","Hong Hyun-seok","Hong_Hyun-seok","根特中场","€0.8M","根特","midfielder",14),
nd(19,"裴峻浩","Bae Jun-ho","Bae_Jun-ho","斯托克城新星","€0.5M","斯托克城","forward",14),
nd(20,"白昇浩","Paik Seung-ho","Paik_Seung-ho","伯明翰中场","€0.5M","伯明翰","midfielder",14),
nd(21,"朴镕宇","Park Yong-woo","Park_Yong-woo","艾因后腰","€1M","艾因","midfielder",14),
nd(22,"洪明甫","Hong Myung-bo","Hong_Myung-bo","韩国足球传奇","€1.5M","韩国国家队","coach",20,True)]
KR_E=[R(10,11,"乒乓球门",4.5,"孙兴慜与李刚仁冲突手指脱臼","<b>【亚洲杯乒乓球门】</b><br><br>2024亚洲杯前夕李刚仁等打乒乓球队长制止引发肢体冲突孙兴慜手指脱臼！长幼尊卑文化碰撞。<br><br><b>📰 《朝鲜日报》独家</b>"),
R(11,22,"纪律问题",2.5,"李刚仁纪律性屡遭教练组质疑"),
G(10,12,"英超双星",3,"孙兴慜+黄喜灿英超连线"),
G(11,13,"技术流中场",2,"李刚仁+李在城"),
G(4,5,"中卫搭档",2,"金玟哉+金英权拜仁蔚山"),
Gd(22,10,"绝对核心",3,"洪明甫以孙兴慜为队魂"),
W(7,8,"边后卫","薛英佑+金珍洙"),W(17,16,"中锋","曹圭成+吴贤揆")]
S("southkorea","韩国",KR_P,KR_E)

print("\n=== 第二梯队扩充完成 ===")
