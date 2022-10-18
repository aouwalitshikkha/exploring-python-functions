# dollar = 300
# exchange_rate = 100
# bdt = dollar * exchange_rate
# print(dollar, 'is equal to', bdt)
#
# # Samsung rate
# samsang_price = 200
# samsung_bdt = samsang_price * exchange_rate
# print(samsang_price, 'is equal to', samsung_bdt)
#
# # Xaiomi price
#
# xiaomi_price = 150
# xiaomi_bdt = xiaomi_price * exchange_rate
# print(xiaomi_price, 'is equal to', xiaomi_bdt)


# DRY = Don't repeat your self

def mobile_price_bdt(usd_price, exchange_rate):
    bdt_price = usd_price * exchange_rate
    return bdt_price


xiaomi_price = mobile_price_bdt(180, 101.92)
samsang_price = mobile_price_bdt(220, 103.52)
print(xiaomi_price)
print(samsang_price)
