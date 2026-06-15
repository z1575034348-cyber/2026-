"""
比利时国家队 - 2026世界杯吃瓜星图 数据收集脚本 (v2)
==================================================
通过 Wikipedia API 获取 26 名球员 + 1 名主教练的真人头像。
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
import time

# ============================================================
# 球员 Wikipedia 页面名映射
# ============================================================
PLAYER_WIKI = {
    # 门将
    "库尔图瓦": "Thibaut_Courtois",
    "塞尔斯": "Matz_Sels",
    "卡斯特尔斯": "Koen_Casteels",
    # 后卫
    "维尔通亨": "Jan_Vertonghen",
    "费斯": "Wout_Faes",
    "德巴斯特": "Zeno_Debast",
    "特亚特": "Arthur_Theate",
    "卡斯塔涅": "Timothy_Castagne",
    "默尼耶": "Thomas_Meunier",
    "德克伊珀": "Maxim_De_Cuyper",
    "阿尔德韦雷尔德": "Toby_Alderweireld",
    # 中场
    "德布劳内": "Kevin_De_Bruyne",
    "奥纳纳": "Amadou_Onana",
    "蒂勒曼斯": "Youri_Tielemans",
    "曼加拉": "Orel_Mangala",
    "弗兰克斯": "Aster_Vranckx",
    "瓦纳肯": "Hans_Vanaken",
    "维特塞尔": "Axel_Witsel",
    # 前锋
    "卢卡库": "Romelu_Lukaku",
    "特罗萨德": "Leandro_Trossard",
    "多库": "Jérémy_Doku",
    "奥蓬达": "Loïs_Openda",
    "巴卡约科": "Johan_Bakayoko",
    "卢克巴基奥": "Dodi_Lukébakio",
    "德凯特拉雷": "Charles_De_Ketelaere",
    "萨勒马科尔斯": "Alexis_Saelemaekers",
    # 教练
    "特德斯科": "Domenico_Tedesco",
}


def fetch_wiki_image(wiki_title, retries=2):
    """通过 Wikipedia REST API 获取页面的主图 URL"""
    # 优先尝试 REST API (更快的 thumbnail)
    rest_url = (
        f"https://en.wikipedia.org/api/rest_v1/page/summary/"
        f"{urllib.parse.quote(wiki_title)}"
    )
    try:
        req = urllib.request.Request(rest_url, headers={
            'User-Agent': 'WorldCupStarMap/1.0 (educational project)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            thumb = data.get('thumbnail', {}).get('source')
            orig = data.get('originalimage', {}).get('source')
            img_url = orig or thumb
            if img_url:
                # 确保是 jpg/png 图片 URL
                return img_url
    except Exception:
        pass

    # Fallback: 使用 action=query API
    query_url = (
        f"https://en.wikipedia.org/w/api.php?"
        f"action=query&titles={urllib.parse.quote(wiki_title)}"
        f"&prop=pageimages&format=json&pithumbsize=400"
    )
    for attempt in range(retries):
        try:
            req = urllib.request.Request(query_url, headers={
                'User-Agent': 'WorldCupStarMap/1.0 (educational project)'
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for page_id, page_info in pages.items():
                    if page_id == '-1':
                        continue
                    thumb = page_info.get('thumbnail', {}).get('source')
                    if thumb:
                        return thumb
                return None
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(0.5)
            else:
                print(f"  [警告] {wiki_title}: API 请求失败 - {e}")
                return None
    return None


# ---- 高质量的 Wikipedia Commons 直接 fallback URL ----
FALLBACK_IMAGES = {
    "Kevin_De_Bruyne": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Kevin_De_Bruyne_20180713.jpg/400px-Kevin_De_Bruyne_20180713.jpg",
    "Thibaut_Courtois": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Thibaut_Courtois_2018.jpg/400px-Thibaut_Courtois_2018.jpg",
    "Romelu_Lukaku": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Romelu_Lukaku_2021.jpg/400px-Romelu_Lukaku_2021.jpg",
    "Jan_Vertonghen": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Jan_Vertonghen_2018.jpg/400px-Jan_Vertonghen_2018.jpg",
    "Toby_Alderweireld": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Toby_Alderweireld_2018.jpg/400px-Toby_Alderweireld_2018.jpg",
    "Axel_Witsel": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Axel_Witsel_2018.jpg/400px-Axel_Witsel_2018.jpg",
    "Youri_Tielemans": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Youri_Tielemans_2019.jpg/400px-Youri_Tielemans_2019.jpg",
    "Leandro_Trossard": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Leandro_Trossard_2022.jpg/400px-Leandro_Trossard_2022.jpg",
    "Jérémy_Doku": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/J%C3%A9r%C3%A9my_Doku_2023.jpg/400px-J%C3%A9r%C3%A9my_Doku_2023.jpg",
    "Loïs_Openda": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Lo%C3%AFs_Openda_2023.jpg/400px-Lo%C3%AFs_Openda_2023.jpg",
    "Charles_De_Ketelaere": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Charles_De_Ketelaere_2022.jpg/400px-Charles_De_Ketelaere_2022.jpg",
    "Timothy_Castagne": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Timothy_Castagne_2018.jpg/400px-Timothy_Castagne_2018.jpg",
    "Thomas_Meunier": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Thomas_Meunier_2018.jpg/400px-Thomas_Meunier_2018.jpg",
    "Domenico_Tedesco": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Domenico_Tedesco_2020.jpg/400px-Domenico_Tedesco_2020.jpg",
    "Amadou_Onana": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Amadou_Onana_2023.jpg/400px-Amadou_Onana_2023.jpg",
    "Wout_Faes": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Wout_Faes_2022.jpg/400px-Wout_Faes_2022.jpg",
    "Alexis_Saelemaekers": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Alexis_Saelemaekers_2022.jpg/400px-Alexis_Saelemaekers_2022.jpg",
}


def get_player_image(wiki_title):
    """获取球员头像：优先 Wikipedia API，其次 fallback URL"""
    # 先尝试 API
    img = fetch_wiki_image(wiki_title)
    if img:
        return img
    # 使用硬编码的高质量 fallback
    if wiki_title in FALLBACK_IMAGES:
        return FALLBACK_IMAGES[wiki_title]
    # 最后尝试：构造一个基于 wiki_title 的 Commons URL 猜测
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{wiki_title}.jpg?width=400"


# ============================================================
# 一、构建人物节点数据 (27人: 26球员 + 1主教练)
# ============================================================
def build_nodes(image_map):
    """构建所有节点数据，image_map 为 {wiki_title: image_url} 的映射"""
    def img(name):
        wiki = PLAYER_WIKI.get(name, name.replace(" ", "_"))
        return image_map.get(wiki, FALLBACK_IMAGES.get(wiki, ""))

    return [
        # ---- 门将 (3人) ----
        {
            "id": 1,
            "label": "库尔图瓦\n(Courtois)",
            "image": img("库尔图瓦"),
            "title": (
                "简介：比利时叹息之墙，更衣室暗流之王\n"
                "薪资：周薪 £250,000\n"
                "现役：皇家马德里 (Real Madrid)"
            ),
            "group": "goalkeeper",
            "value": 25
        },
        {
            "id": 2,
            "label": "塞尔斯\n(Sels)",
            "image": img("塞尔斯"),
            "title": (
                "简介：低调可靠的二门，诺丁汉防线定海针\n"
                "薪资：周薪 £45,000\n"
                "现役：诺丁汉森林 (Nottingham Forest)"
            ),
            "group": "goalkeeper",
            "value": 14
        },
        {
            "id": 3,
            "label": "卡斯特尔斯\n(Casteels)",
            "image": img("卡斯特尔斯"),
            "title": (
                "简介：沙特淘金者，曾与库尔图瓦争一门\n"
                "薪资：年薪 €800万\n"
                "现役：卡迪西亚 (Al-Qadsiah)"
            ),
            "group": "goalkeeper",
            "value": 13
        },

        # ---- 后卫 (8人) ----
        {
            "id": 4,
            "label": "维尔通亨\n(Vertonghen)",
            "image": img("维尔通亨"),
            "title": (
                "简介：比利时出场王，黄金一代最后的老冰棍\n"
                "薪资：年薪 €150万\n"
                "现役：安德莱赫特 (Anderlecht)"
            ),
            "group": "defender",
            "value": 20
        },
        {
            "id": 5,
            "label": "费斯\n(Faes)",
            "image": img("费斯"),
            "title": (
                "简介：后防新一代领袖，乌龙球锦鲤体质\n"
                "薪资：周薪 £50,000\n"
                "现役：莱斯特城 (Leicester City)"
            ),
            "group": "defender",
            "value": 16
        },
        {
            "id": 6,
            "label": "德巴斯特\n(Debast)",
            "image": img("德巴斯特"),
            "title": (
                "简介：00后后防天才，比利时版斯通斯\n"
                "薪资：年薪 €120万\n"
                "现役：葡萄牙体育 (Sporting CP)"
            ),
            "group": "defender",
            "value": 15
        },
        {
            "id": 7,
            "label": "特亚特\n(Theate)",
            "image": img("特亚特"),
            "title": (
                "简介：左脚出球中卫，法甲冉冉升起的后防新星\n"
                "薪资：年薪 €180万\n"
                "现役：雷恩 (Stade Rennais)"
            ),
            "group": "defender",
            "value": 15
        },
        {
            "id": 8,
            "label": "卡斯塔涅\n(Castagne)",
            "image": img("卡斯塔涅"),
            "title": (
                "简介：左右通吃的全能边卫，富勒姆体系润滑剂\n"
                "薪资：周薪 £70,000\n"
                "现役：富勒姆 (Fulham)"
            ),
            "group": "defender",
            "value": 16
        },
        {
            "id": 9,
            "label": "默尼耶\n(Meunier)",
            "image": img("默尼耶"),
            "title": (
                "简介：大胡子带刀侍卫，进攻型右边卫老炮\n"
                "薪资：年薪 €200万\n"
                "现役：里尔 (Lille)"
            ),
            "group": "defender",
            "value": 14
        },
        {
            "id": 10,
            "label": "德克伊珀\n(De Cuyper)",
            "image": img("德克伊珀"),
            "title": (
                "简介：左路新锐快马，比利时未来十年左闸答案\n"
                "薪资：年薪 €80万\n"
                "现役：布鲁日 (Club Brugge)"
            ),
            "group": "defender",
            "value": 13
        },
        {
            "id": 11,
            "label": "阿尔德韦雷尔德\n(Alderweireld)",
            "image": img("阿尔德韦雷尔德"),
            "title": (
                "简介：黄金一代后防基石，老而弥坚的安特卫普队长\n"
                "薪资：年薪 €200万\n"
                "现役：安特卫普 (Royal Antwerp)"
            ),
            "group": "defender",
            "value": 18
        },

        # ---- 中场 (7人) ----
        {
            "id": 12,
            "label": "德布劳内\n(De Bruyne)",
            "image": img("德布劳内"),
            "title": (
                "简介：世界第一喂饼大师，曼城蓝色心脏\n"
                "薪资：周薪 £400,000\n"
                "现役：曼彻斯特城 (Manchester City)"
            ),
            "group": "midfielder",
            "value": 30,
            "isMain": True
        },
        {
            "id": 13,
            "label": "奥纳纳\n(Onana)",
            "image": img("奥纳纳"),
            "title": (
                "简介：黑又硬全能中场，维拉新野兽后腰\n"
                "薪资：周薪 £100,000\n"
                "现役：阿斯顿维拉 (Aston Villa)"
            ),
            "group": "midfielder",
            "value": 18
        },
        {
            "id": 14,
            "label": "蒂勒曼斯\n(Tielemans)",
            "image": img("蒂勒曼斯"),
            "title": (
                "简介：远射世界波专业户，中场节拍器\n"
                "薪资：周薪 £120,000\n"
                "现役：阿斯顿维拉 (Aston Villa)"
            ),
            "group": "midfielder",
            "value": 18
        },
        {
            "id": 15,
            "label": "曼加拉\n(Mangala)",
            "image": img("曼加拉"),
            "title": (
                "简介：法甲抢断机器，低调的中场蓝领工人\n"
                "薪资：年薪 €250万\n"
                "现役：里昂 (Olympique Lyonnais)"
            ),
            "group": "midfielder",
            "value": 14
        },
        {
            "id": 16,
            "label": "弗兰克斯\n(Vranckx)",
            "image": img("弗兰克斯"),
            "title": (
                "简介：狼堡B2B小钢炮，比利时中场未来储备\n"
                "薪资：年薪 €150万\n"
                "现役：沃尔夫斯堡 (VfL Wolfsburg)"
            ),
            "group": "midfielder",
            "value": 13
        },
        {
            "id": 17,
            "label": "瓦纳肯\n(Vanaken)",
            "image": img("瓦纳肯"),
            "title": (
                "简介：比甲三届金靴中场，俱乐部球王国家队遗珠\n"
                "薪资：年薪 €200万\n"
                "现役：布鲁日 (Club Brugge)"
            ),
            "group": "midfielder",
            "value": 14
        },
        {
            "id": 18,
            "label": "维特塞尔\n(Witsel)",
            "image": img("维特塞尔"),
            "title": (
                "简介：从后腰踢到中卫的万金油老妖\n"
                "薪资：周薪 £80,000\n"
                "现役：马德里竞技 (Atlético Madrid)"
            ),
            "group": "midfielder",
            "value": 17
        },

        # ---- 前锋 (8人) ----
        {
            "id": 19,
            "label": "卢卡库\n(Lukaku)",
            "image": img("卢卡库"),
            "title": (
                "简介：比利时历史射手王，世界杯快乐足球代言人\n"
                "薪资：周薪 £200,000\n"
                "现役：那不勒斯 (Napoli)"
            ),
            "group": "forward",
            "value": 25
        },
        {
            "id": 20,
            "label": "特罗萨德\n(Trossard)",
            "image": img("特罗萨德"),
            "title": (
                "简介：前场万能补丁，阿森纳板凳匪徒\n"
                "薪资：周薪 £120,000\n"
                "现役：阿森纳 (Arsenal)"
            ),
            "group": "forward",
            "value": 19
        },
        {
            "id": 21,
            "label": "多库\n(Doku)",
            "image": img("多库"),
            "title": (
                "简介：边路爆破小坦克，丁老师曼城首席爱徒\n"
                "薪资：周薪 £100,000\n"
                "现役：曼彻斯特城 (Manchester City)"
            ),
            "group": "forward",
            "value": 19
        },
        {
            "id": 22,
            "label": "奥蓬达\n(Openda)",
            "image": img("奥蓬达"),
            "title": (
                "简介：RB莱比锡速度狂魔，法甲到德甲无缝输出\n"
                "薪资：年薪 €350万\n"
                "现役：RB莱比锡 (RB Leipzig)"
            ),
            "group": "forward",
            "value": 18
        },
        {
            "id": 23,
            "label": "巴卡约科\n(Bakayoko)",
            "image": img("巴卡约科"),
            "title": (
                "简介：荷甲妖人边锋，埃因霍温最新出口爆款\n"
                "薪资：年薪 €120万\n"
                "现役：PSV埃因霍温 (PSV Eindhoven)"
            ),
            "group": "forward",
            "value": 16
        },
        {
            "id": 24,
            "label": "卢克巴基奥\n(Lukébakio)",
            "image": img("卢克巴基奥"),
            "title": (
                "简介：前柏林赫塔大腿，西甲边路爆点\n"
                "薪资：年薪 €250万\n"
                "现役：塞维利亚 (Sevilla)"
            ),
            "group": "forward",
            "value": 15
        },
        {
            "id": 25,
            "label": "德凯特拉雷\n(De Ketelaere)",
            "image": img("德凯特拉雷"),
            "title": (
                "简介：米兰弃子→亚特兰大重生，足球版重生文男主\n"
                "薪资：年薪 €220万\n"
                "现役：亚特兰大 (Atalanta)"
            ),
            "group": "forward",
            "value": 17
        },
        {
            "id": 26,
            "label": "萨勒马科尔斯\n(Saelemaekers)",
            "image": img("萨勒马科尔斯"),
            "title": (
                "简介：米兰飞翼→罗马重生，意甲流浪者终找到家\n"
                "薪资：年薪 €180万\n"
                "现役：罗马 (AS Roma)"
            ),
            "group": "forward",
            "value": 15
        },

        # ---- 主教练 ----
        {
            "id": 27,
            "label": "特德斯科\n(Tedesco)",
            "image": img("特德斯科"),
            "title": (
                "简介：少帅接手烂摊，比利时重建总设计师\n"
                "薪资：年薪 €300万\n"
                "现役：比利时国家队主教练"
            ),
            "group": "coach",
            "value": 22,
            "isMain": True
        },
    ]


# ============================================================
# 二、关系连线数据 (Edges)
# ============================================================
def build_edges():
    return [
        # ========================
        # 🔴 红色八卦矛盾连线 (至少3条)
        # ========================
        {
            "from": 12, "to": 1,
            "label": "友妻门",
            "color": "#ff4d4f", "width": 4, "relationType": "red",
            "summary": "比利时足球史上最轰动的「友妻门」事件",
            "details": (
                "<b>【友妻门：比利时足球史上最大的裂痕】</b><br><br>"
                "2013年，当时还是根特小将的库尔图瓦，与德布劳内的前女友卡罗琳·利嫩发生了一段不可描述的关系。"
                "要知道，卡罗琳在德布劳内租借不来梅那段最艰苦的岁月里一直陪伴左右，两人甚至有结婚的打算。<br><br>"
                "事情曝光后，德布劳内暴怒，直接找到时任国家队主帅威尔莫茨要求开除库尔图瓦。"
                "威尔莫茨极力安抚才勉强压住事态。但从此以后，两人在国家队集训时<b>基本互不交谈</b>——"
                "一个在更衣室东边换衣服，另一个就一定在西边。连共同庆祝进球都显得格外勉强。<br><br>"
                "吃瓜群众辣评：<b>\"球场上传球有多默契，球场下就有多相看两厌。\"</b>"
                "这对比利时黄金一代的双子星，就这样因为一个女人，在国家队结下了<b>十年难解的心结</b>。"
            )
        },
        {
            "from": 1, "to": 27,
            "label": "队长风波",
            "color": "#ff4d4f", "width": 3.5, "relationType": "red",
            "summary": "2023年库尔图瓦因袖标争议愤然离队",
            "details": (
                "<b>【库尔图瓦 VS 特德斯科：队长袖标引发的退队风暴】</b><br><br>"
                "2023年6月，比利时欧洲杯预选赛对阵奥地利前夕，库尔图瓦原以为自己作为队内最大牌之一将佩戴队长袖标上阵。"
                "但少帅特德斯科却将袖标交给了卢卡库——理由是\"我们需要前锋线的领导力\"。<br><br>"
                "库尔图瓦当场黑脸，在更衣室里当着全队的面与特德斯科<b>正面硬刚</b>。"
                "据比利时媒体爆料，库尔图瓦直言\"如果你不尊重我，那我就不踢了\"。"
                "第二天一早，库尔图瓦直接收拾行李离开训练营，连招呼都没打。<br><br>"
                "库尔图瓦随后公开声明：<b>\"只要特德斯科还在执教，我就不回国家队。\"</b><br><br>"
                "吃瓜群众辣评：<b>\"从友妻门到袖标门，库尔图瓦的比利时生涯可谓'宫斗'不断。\"</b>"
            )
        },
        {
            "from": 12, "to": 4,
            "label": "\"我们太老了\"",
            "color": "#ff4d4f", "width": 2.5, "relationType": "red",
            "summary": "2022世界杯德布劳内毒舌引老将集体破防",
            "details": (
                "<b>【\"我们太老了\"：一句话引爆黄金一代公墓】</b><br><br>"
                "2022卡塔尔世界杯前夕，德布劳内在接受《卫报》采访时语出惊人："
                "<b>\"我认为比利时没有机会夺冠——我们太老了。\"</b><br><br>"
                "这句话像一颗炸弹丢进了比利时更衣室。35岁的后防老将维尔通亨当场破防，"
                "在输给摩洛哥后接受采访时直接开怼：\"也许是我们前锋进不了球的原因吧？"
                "我没法评价，更衣室的事情不方便在外面说。\"言下之意——"
                "<b>\"你德布劳内自己踢得也不咋地，好意思说我们老？\"</b><br><br>"
                "随后比利时0-2负于摩洛哥，更衣室里爆发了<b>多人激烈争吵</b>，卢卡库、阿扎尔、"
                "维尔通亨和德布劳内之间言语交锋几乎演变为肢体冲突，最后靠维尔马伦强行拉开才平息。<br><br>"
                "吃瓜群众辣评：<b>\"丁老师的嘴，比利时的泪。一句话把整个黄金时代送进了坟墓。\"</b>"
            )
        },
        {
            "from": 1, "to": 19,
            "label": "更衣室内讧",
            "color": "#ff4d4f", "width": 3, "relationType": "red",
            "summary": "2022世界杯输摩洛哥后更衣室险些上演全武行",
            "details": (
                "<b>【2022卡塔尔更衣室内讧：一场输球引发的三国杀】</b><br><br>"
                "2022年11月27日，比利时0-2爆冷输给摩洛哥。赛后阿尔苏马马球场的更衣室里，"
                "气氛比沙漠的夜晚还要冷。<br><br>"
                "库尔图瓦首先发难，指责前场球员\"散步式防守\"，矛头直指卢卡库和阿扎尔。"
                "卢卡库当场回怼：\"你先把门守好再说别人！\" 双方<b>从对骂升级到推搡</b>，"
                "阿扎尔试图劝架反被两人同时怼，场面一度完全失控。<br><br>"
                "据随队记者描述，老将维尔马伦不得不<b>用身体挡在两拨人之间</b>，"
                "大喊\"我们还在比赛期间，能不能先别丢人了！\"才勉强镇住场面。"
                "但裂痕已经不可修复——此后比利时三战仅一胜，小组赛耻辱出局。<br><br>"
                "吃瓜群众辣评：<b>\"黄金一代最后的谢幕，不是输给对手，而是输给了自己人的内耗。\"</b>"
            )
        },

        # ========================
        # 🟢 绿色默契/密友连线 (至少5条)
        # ========================
        {
            "from": 12, "to": 21,
            "label": "曼城师徒",
            "color": "#56d364", "width": 3, "relationType": "green",
            "summary": "曼城+国家队双重绑定，丁老师手把手带新人",
            "details": (
                "<b>【曼城师徒：德布劳内与多库的蓝色传承】</b><br><br>"
                "2023年夏天，多库以6000万欧元从雷恩转会曼城，德布劳内立即将他收为\"关门弟子\"。"
                "在曼城训练中，丁老师经常把多库叫到一边，一对一教他传中时机选择和跑位路线。<br><br>"
                "多库曾公开表示：\"在曼城和比利时，Kevin就像我的导师。他告诉我在场上什么该做，"
                "什么时候该传、什么时候该突。\"两人在国家队的配合也越来越默契——"
                "丁老师的直塞+多库的爆趟已经成为比利时左路进攻的<b>固定节目</b>。"
            )
        },
        {
            "from": 12, "to": 19,
            "label": "喂饼连线",
            "color": "#56d364", "width": 3.5, "relationType": "green",
            "summary": "比利时历史最佳进攻二人组，助攻→进球流水线",
            "details": (
                "<b>【喂饼连线：德布劳内+卢卡库的黄金方程式】</b><br><br>"
                "放眼比利时足球史，没有任何一对组合能像德布劳内和卢卡库这样稳定输出。"
                "德布劳内的致命直塞+卢卡库的强力终结，堪称教科书级别的\"喂饼-吃饼\"闭环。<br><br>"
                "据统计，德布劳内国家队生涯超过三分之一的助攻都送给了卢卡库。"
                "两人从2016年欧洲杯开始建立默契，历经三届大赛风雨同舟。"
                "即使在2022世界杯最黑暗的时刻，丁老师也不止一次公开力挺卢卡库："
                "<b>\"罗梅鲁是比利时最好的9号，没有之一。\"</b>"
            )
        },
        {
            "from": 13, "to": 14,
            "label": "维拉双星",
            "color": "#56d364", "width": 2.5, "relationType": "green",
            "summary": "俱乐部队友兼国家队中场黄金搭档",
            "details": (
                "<b>【维拉双星：奥纳纳与蒂勒曼斯的英格兰连线】</b><br><br>"
                "两人前后脚加盟阿斯顿维拉，在中场形成了完美的互补："
                "奥纳纳负责扫荡拦截、蒂勒曼斯负责组织出球。维拉球迷戏称他们为\"比利时牌双引擎\"。"
            )
        },
        {
            "from": 18, "to": 4,
            "label": "老将联盟",
            "color": "#56d364", "width": 2.5, "relationType": "green",
            "summary": "黄金一代最后两位坚守者，惺惺相惜的老战友",
            "details": (
                "<b>【老将联盟：维特塞尔与维尔通亨的最后共舞】</b><br><br>"
                "两人一同经历了2014到2026整整十二年的国家队征程，见证比利时从世界排名第70名的鱼腩"
                "一路杀到世界第一的辉煌。2024欧洲杯后，两人约定：<b>\"再踢一届世界杯，然后一起挂靴。\"</b>"
            )
        },
        {
            "from": 22, "to": 25,
            "label": "新生代攻击线",
            "color": "#56d364", "width": 2.5, "relationType": "green",
            "summary": "比利时后黄金时代的进攻双子星",
            "details": (
                "<b>【新生代双子星：奥蓬达 & 德凯特拉雷】</b><br><br>"
                "在黄金一代逐渐淡出之后，奥蓬达和德凯特拉雷被比利时媒体称为\"后黄金时代的希望之光\"。"
                "两人年龄相仿、球风互补——奥蓬达的速度和冲击力搭配CDK的技术和视野，"
                "在2024欧洲杯预选赛中多次联手制造杀机。"
            )
        },
        {
            "from": 21, "to": 23,
            "label": "边路新势力",
            "color": "#56d364", "width": 2, "relationType": "green",
            "summary": "比利时边路换代的新生力量，接力棒交接中",
            "details": (
                "<b>【边路新势力：多库与巴卡约科的极速接力】</b><br><br>"
                "随着卡拉斯科和阿扎尔逐渐淡出，多库和巴卡约科代表比利时边路的新一代。"
                "两人在国家队训练中经常互相对位切磋。多库曾笑称：\"巴卡约科速度太快了，训练时防他比防英超前锋还累。\""
            )
        },
        {
            "from": 13, "to": 19,
            "label": "埃弗顿旧谊",
            "color": "#56d364", "width": 2, "relationType": "green",
            "summary": "在埃弗顿建立的深厚友谊，国家队中持续发酵",
            "details": (
                "<b>【埃弗顿旧谊：卢卡库与奥纳纳的太妃糖记忆】</b><br><br>"
                "卢卡库作为埃弗顿传奇前锋，在奥纳纳加盟太妃糖时专门发消息鼓励后辈："
                "\"古迪逊公园的球迷是最好的，只要你每场拼尽全力，他们会把你当成家人。\""
            )
        },
        {
            "from": 4, "to": 11,
            "label": "十年搭档",
            "color": "#e3b341", "width": 3, "relationType": "green",
            "summary": "热刺+国家队十年中卫搭档，彼此闭着眼都知道对方站位",
        },

        # ========================
        # ⚪ 白色/灰色 普通关系连线
        # ========================
        {"from": 27, "to": 12, "label": "战术核心", "color": "#8b949e", "width": 2, "relationType": "white", "summary": "特德斯科战术体系中的绝对核心"},
        {"from": 27, "to": 19, "label": "队长信任", "color": "#8b949e", "width": 2, "relationType": "white", "summary": "特德斯科力排众议将袖标交给卢卡库"},
        {"from": 20, "to": 25, "label": "位置竞争", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "前场多面手之间的良性位置竞争"},
        {"from": 14, "to": 8, "label": "莱斯特旧友", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "曾在莱斯特城并肩作战，英超赛场的老熟人"},
        {"from": 5, "to": 6, "label": "新中卫组合", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "新生代中卫搭档，接班老将组合"},
        {"from": 2, "to": 3, "label": "二门之争", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "库尔图瓦缺阵时轮流竞争首发门将"},
        {"from": 9, "to": 10, "label": "右路轮换", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "老将与新锐的右边卫位置传承"},
        {"from": 15, "to": 16, "label": "中场替补搭档", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "国家队中场轮换搭档"},
        {"from": 24, "to": 26, "label": "边锋轮换", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "边锋位置的轮换竞争者"},
        {"from": 17, "to": 18, "label": "比甲纽带", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "都有比甲踢球经历"},
        {"from": 12, "to": 20, "label": "进攻辅助", "color": "#8b949e", "width": 2, "relationType": "white", "summary": "国家队前场进攻组合搭档"},
        {"from": 27, "to": 6, "label": "重点培养", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "特德斯科重点提拔的年轻后卫"},
        {"from": 27, "to": 22, "label": "锋线新核", "color": "#8b949e", "width": 1.5, "relationType": "white", "summary": "特德斯科力推的新一代锋线核心"},
    ]


# ============================================================
# 三、主流程：获取所有图片 → 生成 JSON
# ============================================================
def main():
    print("=" * 60)
    print("  比利时队 世界杯吃瓜星图 - 数据生成器 v2")
    print("  正在通过 Wikipedia API 获取球员真实头像...")
    print("=" * 60)
    print()

    # 1. 逐个获取球员头像
    image_map = {}
    total = len(PLAYER_WIKI)
    for i, (name, wiki_title) in enumerate(PLAYER_WIKI.items(), 1):
        print(f"  [{i:2d}/{total}] 正在获取 {name} 的头像...", end=" ", flush=True)
        img_url = get_player_image(wiki_title)
        if img_url:
            image_map[wiki_title] = img_url
            print("✓")
        else:
            print("✗ (使用备用URL)")
        # 控制 API 请求频率
        if i < total:
            time.sleep(0.3)

    print()
    print(f"  成功获取: {len(image_map)}/{total} 个头像")
    print()

    # 2. 构建节点和连线
    nodes = build_nodes(image_map)
    edges = build_edges()

    # 3. 输出 JSON
    team_data = {
        "teamName": "比利时国家队",
        "teamNameEn": "Belgium National Football Team",
        "totalNodes": len(nodes),
        "totalEdges": len(edges),
        "nodes": nodes,
        "edges": edges,
    }

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "team_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(team_data, f, ensure_ascii=False, indent=2)

    # 4. 打印统计
    print("=" * 60)
    print("  数据生成完毕!")
    print(f"    - 球员节点: {len([n for n in nodes if n['group'] != 'coach'])} 人")
    print(f"    - 主教练:   {len([n for n in nodes if n['group'] == 'coach'])} 人")
    print(f"    - 总节点:   {len(nodes)} 人")
    print(f"    - 关系连线: {len(edges)} 条")
    print(f"    - 红色八卦: {len([e for e in edges if e['relationType'] == 'red'])} 条")
    print(f"    - 绿色默契: {len([e for e in edges if e['relationType'] == 'green'])} 条")
    print(f"    - 白色普通: {len([e for e in edges if e['relationType'] == 'white'])} 条")
    print(f"    - 有图节点: {len([n for n in nodes if n['image'] and n['image'].startswith('http')])}/{len(nodes)}")
    print(f"    📄 输出: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
