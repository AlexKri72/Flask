# �������� ���������, ������� ��������� ������ �� 10 URL-������� � ������������ ��������� ������ � ������� ������.
# ����� �������� ������ ����� �������� �� � ��������� �����.
# ����������� ������.
import threading,requests
urls=[
    'https://about.google/?utm_source=google-RU&utm_medium=referral&utm_campaign=hp-footer&fg=1',
    'https://www.python.org/',
    'https://www.youryoga.org/',
    'https://omoda.ru/models/modelc5/?utm_source=yandex&utm_medium=cpc&utm_campaign=2023_OMODA_C5_always-on-apr-dec_search_brand&utm_term=omoda&utm_content=ad_id%7C13819124806%7Cbanner_id%7C13819124806%7Ccampaign_type%7Ctype1%7Ccampaign_id%7C85691854%7Cdevice_type%7Cdesktop%7Cgroup_id%7C5164735841%7Cphrase_id%7C44049909178%7Cposition%7C1%7Cposition_type%7Cpremium%7Cplacement%7Cnone%7Cplacement_type%7Csearch%7Cregion_name%7C������&calltouch_tm=yd_c:85691854_gb:5164735841_ad:13819124806_ph:44049909178_st:search_pt:premium_p:1_s:none_dt:desktop_reg:55_ret:44049909178_apt:none&yclid=12853616667909423103',
    'https://www.chery.ru/',
    'https://www.lada.ru/'
]

def get_urls(url:str,file_name):
    responce=requests.get(url)
    with open(f'{file_name}','w',encoding='utf-8') as f:
        f.write(responce.text)

if __name__=='__main__':
    threads=[]
    for url in urls:
        t= threading.Thread(target=get_urls,args=(url,f'thread_{url.split(".")[1]}'))
        threads.append(t)

    for item in threads:
        item.start()

    for item in threads:
        item.join()