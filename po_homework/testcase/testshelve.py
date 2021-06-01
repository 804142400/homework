import shelve


def test_shelve():
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                'value': '1688850481935123'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'u4yNaE89OY6_EM_tLGgumEwaUlNGQVm0ebyZGEaPX8Mcq7YOgWdcG9MzDeSlJEOE65j0vmBc5DBFox6-x7YEqxlBGpyxOhBz3qiehno8EZkRBd-jGj_nkVvF60PMGsNHhWxmZVyKYwKYp2cxropkQ2UfpFdSZK_zzqLigJRk_fdyPVhONUiZK34E8z4hvW0oN-P5y1FpLe6XLiQh1VtNghWEx-2knp-0lYXhBd8XMFPTD11GXmeT_TFZNlmXXMRin-WYr9k1J-SY9HuG_PuyfA'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                'value': '1688850481935123'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False, 'value': '1970325097443930'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': '9r-KGhPmw0CutucPTXb1FPq3n09NusWGAxKlJqR_K9wXAeEBT-aXwSxClq83LD7H'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a9840836'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649849926, 'httpOnly': False,
                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                     'value': '1618228058,1618231569,1618234212,1618313927'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1621060201, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'},
               {'domain': '.qq.com', 'expiry': 1681540198, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.2009980336.1618067759'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1649603602, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.qq.com', 'expiry': 1619610310, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
                'secure': False, 'value': '804142400'},
               {'domain': '.qq.com', 'expiry': 2147483651, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                'secure': False, 'value': '155fbb3075715e13aa181ff31621a2cebd9b969e2f390755940c7f091f406be5'},
               {'domain': '.qq.com', 'expiry': 2147483659, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False, 'value': '19QkhYI3tf'},
               {'domain': '.qq.com', 'expiry': 1618554598, 'httpOnly': False, 'name': '_gid', 'path': '/',
                'secure': False, 'value': 'GA1.2.151745177.1618468189'},
               {'domain': 'work.weixin.qq.com', 'expiry': 1618499723, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
                'secure': False, 'value': '3482nm1'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                'value': '3367730841780216'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/',
                'secure': False, 'value': ''},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                'secure': False, 'value': '1221384192'}]

    db = shelve.open('./mydb/cookies')
    db['cookie'] = cookies
    db.close()

