# top-up-3

A Selenium Python script to top up a pre-pay phone on Three Ireland.

Currently only works for cards _without_ Verified by Visa or the MasterCard equivalent.

Note that you need the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed. For macOS users the ~~best~~ _easiest_ way is via homebrew - `brew install chromedriver`.

## To Run

1. `git clone` and `cd` in
2. `virtualenv venv` to setup a sandboxed virtualenv
3. `. venv/bin/activate` to activate it
4. `pip install -r requirements.txt` to get Selenium installed
5. Copy `config-example.py` into `config.py` and fill it out with your details - see the "Caveats on `config.py`" section for some gotchas
6. `python app/app.py` (with optional phone number and top-up amount as arguments, e.g. `python app/app.py 0817777777 15.00`, to override the values in your `config.py` file), sit back and watch the magic happen

## Caveats on `config.py`

- The top-up amount can be any multiple of 5 from 10.00 to 30.00, and multiple of 10 from 30.00 to 50.00, but must be in the form `"xx.00"`
- All countries on Three's form are in English, e.g. Spain instead of España
- A postal code is not strictly necessary
- Valid card types are: `"Visa Credit"`, `"Visa Debit"`, `"Visa Electron"`, `"Master Card"` and `"Maestro"`

## To-do:

- Handle Verified by Visa and MasterCard equivalent
