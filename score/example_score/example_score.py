from iconservice import *

TAG = 'EXAMPLE_SCORE'

class BAND_PRICE_SCORE(InterfaceScore):
    @interface
    def get_price_info(self,symbol: str) -> dict:
        pass

class EXAMPLE_SCORE(IconScoreBase):
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.band_price_address = VarDB("band_price_address", db, value_type=Address)

        self.price = VarDB("price", db, value_type=int)
        self.multiplier = VarDB("multiplier", db, value_type=int)
        self.response_timestamp = VarDB(
            "response_timestamp", db, value_type=int)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def set_band_price_address(self, bridge_address: Address) -> None:
        self.band_price_address.set(bridge_address)

    @external(readonly=True)
    def get_band_price_address(self) -> Address:
        return self.band_price_address.get()

    @external(readonly=True)
    def get_price(self) -> int:
        return self.price.get()

    @external(readonly=True)
    def get_multiplier(self) -> int:
        return self.multiplier.get()

    @external(readonly=True)
    def get_response_timestamp(self) -> int:
        return self.response_timestamp.get()

    @external
    def read_from_price_db(self) -> None:
        expected_symbol = "ICX"

        price_db = self.create_interface_score(self.band_price_address.get(), BAND_PRICE_SCORE)
        res = price_db.get_price_info(expected_symbol)

        res_symbol = res["symbol"]
        res_price = res["price"]
        res_multiplier = res["multiplier"]
        res_latest_response_timestamp = res["latest_response_timestamp"]

        if res_symbol != expected_symbol:
            revert(f"result token symbol mismatch: expected {expected_symbol} but got {res_symbol}")

        self.price.set(res_price)
        self.multiplier.set(res_multiplier)
        self.response_timestamp.set(res_latest_response_timestamp)
