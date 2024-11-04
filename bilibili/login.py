import requests
import time


"""
    source: main-fe-header
    username: 12222225
    password: WmQJ2dXQFvMSCjaJIGp6tTTxmMRZk67EmU+oL4JcIeSFK0CXd4A1uQnGKMPiAadEx4cGtdtiAKrpMo86T4zmJBEjC+r1OtV6Xjify81Qa/ytamD/AkJGYKDLLqRbZslA1ubGM3OB90btYaekotdV5vxRfDaJTOzI0sbqlgJRcxI=
    go_url: https://www.bilibili.com/
    validate: 843084f631994332c2413ed3ebcaaefc
    token: 9541d308914b43cdbbd60c8d4a311b96
    seccode: 843084f631994332c2413ed3ebcaaefc|jordan
    challenge: d41bfaefa0ab9d04f05bf4943a518aad
"""

url="https://www.bilibili.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "Referer":"https://www.baidu.com/link?url=IyJTqjtYHaZAwRmkZif4IshnzBn2kOokiARRrysoJB4GuvG6eSv2NA1opF3-FU5Q&wd=&eqid=a81afc3d001dc1dc0000000567273ff4",
    "cookie":"buvid3=54AC4795-988C-EF61-D016-7112F474D5B535606infoc; b_nut=1714118135; _uuid=EA993AD10-371E-3C89-1EB8-2BB34B75A6D923287infoc; buvid4=0B6F012D-1FAF-80BC-5A3F-F00DBB566EB836424-024042607-AM/hD9Dy83FqZl7OKM2/vA%3D%3D; buvid_fp=e4ee8123bedc5015251c5d9f39b139ee; rpdid=|(u)mmYku~ul0J'u~uRuu)uJ~; enable_web_push=DISABLE; header_theme_version=CLOSE; PVID=1; CURRENT_FNVAL=4048; is-2022-channel=1; bsource=search_baidu; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4ODQ3MzUsImlhdCI6MTczMDYyNTQ3NSwicGx0IjotMX0.sypZlpi68BiIgFUA4yonayhgIcRn37hF_UVgpXow0og; bili_ticket_expires=1730884675; b_lsid=F11031823_192F1F6F24B; SESSDATA=da16dafd%2C1746191493%2C46a60%2Ab1CjDHPWgZjvdUuB6J0KNUzql4WeNURjfPR93OfNFov6yTE5lvvpFCE4rjf_M5mkPntv4SVmU3V0I1WmlzMkpORjVSUzZPNG9ZN2h3eGMtRW5oZ3NhcmhoYzliUjlPZ19PeXlzWnY4UHFITUtURUh1bFpqMG82RDBFTU5hR1pKalVJUXVGazkxTkhRIIEC; bili_jct=34ad28e1465def63d84519d1b1f818a5; DedeUserID=631861169; DedeUserID__ckMd5=5d4e866c827e6514; sid=qa1j8zlh; home_feed_column=4; browser_resolution=371-954",
}
res=requests.get(url=url,headers=headers)
print(res.status_code)