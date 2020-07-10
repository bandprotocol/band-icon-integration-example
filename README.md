# Band Oracle ICON Developer Guide Example Score

This repository contains the source code for the example score found in ICON's developer guide on using Band's oracle price data.

## Usage

This example score contains two main functions: `set_band_price_address` and `read_from_price_db`. The configuration files for calling them is also included, being [`set_band_price_address.json`](./score/example_score/send_set_band_price_address.json) and [`send_read_from_db.json`](./score/example_score/send_read_from_db.json), respectively.

Before using the config files, please update its `from` field to match the account address you will be making the transaction from. More information on making transactions can be found on ICON's [developer documentation](https://www.icondev.io/docs/invoking-score-functions).
