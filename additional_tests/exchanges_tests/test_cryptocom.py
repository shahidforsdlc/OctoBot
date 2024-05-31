#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import pytest

from additional_tests.exchanges_tests import abstract_authenticated_exchange_tester

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


class TestCryptoComAuthenticatedExchange(
    abstract_authenticated_exchange_tester.AbstractAuthenticatedExchangeTester
):
    # enter exchange name as a class variable here
    EXCHANGE_NAME = "cryptocom"
    EXCHANGE_TENTACLE_NAME = "CryptoCom"
    ORDER_CURRENCY = "BTC"
    SETTLEMENT_CURRENCY = "USDT"
    SYMBOL = f"{ORDER_CURRENCY}/{SETTLEMENT_CURRENCY}"
    ORDER_SIZE = 20  # % of portfolio to include in test orders
    VALID_ORDER_ID = "1777764898965454848"

    async def test_get_portfolio(self):
        await super().test_get_portfolio()

    async def test_get_portfolio_with_market_filter(self):
        # pass if not implemented
        pass

    async def test_get_account_id(self):
        # pass if not implemented
        pass

    async def test_get_api_key_permissions(self):
        # pass if not implemented
        pass

    async def test_missing_trading_api_key_permissions(self):
        pass

    async def test_get_not_found_order(self):
        await super().test_get_not_found_order()

    async def test_create_and_cancel_limit_orders(self):
        await super().test_create_and_cancel_limit_orders()

    async def test_create_and_fill_market_orders(self):
        await super().test_create_and_fill_market_orders()

    async def test_get_my_recent_trades(self):
        await super().test_get_my_recent_trades()

    async def test_get_closed_orders(self):
        await super().test_get_closed_orders()

    async def test_create_and_cancel_stop_orders(self):
        # pass if not implemented
        pass

    async def test_edit_limit_order(self):
        # pass if not implemented
        pass

    async def test_edit_stop_order(self):
        # pass if not implemented
        pass

    async def test_create_single_bundled_orders(self):
        # pass if not implemented
        pass

    async def test_create_double_bundled_orders(self):
        # pass if not implemented
        pass
