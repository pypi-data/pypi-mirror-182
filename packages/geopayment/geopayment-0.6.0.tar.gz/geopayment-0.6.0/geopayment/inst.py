import time

from geopayment.providers import TBCInstallmentProvider


class MySmartTbcInstallmentProvider(TBCInstallmentProvider):
    @property
    def merchant_key(self):
        return "000000000-ce21da5e-da92-48f3-8009-4d438cbcc137"  # 'MerchantIntegrationTesting'

    @property
    def campaign_id(self):
        return "204"

    @property
    def key(self):
        return "ibO35FpiEs3NlXuAvv6L28niKRBfBoet"

    @property
    def secret(self):
        return "WStif1GSfGRK7dBM"

    @property
    def service_url(self) -> str:
        return "https://test-api.tbcbank.ge"

    @property
    def version(self) -> str:
        return "v1"


if __name__ == "__main__":
    tbc_installment = MySmartTbcInstallmentProvider()
    print(tbc_installment)
    a = tbc_installment.auth()
    print("aa: ", a)
    print(tbc_installment.auth)
    invoice_id = int(time.time())
    products = [{"name": "მაცივარი", "price": 150.33, "quantity": 1}]

    res = tbc_installment.create(products=products, invoice_id=invoice_id)
    print("sess: ", tbc_installment.session_id)
    print("rul: ", tbc_installment.redirect_url)
    print(res)
    ic = tbc_installment.confirm()
    print("Confirm: ", ic)
    st = tbc_installment.status()
    print("Status: ", st)
    sts = tbc_installment.statuses()
    print("STSTS: ", sts)
    # c = tbc_installment.cancel()
    # print('Cancel: ', c)
    # st = tbc_installment.status()
    # print('Status: ', st)
