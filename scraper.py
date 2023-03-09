from playwright.sync_api import sync_playwright


amazon_url = 'https://www.amazon.com/Razer-Basilisk-Customizable-Wireless-Gaming/dp/B0B6Y3XYFG/ref=sr_1_1_sspa?keywords=gaming+mouse&pd_rd_r=9106c6ca-1c4d-43f1-91fd-233bb0d25f77&pd_rd_w=zeZgG&pd_rd_wg=7e2CU&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=SN3023ASAAZKVZJB9XYB&qid=1678362865&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRDA5STFKMElXTVhLJmVuY3J5cHRlZElkPUEwOTE2MjYxMVZZVDdQOTM0VTFZMCZlbmNyeXB0ZWRBZElkPUEwMDcxMjMzMlY4U0o2SENMVlFNRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
keepa_url = 'https://keepa.com/#!product/1-B0B6Y3XYFG'

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # page.wait_for_timeout(5000)
    page.goto(amazon_url)
    
    price_amazon = page.locator('//div[@id="corePrice_feature_div"]//span[@class="a-offscreen"]').inner_text().strip()
    print(price_amazon)
    
    # page.wait_for_timeout(5000)
    page.goto(keepa_url)
    price_keepa = page.locator('//span[@class="productTableDescriptionPrice priceAmazon"]//span').inner_text().strip()
    print(price_keepa)
    
    page.wait_for_timeout(5000)
        
    browser.close()