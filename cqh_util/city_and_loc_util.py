"""
https://blog.csdn.net/cds86333774/article/details/51009057
"""
city_loc_raw = """
    北京经纬度:(116.41667,39.91667)<br>
    上海经纬度:(121.43333,31.20000)<br>
    天津经纬度:(117.20000,39.13333)<br>
    香港经纬度:(114.10000,22.20000)<br>
    广州经纬度:(113.23333,23.16667)<br>
    珠海经纬度:(113.51667,22.30000)<br>
    深圳经纬度:(114.06667,22.61667)<br>
    杭州经纬度:(120.20000,30.26667)<br>
    重庆经纬度:(106.45000, 29.56667)<br>
    青岛经纬度:(120.33333,36.06667)<br>
    厦门经纬度:(118.10000,24.46667)<br>
    福州经纬度:(119.30000,26.08333)<br>
    兰州经纬度:(103.73333,36.03333)<br>
    贵阳经纬度:(106.71667,26.56667)<br>
    长沙经纬度:(113.00000,28.21667)<br>
    南京经纬度:(118.78333,32.05000)<br>
    南昌经纬度:(115.90000,28.68333)<br>
    沈阳经纬度:(123.38333,41.80000)<br>
    太原经纬度:(112.53333,37.86667)<br>
    成都经纬度:(104.06667,30.66667)<br>
    拉萨经纬度:(91.00000,29.60000)<br>
    乌鲁木齐经纬度:(87.68333,43.76667)<br>
    昆明经纬度:(102.73333,25.05000)<br>
    西安经纬度:(108.95000,34.26667)<br>
    西宁经纬度:(101.75000,36.56667)<br>
    银川经纬度:(106.26667,38.46667)<br>
    兰浩特经纬度:(122.08333,46.06667)<br>
    哈尔滨经纬度:(126.63333,45.75000)<br>
    长春经纬度:(125.35000,43.88333)<br>
    武汉经纬度:(114.31667,30.51667)<br>
    郑州经纬度:(113.65000,34.76667)<br>
    石家庄经纬度:(114.48333,38.03333)<br>
    三亚经纬度:(109.50000,18.20000)<br>
    海口经纬度:(110.35000,20.01667)<br>
    澳门经纬度:(113.50000,22.20000)</p>
"""
province_city_raw = """
安徽省 合肥 北纬31.52 东经117.17<br>
    安徽省 安庆 北纬30.31 东经117.02<br>
    安徽省 蚌埠 北纬32.56 东经117.21<br>
    安徽省 亳州 北纬33.52 东经115.47<br>
    安徽省 巢湖 北纬31.36 东经117.52<br>
    安徽省 滁州 北纬32.18 东经118.18<br>
    安徽省 阜阳 北纬32.54 东经115.48<br>
    安徽省 贵池 北纬30.39 东经117.28<br>
    安徽省 淮北 北纬33.57 东经116.47<br>
    安徽省 淮南 北纬32.37 东经116.58<br>
    安徽省 黄山 北纬29.43 东经118.18<br>
    安徽省 界首 北纬33.15 东经115.21<br>
    安徽省 六安 北纬31.44 东经116.28<br>
    安徽省 马鞍山 北纬31.43 东经118.28<br>
    安徽省 明光 北纬32.47 东经117.58<br>
    安徽省 宿州 北纬33.38 东经116.58<br>
    安徽省 天长 北纬32.41 东经118.59<br>
    安徽省 铜陵 北纬30.56 东经117.48<br>
    安徽省 芜湖 北纬31.19 东经118.22<br>
    安徽省 宣州 北纬30.57 东经118.44<br>
    澳门省 澳门 北纬21.33 东经115.07<br>
    福建省 福州 北纬26.05 东经119.18<br>
    福建省 长乐 北纬25.58 东经119.31<br>
    福建省 福安 北纬27.06 东经119.39<br>
    福建省 福清 北纬25.42 东经119.23<br>
    福建省 建瓯 北纬27.03 东经118.20<br>
    福建省 建阳 北纬27.21 东经118.07<br>
    福建省 晋江 北纬24.49 东经118.35<br>
    福建省 龙海 北纬24.26 东经117.48<br>
    福建省 龙岩 北纬25.06 东经117.01<br>
    福建省 南安 北纬24.57 东经118.23<br>
    福建省 南平 北纬26.38 东经118.10<br>
    福建省 宁德 北纬26.39 东经119.31<br>
    福建省 莆田 北纬24.26 东经119.01<br>
    福建省 泉州 北纬24.56 东经118.36<br>
    福建省 三明 北纬26.13 东经117.36<br>
    福建省 邵武 北纬27.20 东经117.29<br>
    福建省 石狮 北纬24.44 东经118.38<br>
    福建省 武夷山 北纬27.46 东经118.02<br>
    福建省 厦门 北纬24.27 东经118.06<br>
    福建省 永安 北纬25.58 东经117.23<br>
    福建省 漳平 北纬25.17 东经117.24<br>
    福建省 漳州 北纬24.31 东经117.39<br>
    甘肃省 兰州 北纬36.04 东经103.51<br>
    甘肃省 白银 北纬36.33 东经104.12<br>
    甘肃省 敦煌 北纬40.08 东经94.41<br>
    甘肃省 嘉峪关 北纬39.48 东经98.14<br>
    甘肃省 金昌 北纬38.28 东经102.10<br>
    甘肃省 酒泉 北纬39.44 东经98.31<br>
    甘肃省 临夏 北纬35.37 东经103.12<br>
    甘肃省 平凉 北纬35.32 东经106.40<br>
    甘肃省 天水 北纬34.37 东经105.42<br>
    甘肃省 武威 北纬37.56 东经102.39<br>
    甘肃省 西峰 北纬35.45 东经107.40<br>
    甘肃省 玉门 北纬39.49 东经97.35<br>
    甘肃省 张掖 北纬38.56 东经100.26<br>
    广东省 广州 北纬23.08 东经113.14<br>
    广东省 潮阳 北纬23.16 东经116.36<br>
    广东省 潮州 北纬23.40 东经116.38<br>
    广东省 澄海 北纬23.28 东经116.46<br>
    广东省 从化 北纬23.33 东经113.33<br>
    广东省 东莞 北纬23.02 东经113.45<br>
    广东省 恩平 北纬22.12 东经112.19<br>
    广东省 佛山 北纬23.02 东经113.06<br>
    广东省 高明 北纬22.53 东经112.50<br>
    广东省 高要 北纬23.02 东经112.26<br>
    广东省 高州 北纬21.54 东经110.50<br>
    广东省 鹤山 北纬22.46 东经112.57<br>
    广东省 河源 北纬23.43 东经114.41<br>
    广东省 花都 北纬23.23 东经113.12<br>
    广东省 化州 北纬21.39 东经110.37<br>
    广东省 惠阳 北纬22.48 东经114.28<br>
    广东省 惠州 北纬23.05 东经114.22<br>
    广东省 江门 北纬22.35 东经113.04<br>
    广东省 揭阳 北纬22.32 东经116.21<br>
    广东省 开平 北纬22.22 东经112.40<br>
    广东省 乐昌 北纬25.09 东经113.21<br>
    广东省 雷州 北纬20.54 东经110.04<br>
    广东省 廉江 北纬21.37 东经110.17<br>
    广东省 连州 北纬24.48 东经112.23<br>
    广东省 罗定 北纬22.46 东经111.33<br>
    广东省 茂名 北纬21.40 东经110.53<br>
    广东省 梅州 北纬24.19 东经116.07<br>
    广东省 南海 北纬23.01 东经113.09<br>
    广东省 番禺 北纬22.57 东经113.22<br>
    广东省 普宁 北纬23.18 东经116.10<br>
    广东省 清远 北纬23.42 东经113.01<br>
    广东省 三水 北纬23.10 东经112.52<br>
    广东省 汕头 北纬23.22 东经116.41<br>
    广东省 汕尾 北纬22.47 东经115.21<br>
    广东省 韶关 北纬24.48 东经113.37<br>
    广东省 深圳 北纬22.33 东经114.07<br>
    广东省 顺德 北纬22.50 东经113.15<br>
    广东省 四会 北纬23.21 东经112.41<br>
    广东省 台山 北纬22.15 东经112.48<br>
    广东省 吴川 北纬21.26 东经110.47<br>
    广东省 新会 北纬22.32 东经113.01<br>
    广东省 兴宁 北纬24.09 东经115.43<br>
    广东省 阳春 北纬22.10 东经111.48<br>
    广东省 阳江 北纬21.50 东经111.58<br>
    广东省 英德 北纬24.10 东经113.22<br>
    广东省 云浮 北纬22.57 东经112.02<br>
    广东省 增城 北纬23.18 东经113.49<br>
    广东省 湛江 北纬21.11 东经110.24<br>
    广东省 肇庆 北纬23.03 东经112.27<br>
    广东省 中山 北纬22.31 东经113.22<br>
    广东省 珠海 北纬22.17 东经113.34<br>
    广西自治区 南宁 北纬22.48 东经108.19<br>
    广西自治区 北海 北纬21.28 东经109.07<br>
    广西自治区 北流 北纬22.42 东经110.21<br>
    广西自治区 百色 北纬23.54 东经106.36<br>
    广西自治区 防城港 北纬21.37 东经108.20<br>
    广西自治区 贵港 北纬23.06 东经109.36<br>
    广西自治区 桂林 北纬25.17 东经110.17<br>
    广西自治区 桂平 北纬23.22 东经110.04<br>
    广西自治区 河池 北纬24.42 东经108.03<br>
    广西自治区 合山 北纬23.47 东经108.52<br>
    广西自治区 柳州 北纬23.19 东经109.24<br>
    广西自治区 赁祥 北纬22.07 东经106.44<br>
    广西自治区 钦州 北纬21.57 东经108.37<br>
    广西自治区 梧州 北纬23.29 东经111.20<br>
    广西自治区 玉林 北纬22.38 东经110.09<br>
    广西自治区 宜州 北纬24.28 东经108.40<br>
    贵州省 贵阳 北纬26.35 东经106.42<br>
    贵州省 安顺 北纬26.14 东经105.55<br>
    贵州省 毕节 北纬27.18 东经105.18<br>
    贵州省 赤水 北纬28.34 东经105.42<br>
    贵州省 都匀 北纬26.15 东经107.31<br>
    贵州省 凯里 北纬26.35 东经107.58<br>
    贵州省 六盘水 北纬26.35 东经104.50<br>
    贵州省 清镇 北纬26.33 东经106.27<br>
    贵州省 铜仁 北纬27.43 东经109.12<br>
    贵州省 兴义 北纬25.05 东经104.53<br>
    贵州省 遵义 北纬27.42 东经106.55<br>
    海南省 海口 北纬20.02 东经110.20<br>
    海南省 儋州 北纬19.31 东经109.34<br>
    海南省 琼海 北纬19.14 东经110.28<br>
    海南省 琼山 北纬19.59 东经110.21<br>
    海南省 三亚 北纬18.14 东经109.31<br>
    海南省 通什 北纬18.46 东经109.31<br>
    河北省 石家庄 北纬38.02 东经114.30<br>
    河北省 安国 北纬38.24 东经115.20<br>
    河北省 保定 北纬38.51 东经115.30<br>
    河北省 霸州 北纬39.06 东经116.24<br>
    河北省 泊头 北纬38.04 东经116.34<br>
    河北省 沧州 北纬38.18 东经116.52<br>
    河北省 承德 北纬40.59 东经117.57<br>
    河北省 定州 北纬38.30 东经115.00<br>
    河北省 丰南 北纬39.34 东经118.06<br>
    河北省 高碑店 北纬39.20 东经115.51<br>
    河北省 蒿城 北纬38.02 东经114.50<br>
    河北省 邯郸 北纬36.36 东经114.28<br>
    河北省 河间 北纬38.26 东经116.05<br>
    河北省 衡水 北纬37.44 东经115.42<br>
    河北省 黄骅 北纬38.21 东经117.21<br>
    河北省 晋州 北纬38.02 东经115.02<br>
    河北省 冀州 北纬37.34 东经115.33<br>
    河北省 廓坊 北纬39.31 东经116.42<br>
    河北省 鹿泉 北纬38.04 东经114.19<br>
    河北省 南宫 北纬37.22 东经115.23<br>
    河北省 秦皇岛 北纬39.55 东经119.35<br>
    河北省 任丘 北纬38.42 东经116.07<br>
    河北省 三河 北纬39.58 东经117.04<br>
    河北省 沙河 北纬36.51 东经114.30<br>
    河北省 深州 北纬38.01 东经115.32<br>
    河北省 唐山 北纬39.36 东经118.11<br>
    河北省 武安 北纬36.42 东经114.11<br>
    河北省 邢台 北纬37.04 东经114.30<br>
    河北省 辛集 北纬37.54 东经115.12<br>
    河北省 新乐 北纬38.20 东经114.41<br>
    河北省 张家口 北纬40.48 东经114.53<br>
    河北省 涿州 北纬39.29 东经115.59<br>
    河北省 遵化 北纬40.11 东经117.58<br>
    河南省 郑州 北纬34.46 东经11340<br>
    河南省 安阳 北纬36.06 东经114.21<br>
    河南省 长葛 北纬34.12 东经113.47<br>
    河南省 登封 北纬34.27 东经113.02<br>
    河南省 邓州 北纬32.42 东经112.05<br>
    河南省 巩义 北纬34.46 东经112.58<br>
    河南省 鹤壁 北纬35.54 东经114.11<br>
    河南省 辉县 北纬35.27 东经113.47<br>
    河南省 焦作 北纬35.14 东经113.12<br>
    河南省 济源 北纬35.04 东经112.35<br>
    河南省 开封 北纬34.47 东经114.21<br>
    河南省 灵宝 北纬34.31 东经110.52<br>
    河南省 林州 北纬36.03 东经113.49<br>
    河南省 漯河 北纬33.33 东经114.02<br>
    河南省 洛阳 北纬34.41 东经112.27<br>
    河南省 南阳 北纬33.00 东经112.32<br>
    河南省 平顶山 北纬33.44 东经113.17<br>
    河南省 濮阳 北纬35.44 东经115.01<br>
    河南省 沁阳 北纬35.05 东经112.57<br>
    河南省 汝州 北纬34.09 东经112.50<br>
    河南省 三门峡 北纬34.47 东经111.12<br>
    河南省 商丘 北纬34.26 东经115.38<br>
    河南省 卫辉 北纬35.24 东经114.03<br>
    河南省 舞钢 北纬33.17 东经113.30<br>
    河南省 项城 北纬33.26 东经114.54<br>
    河南省 荥阳 北纬34.46 东经113.21<br>
    河南省 新密 北纬34.31 东经113.22<br>
    河南省 新乡 北纬35.18 东经113.52<br>
    河南省 信阳 北纬32.07 东经114.04<br>
    河南省 新郑 北纬34.24 东经113.43<br>
    河南省 许昌 北纬34.01 东经113.49<br>
    河南省 偃师 北纬34.43 东经112.47<br>
    河南省 义马 北纬34.43 东经111.55<br>
    河南省 禹州 北纬34.09 东经113.28<br>
    河南省 周口 北纬33.37 东经114.38<br>
    河南省 驻马店 北纬32.58 东经114.01<br>
    黑龙江省 哈尔滨 北纬45.44 东经126.36<br>
    黑龙江省 阿城 北纬45.32 东经126.58<br>
    黑龙江省 安达 北纬46.24 东经125.18<br>
    黑龙江省 北安 北纬48.15 东经126.31<br>
    黑龙江省 大庆 北纬46.36 东经125.01<br>
    黑龙江省 富锦 北纬47.15 东经132.02<br>
    黑龙江省 海林 北纬44.35 东经129.21<br>
    黑龙江省 海伦 北纬47.28 东经126.57<br>
    黑龙江省 鹤岗 北纬47.20 东经130.16<br>
    黑龙江省 黑河 北纬50.14 东经127.29<br>
    黑龙江省 佳木斯 北纬46.47 东经130.22<br>
    黑龙江省 鸡西 北纬45.17 东经130.57<br>
    黑龙江省 密山 北纬45.32 东经131.50<br>
    黑龙江省 牡丹江 北纬44.35 东经129.36<br>
    黑龙江省 讷河 北纬48.29 东经124.51<br>
    黑龙江省 宁安 北纬44.21 东经129.28<br>
    黑龙江省 齐齐哈尔 北纬47.20 东经123.57<br>
    黑龙江省 七台河 北纬45.48 东经130.49<br>
    黑龙江省 双城 北纬45.22 东经126.15<br>
    黑龙江省 尚志 北纬45.14 东经127.55<br>
    黑龙江省 双鸭山 北纬46.38 东经131.11<br>
    黑龙江省 绥芬河 北纬44.25 东经131.11<br>
    黑龙江省 绥化 北纬46.38 东经126.59<br>
    黑龙江省 铁力 北纬46.59 东经128.01<br>
    黑龙江省 同江 北纬47.39 东经132.30<br>
    黑龙江省 五常 北纬44.55 东经127.11<br>
    黑龙江省 五大连池 北纬48.38 东经126.07<br>
    黑龙江省 伊春 北纬47.42 东经128.56<br>
    黑龙江省 肇东 北纬46.04 东经125.58<br>
    湖北省 武汉 北纬30.35 东经114.17<br>
    湖北省 安陆 北纬31.15 东经113.41<br>
    湖北省 当阳 北纬30.50 东经111.47<br>
    湖北省 丹江口 北纬32.33 东经108.30<br>
    湖北省 大冶 北纬30.06 东经114.58<br>
    湖北省 恩施 北纬30.16 东经109.29<br>
    湖北省 鄂州 北纬30.23 东经114.52<br>
    湖北省 广水 北纬31.37 东经113.48<br>
    湖北省 洪湖 北纬29.48 东经113.27<br>
    湖北省 黄石 北纬30.12 东经115.06<br>
    湖北省 黄州 北纬30.27 东经114.52<br>
    湖北省 荆门 北纬31.02 东经112.12<br>
    湖北省 荆沙 北纬30.18 东经112.16<br>
    湖北省 老河口 北纬32.23 东经111.40<br>
    湖北省 利川 北纬30.18 东经108.56<br>
    湖北省 麻城 北纬31.10 东经115.01<br>
    湖北省 浦圻 北纬29.42 东经113.51<br>
    湖北省 潜江 北纬30.26 东经112.53<br>
    湖北省 石首 北纬29.43 东经112.24<br>
    湖北省 十堰 北纬32.40 东经110.47<br>
    湖北省 随州 北纬31.42 东经113.22<br>
    湖北省 天门 北纬60.39 东经113.10<br>
    湖北省 武穴 北纬29.51 东经115.33<br>
    湖北省 襄樊 北纬32.02 东经112.08<br>
    湖北省 咸宁 北纬29.53 东经114.17<br>
    湖北省 仙桃 北纬30.22 东经113.27<br>
    湖北省 孝感 北纬30.56 东经113.54<br>
    湖北省 宜昌 北纬30.42 东经111.17<br>
    湖北省 宜城 北纬31.42 东经112.15<br>
    湖北省 应城 北纬30.57 东经113.33<br>
    湖北省 枣阳 北纬32.07 东经112.44<br>
    湖北省 枝城 北纬30.23 东经111.27<br>
    湖北省 钟祥 北纬31.10 东经112.34<br>
    湖南省 长沙 北纬28.12 东经112.59<br>
    湖南省 常德 北纬29.02 东经111.51<br>
    湖南省 郴州 北纬25.46 东经113.02<br>
    湖南省 衡阳 北纬26.53 东经112.37<br>
    湖南省 洪江 北纬27.07 东经109.59<br>
    湖南省 怀化 北纬27.33 东经109.58<br>
    湖南省 津市 北纬29.38 东经111.52<br>
    湖南省 吉首 北纬28.18 东经109.43<br>
    湖南省 耒阳 北纬26.24 东经112.51<br>
    湖南省 冷水江 北纬27.42 东经111.26<br>
    湖南省 冷水滩 北纬26.26 东经111.35<br>
    湖南省 涟源 北纬27.41 东经111.41<br>
    湖南省 醴陵 北纬27.40 东经113.30<br>
    湖南省 临湘 北纬29.29 东经113.27<br>
    湖南省 浏阳 北纬28.09 东经113.37<br>
    湖南省 娄底 北纬27.44 东经111.59<br>
    湖南省 汨罗 北纬28.49 东经113.03<br>
    湖南省 韶山 北纬27.54 东经112.29<br>
    湖南省 邵阳 北纬27.14 东经111.28<br>
    湖南省 武冈 北纬26.43 东经110.37<br>
    湖南省 湘潭 北纬27.52 东经112.53<br>
    湖南省 湘乡 北纬27.44 东经112.31<br>
    湖南省 益阳 北纬28.36 东经112.20<br>
    湖南省 永州 北纬26.13 东经111.37<br>
    湖南省 沅江 北纬28.50 东经112.22<br>
    湖南省 岳阳 北纬29.22 东经113.06<br>
    湖南省 张家界 北纬29.08 东经110.29<br>
    湖南省 株洲 北纬27.51 东经113.09<br>
    湖南省 资兴 北纬25.58 东经113.13<br>
    吉林省 长春 北纬43.54 东经125.19<br>
    吉林省 白城 北纬45.38 东经122.50<br>
    吉林省 白山 北纬41.56 东经126.26<br>
    吉林省 大安 北纬45.30 东经124.18<br>
    吉林省 德惠 北纬44.32 东经125.42<br>
    吉林省 敦化 北纬43.22 东经128.13<br>
    吉林省 公主岭 北纬43.31 东经124.49<br>
    吉林省 和龙 北纬42.32 东经129.00<br>
    吉林省 桦甸 北纬42.58 东经126.44<br>
    吉林省 珲春 北纬42.52 东经130.22<br>
    吉林省 集安 北纬41.08 东经126.11<br>
    吉林省 蛟河 北纬43.42 东经127.21<br>
    吉林省 吉林 北纬43.52 东经126.33<br>
    吉林省 九台 北纬44.09 东经125.51<br>
    吉林省 辽源 北纬42.54 东经125.09<br>
    吉林省 临江 北纬41.49 东经126.53<br>
    吉林省 龙井 北纬42.46 东经129.26<br>
    吉林省 梅河口 北纬42.32 东经125.40<br>
    吉林省 舒兰 北纬44.24 东经126.57<br>
    吉林省 四平 北纬43.10 东经124.22<br>
    吉林省 松原 北纬45.11 东经124.49<br>
    吉林省 洮南 北纬45.20 东经122.47<br>
    吉林省 通化 北纬41.43 东经125.56<br>
    吉林省 图们 北纬42.57 东经129.51<br>
    吉林省 延吉 北纬42.54 东经129.30<br>
    吉林省 愉树 北纬44.49 东经126.32<br>
    江苏省 南京 北纬32.03 东经118.46<br>
    江苏省 常熟 北纬31.39 东经120.43<br>
    江苏省 常州 北纬31.47 东经119.58<br>
    江苏省 丹阳 北纬32.00 东经119.32<br>
    江苏省 东台 北纬32.51 东经120.19<br>
    江苏省 高邮 北纬32.47 东经119.27<br>
    江苏省 海门 北纬31.53 东经121.09<br>
    江苏省 淮安 北纬33.30 东经119.09<br>
    江苏省 淮阴 北纬33.36 东经119.02<br>
    江苏省 江都 北纬32.26 东经119.32<br>
    江苏省 姜堰 北纬32.34 东经120.08<br>
    江苏省 江阴 北纬31.54 东经120.17<br>
    江苏省 靖江 北纬32.02 东经120.17<br>
    江苏省 金坛 北纬31.46 东经119.33<br>
    江苏省 昆山 北纬31.23 东经120.57<br>
    江苏省 连去港 北纬34.36 东经119.10<br>
    江苏省 溧阳 北纬31.26 东经119.29<br>
    江苏省 南通 北纬32.01 东经120.51<br>
    江苏省 邳州 北纬34.19 东经117.59<br>
    江苏省 启乐 北纬31.48 东经121.39<br>
    江苏省 如皋 北纬32.23 东经120.33<br>
    江苏省 宿迁 北纬33.58 东经118.18<br>
    江苏省 苏州 北纬31.19 东经120.37<br>
    江苏省 太仓 北纬31.27 东经121.06<br>
    江苏省 泰兴 北纬32.10 东经120.01<br>
    江苏省 泰州 北纬32.30 东经119.54<br>
    江苏省 通州 北纬32.05 东经121.03<br>
    江苏省 吴江 北纬31.10 东经120.39<br>
    江苏省 无锡 北纬31.34 东经120.18<br>
    江苏省 兴化 北纬32.56 东经119.50<br>
    江苏省 新沂 北纬34.22 东经118.20<br>
    江苏省 徐州 北纬34.15 东经117.11<br>
    江苏省 盐在 北纬33.22 东经120.08<br>
    江苏省 扬中 北纬32.14 东经119.49<br>
    江苏省 扬州 北纬32.23 东经119.26<br>
    江苏省 宜兴 北纬31.21 东经119.49<br>
    江苏省 仪征 北纬32.16 东经119.10<br>
    江苏省 张家港 北纬31.52 东经120.32<br>
    江苏省 镇江 北纬32.11 东经119.27<br>
    江西省 南昌 北纬28.40 东经115.55<br>
    江西省 德兴 北纬28.57 东经117.35<br>
    江西省 丰城 北纬28.12 东经115.48<br>
    江西省 赣州 北纬28.52 东经114.56<br>
    江西省 高安 北纬28.25 东经115.22<br>
    江西省 吉安 北纬27.07 东经114.58<br>
    江西省 景德镇 北纬29.17 东经117.13<br>
    江西省 井冈山 北纬26.34 东经114.10<br>
    江西省 九江 北纬29.43 东经115.58<br>
    江西省 乐平 北纬28.58 东经117.08<br>
    江西省 临川 北纬27.59 东经116.21<br>
    江西省 萍乡 北纬27.37 东经113.50<br>
    江西省 瑞昌 北纬29.40 东经115.38<br>
    江西省 瑞金 北纬25.53 东经116.01<br>
    江西省 上饶 北纬25.27 东经117.58<br>
    江西省 新余 北纬27.48 东经114.56<br>
    江西省 宜春 北纬27.47 东经114.23<br>
    江西省 鹰潭 北纬28.14 东经117.03<br>
    江西省 樟树 北纬28.03 东经115.32<br>
    辽宁省 沈阳 北纬41.48 东经123.25<br>
    辽宁省 鞍山 北纬41.07 东经123.00<br>
    辽宁省 北票 北纬41.48 东经120.47<br>
    辽宁省 本溪 北纬41.18 东经123.46<br>
    辽宁省 朝阳 北纬41.34 东经120.27<br>
    辽宁省 大连 北纬38.55 东经121.36<br>
    辽宁省 丹东 北纬40.08 东经124.22<br>
    辽宁省 大石桥 北纬40.37 东经122.31<br>
    辽宁省 东港 北纬39.53 东经124.08<br>
    辽宁省 凤城 北纬40.28 东经124.02<br>
    辽宁省 抚顺 北纬41.51 东经123.54<br>
    辽宁省 阜新 北纬42.01 东经121.39<br>
    辽宁省 盖州 北纬40.24 东经122.21<br>
    辽宁省 海城 北纬40.51 东经122.43<br>
    辽宁省 葫芦岛 北纬40.45 东经120.51<br>
    辽宁省 锦州 北纬41.07 东经121.09<br>
    辽宁省 开原 北纬42.32 东经124.02<br>
    辽宁省 辽阳 北纬41.16 东经123.12<br>
    辽宁省 凌海 北纬41.10 东经121.21<br>
    辽宁省 凌源 北纬41.14 东经119.22<br>
    辽宁省 盘锦 北纬41.07 东经122.03<br>
    辽宁省 普兰店 北纬39.23 东经121.58<br>
    辽宁省 铁法 北纬42.28 东经123.32<br>
    辽宁省 铁岭 北纬42.18 东经123.51<br>
    辽宁省 瓦房店 北纬39.37 东经122.00<br>
    辽宁省 兴城 北纬40.37 东经120.41<br>
    辽宁省 新民 北纬41.59 东经122.49<br>
    辽宁省 营口 北纬40.39 东经122.13<br>
    辽宁省 庄河 北纬39.41 东经122.58<br>
    内自治区 呼和浩特 北纬40.48 东经111.41<br>
    内自治区 包头 北纬40.39 东经109.49<br>
    内自治区 赤峰 北纬42.17 东经118.58<br>
    内自治区 东胜 北纬39.48 东经109.59<br>
    内自治区 二连浩特 北纬43.38 东经111.58<br>
    内自治区 额尔古纳 北纬50.13 东经120.11<br>
    内自治区 丰镇 北纬40.27 东经113.09<br>
    内自治区 根河 北纬50.48 东经121.29<br>
    内自治区 海拉尔 北纬49.12 东经119.39<br>
    内自治区 霍林郭勒 北纬45.32 东经119.38<br>
    内自治区 集宁 北纬41.02 东经113.06<br>
    内自治区 临河 北纬40.46 东经107.22<br>
    内自治区 满洲里 北纬49.35 东经117.23<br>
    内自治区 通辽 北纬43.37 东经122.16<br>
    内自治区 乌兰浩特 北纬46.03 东经122.03<br>
    内自治区 乌海 北纬39.40 东经106.48<br>
    内自治区 锡林浩特 北纬43.57 东经116.03<br>
    内自治区 牙克石 北纬49.17 东经120.40<br>
    内自治区 扎兰屯 北纬48.00 东经122.47<br>
    宁夏自治区 银川 北纬38.27 东经106.16<br>
    宁夏自治区 青铜峡 北纬37.56 东经105.59<br>
    宁夏自治区 石嘴山 北纬39.02 东经106.22<br>
    宁夏自治区 吴忠 北纬37.59 东经106.11<br>
    青海省 西宁 北纬36.38 东经101.48<br>
    青海省 德令哈 北纬37.22 东经97.23<br>
    青海省 格尔木 北纬36.26 东经94.55<br>
    山东省 济南 北纬36.40 东经117.00<br>
    山东省 安丘 北纬36.25 东经119.12<br>
    山东省 滨州 北纬37.22 东经118.02<br>
    山东省 昌邑 北纬39.52 东经119.24<br>
    山东省 德州 北纬37.26 东经116.17<br>
    山东省 东营 北纬37.27 东经118.30<br>
    山东省 肥城 北纬36.14 东经116.46<br>
    山东省 高密 北纬36.22 东经119.44<br>
    山东省 菏泽 北纬35.14 东经115.26<br>
    山东省 胶南 北纬35.53 东经119.58<br>
    山东省 胶州 北纬36.17 东经120.00<br>
    山东省 即墨 北纬36.22 东经120.28<br>
    山东省 济宁 北纬35.23 东经116.33<br>
    山东省 莱芜 北纬36.12 东经117.40<br>
    山东省 莱西 北纬36.52 东经120.31<br>
    山东省 莱阳 北纬36.58 东经120.42<br>
    山东省 莱州 北纬37.10 东经119.57<br>
    山东省 乐陵 北纬37.44 东经117.12<br>
    山东省 聊城 北纬36.26 东经115.57<br>
    山东省 临清 北纬36.51 东经115.42<br>
    山东省 临沂 北纬35.03 东经118.20<br>
    山东省 龙口 北纬37.39 东经120.21<br>
    山东省 蓬莱 北纬37.48 东经120.45<br>
    山东省 平度 北纬36.47 东经119.58<br>
    山东省 青岛 北纬36.03 东经120.18<br>
    山东省 青州 北纬36.42 东经118.28<br>
    山东省 曲阜 北纬35.36 东经116.58<br>
    山东省 日照 北纬35.23 东经119.32<br>
    山东省 荣成 北纬37.10 东经122.25<br>
    山东省 乳山 北纬36.54 东经121.31<br>
    山东省 寿光 北纬36.53 东经118.44<br>
    山东省 泰安 北纬36.11 东经117.08<br>
    山东省 滕州 北纬35.06 东经117.09<br>
    山东省 潍坊 北纬36.43 东经119.06<br>
    山东省 威海 北纬37.31 东经122.07<br>
    山东省 文登 北纬37.12 东经122.03<br>
    山东省 新泰 北纬35.54 东经117.45<br>
    山东省 烟台 北纬37.32 东经121.24<br>
    山东省 兖州 北纬35.32 东经116.49<br>
    山东省 禹城 北纬36.56 东经116.39<br>
    山东省 枣庄 北纬34.52 东经117.33<br>
    山东省 章丘 北纬36.43 东经117.32<br>
    山东省 招远 北纬37.21 东经120.23<br>
    山东省 诸城 北纬35.59 东经119.24<br>
    山东省 淄博 北纬36.48 东经118.03<br>
    山东省 邹城 北纬35.24 东经116.58<br>
    山西省 太原 北纬37.54 东经112.33<br>
    山西省 长治 北纬36.11 东经113.06<br>
    山西省 大同 北纬40.06 东经113.17<br>
    山西省 高平 北纬35.48 东经112.55<br>
    山西省 古交 北纬37.54 东经112.09<br>
    山西省 河津 北纬35.35 东经110.41<br>
    山西省 侯马 北纬35.37 东经111.21<br>
    山西省 霍州 北纬36.34 东经111.42<br>
    山西省 介休 北纬37.02 东经111.55<br>
    山西省 晋城 北纬35.30 东经112.51<br>
    山西省 临汾 北纬36.05 东经111.31<br>
    山西省 潞城 北纬36.21 东经113.14<br>
    山西省 朔州 北纬39.19 东经112.26<br>
    山西省 孝义 北纬37.08 东经111.48<br>
    山西省 忻州 北纬38.24 东经112.43<br>
    山西省 阳泉 北纬37.51 东经113.34<br>
    山西省 永济 北纬34.52 东经110.27<br>
    山西省 原平 北纬38.43 东经112.42<br>
    山西省 榆次 北纬37.41 东经112.43<br>
    山西省 运城 北纬35.02 东经110.59<br>
    陕西省 西安 北纬34.17 东经108.57<br>
    陕西省 安康 北纬32.41 东经109.01<br>
    陕西省 宝鸡 北纬34.22 东经107.09<br>
    陕西省 韩城 北纬35.28 东经110.27<br>
    陕西省 汉中 北纬33.04 东经107.01<br>
    陕西省 华阴 北纬34.34 东经110.05<br>
    陕西省 商州 北纬33.52 东经109.57<br>
    陕西省 铜川 北纬35.06 东经109.07<br>
    陕西省 渭南 北纬34.30 东经109.30<br>
    陕西省 咸阳 北纬34.20 东经108.43<br>
    陕西省 兴平 北纬34.18 东经108.29<br>
    陕西省 延安 北纬36.35 东经109.28<br>
    陕西省 榆林 北纬38.18 东经109.47<br>
    上海市 上海市 北纬31.14 东经121.29<br>
    四川省 成都 北纬30.40 东经104.04<br>
    四川省 巴中 北纬31.51 东经106.43<br>
    四川省 崇州 北纬30.39 东经103.40<br>
    四川省 达川 北纬31.14 东经107.29<br>
    四川省 德阳 北纬31.09 东经104.22<br>
    四川省 都江堰 北纬31.01 东经103.37<br>
    四川省 峨眉山 北纬29.36 东经103.29<br>
    四川省 涪陵 北纬29.42 东经107.22<br>
    四川省 广汉 北纬30.58 东经104.15<br>
    四川省 广元 北纬32.28 东经105.51<br>
    四川省 华蓥 北纬30.26 东经106.44<br>
    四川省 简阳 北纬30.24 东经104.32<br>
    四川省 江油 北纬31.48 东经104.42<br>
    四川省 阆中 北纬31.36 东经105.58<br>
    四川省 乐山 北纬29.36 东经103.44<br>
    四川省 泸州 北纬28.54 东经105.24<br>
    四川省 绵阳 北纬31.30 东经104.42<br>
    四川省 南充 北纬30.49 东经106.04<br>
    四川省 内江 北纬29.36 东经105.02<br>
    四川省 攀枝花 北纬26.34 东经101.43<br>
    四川省 彭州 北纬30.59 东经103.57<br>
    四川省 邛崃 北纬30.26 东经103.28<br>
    四川省 遂宁 北纬30.31 东经105.33<br>
    四川省 万县 北纬30.50 东经108.21<br>
    四川省 万源 北纬32.03 东经108.03<br>
    四川省 西昌 北纬27.54 东经102.16<br>
    四川省 雅安 北纬29.59 东经102.59<br>
    四川省 宜宾 北纬28.47 东经104.34<br>
    四川省 自贡 北纬29.23 东经104.46<br>
    四川省 资阳 北纬30.09 东经104.38<br>
    台湾省 台北市 北纬25.03 东经121.30<br>
    天津市 天津市 北纬39.02 东经117.12<br>
    西藏自治区 拉萨 北纬29.39 东经91.08<br>
    西藏自治区 日喀则 北纬29.16 东经88.51<br>
    香港 香港市 北纬21.23 东经115.12<br>
    新疆自治区 乌鲁木齐 北纬43.45 东经87.36<br>
    新疆自治区 阿克苏 北纬41.09 东经80.19<br>
    新疆自治区 阿勒泰 北纬47.50 东经88.12<br>
    新疆自治区 阿图什 北纬39.42 东经76.08<br>
    新疆自治区 博乐 北纬44.57 东经82.08<br>
    新疆自治区 昌吉 北纬44.02 东经87.18<br>
    新疆自治区 阜康 北纬44.09 东经87.58<br>
    新疆自治区 哈密 北纬42.50 东经93.28<br>
    新疆自治区 和田 北纬37.09 东经79.55<br>
    新疆自治区 克拉玛依 北纬45.36 东经84.51<br>
    新疆自治区 喀什 北纬39.30 东经75.59<br>
    新疆自治区 库尔勒 北纬41.46 东经86.07<br>
    新疆自治区 奎屯 北纬44.27 东经84.56<br>
    新疆自治区 石河子 北纬44.18 东经86.00<br>
    新疆自治区 塔城 北纬46.46 东经82.59<br>
    新疆自治区 吐鲁番 北纬42.54 东经89.11<br>
    新疆自治区 伊宁 北纬43.55 东经81.20<br>
    云南省 昆明 北纬25.04 东经102.42<br>
    云南省 保山 北纬25.08 东经99.10<br>
    云南省 楚雄 北纬25.01 东经101.32<br>
    云南省 大理 北纬25.34 东经100.13<br>
    云南省 东川 北纬26.06 东经103.12<br>
    云南省 个旧 北纬23.21 东经103.09<br>
    云南省 景洪 北纬22.01 东经100.48<br>
    云南省 开远 北纬23.43 东经103.13<br>
    云南省 曲靖 北纬25.30 东经103.48<br>
    云南省 瑞丽 北纬24.00 东经97.50<br>
    云南省 思茅 北纬22.48 东经100.58<br>
    云南省 畹町 北纬24.06 东经98.04<br>
    云南省 宣威 北纬26.13 东经104.06<br>
    云南省 玉溪 北纬24.22 东经102.32<br>
    云南省 昭通 北纬27.20 东经103.42<br>
    浙江省 杭州 北纬30.16 东经120.10<br>
    浙江省 慈溪 北纬30.11 东经121.15<br>
    浙江省 东阳 北纬29.16 东经120.14<br>
    浙江省 奉化 北纬29.39 东经121.24<br>
    浙江省 富阳 北纬30.03 东经119.57<br>
    浙江省 海宁 北纬30.32 东经120.42<br>
    浙江省 湖州 北纬30.52 东经120.06<br>
    浙江省 建德 北纬29.29 东经119.16<br>
    浙江省 江山 北纬28.45 东经118.37<br>
    浙江省 嘉兴 北纬30.46 东经120.45<br>
    浙江省 金华 北纬29.07 东经119.39<br>
    浙江省 兰溪 北纬29.12 东经119.28<br>
    浙江省 临海 北纬28.51 东经121.08<br>
    浙江省 丽水 北纬28.27 东经119.54<br>
    浙江省 龙泉 北纬28.04 东经119.08<br>
    浙江省 宁波 北纬29.52 东经121.33<br>
    浙江省 平湖 北纬30.42 东经121.01<br>
    浙江省 衢州 北纬28.58 东经118.52<br>
    浙江省 瑞安 北纬27.48 东经120.38<br>
    浙江省 上虞 北纬30.01 东经120.52<br>
    浙江省 绍兴 北纬30.00 东经120.34<br>
    浙江省 台州 北纬28.41 东经121.27<br>
    浙江省 桐乡 北纬30.38 东经120.32<br>
    浙江省 温岭 北纬28.22 东经121.21<br>
    浙江省 温州 北纬28.01 东经120.39<br>
    浙江省 萧山 北纬30.09 东经120.16<br>
    浙江省 义乌 北纬29.18 东经120.04<br>
    浙江省 乐清 北纬28.08 东经120.58<br>
    浙江省 余杭 北纬30.26 东经120.18<br>
    浙江省 余姚 北纬30.02 东经121.10<br>
    浙江省 永康 北纬29.54 东经120.01<br>
    浙江省 舟山 北纬30.01 东经122.06<br>
    浙江省 诸暨 北纬29.43 东经120.14<br>
    重庆市 重庆市 北纬29.35 东经106.33<br>
    重庆市 合川市 北纬30.02 东经106.15<br>
    重庆市 江津市 北纬29.18 东经106.16<br>
    重庆市 南川市 北纬29.10 东经107.05<br>
    重庆市 永川市 北纬29.23 东经105.53<br>
"""
_index = 0
city_loc_list = []
duplicate_city_list = []
for line in city_loc_raw.splitlines():
    line = line.strip()
    if line:
        index1 = line.index("经纬度")
        city = line[:index1]
        begin_index, end_index = line.index("("), line.index(")")
        lon, lat = line[begin_index + 1:end_index].split(",")
        # generated_by_dict_unpack: float(
        lon, lat = float(lon), float(lat)
        city_loc_list.append(
            [_index, city, (lon, lat)]
        )
        duplicate_city_list.append(city)
        _index += 1

for line in province_city_raw.splitlines():
    line = line.strip()
    if line:
        lat_index = line.index("北纬")
        lon_index = line.index("东经")
        end_index = line.index("<")
        city = line[:lat_index].strip().split(" ")[1]
        lat = float(line[lat_index + 2:lon_index].strip())
        lon = float(line[lon_index + 2:end_index])
        if city not in duplicate_city_list:
            city_loc_list.append(
                [
                    _index, city, (lon, lat)
                ]
            )
            _index += 1
            duplicate_city_list.append(city)

if __name__ == "__main__":
    print(city_loc_list)
