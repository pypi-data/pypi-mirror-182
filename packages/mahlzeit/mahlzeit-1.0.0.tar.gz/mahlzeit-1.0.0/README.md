# Mahlzeit food accounting

You're buying groceries and cooking food for and share them with friends or colleagues.
Next time, a different colleague buys and cooks food. In between, a bank note changes hands.
Who owes how much money after a week's (or more) worth of buying, cooking and eating?

In order to track the balances of all participants, all transactions (purchases as well as cash
exchanging hands or bank accounts) need to be accounted using the `Mahlzeit` class and
`Mahlzeit.einkauf()` and `Mahlzeit.bezahlung()` methods.

For viewing the balances (and transaction), the following methods exist:

- As python dict via `Mahlzeit.calc()` with a simple mapping of the overall account balance:
  `[account]balance`
- Sorted and formatted directly on the console via `Mahlzeit.pretty(file=sys.stdout)`
- In a  [`ledger`-compatible format](https://hledger.org/hledger.html#journal-format) (which
  requires dates and descriptions to be set for each transaction) via
  `Mahlzeit.ledger(file=sys.stdout, prec=3)`

# API and usage

Transactions are grouped within a `Mahlzeit` object:

    from Mahlzeit import Mahlzeit
    m = Mahlzeit()

Each purchase is recorded as call to `Mahlzeit.einkauf(amount, eaters, payer, datum=None, description=None, comment=None)`:

    m.einkauf(10, ('Alice', 'Bob'), 'Alice')

`eaters` and `payer` may be a single string, tuple or list or strings or `Esser` objects.

Change in cash can be recorded with a call to `Mahlzeit.bezahlung(payer, payee, amount, datum=None, description=None, comment=None)`:

    m.bezahlung('Bob', 'Alice', 5)

If `ledger`-compatible output is desired, each transaction (`einkauf` and `bezahlung`) must be
annotated with a date and description:

    m.einkauf(10, ('Alice', 'Bob'), 'Alice', datum='2022/03/16', description='Kebap')
    m.bezahlung('Bob', 'Alice', 5, datum='2022/03/17', description='Payback')

Which can be used in a context to group several transactions within the same annotation:

    with m(datum='2022/03/16', description='Kebap'):
        m.einkauf(10, ('Alice', 'Bob'), 'Alice')
        m.bezahlung('Bob', 'Alice', 5)

Quick console output:

    m.pretty()

Or `ledger` output:

    m.journal()

to be interactively used as

    hledger -f <(python3 main.py) balance

We feature a convenience wrapper for "weighing" eaters. In some cases you need to weigh eaters
in case the is a couple at the weight of `2` or `0.5`. Instantiate a object of class
`Esser(name: str, weight: float)`:

    from mahlzeit import Mahlzeit, Esser as E
    m = Mahlzeit()
    m.einkauf(15, ('Laura', 'Nils', E('Katja_Martin', 2), 'Max'), 'Katja_Martin')
    m.pprint()

# Example integration into a personal ledger (ref. plaintextaccounting)

This example explains how to integrate the `--ledger` output of the Mahlzeit module into your
personal journal. It assumes that you're translating the Mahlzeit account for eating
`$you:einkauf:esser` to your personal expense account e.g. `expenses:food:work`. Account money
you spend for you and your colleagues as `liabilities:kollegen`.

```Makefile
.PHONY: auto-mahlzeit.journal

auto-mahlzeit.journal:
	hledger -f <(echo -e "= expenses:food:work\n    unused    *1\n    liabilities:kollegen  *-1\n"; MAHLZEIT_PLACES=2 venv/bin/python main.py --ledger) \
	--alias=meschenbacher:einkauf:esser=expenses:food:work \
	--alias=/meschenbacher:bezahlung:bezahlt*er/=unused \
	--alias=/meschenbacher:einkauf:bezahler/=unused \
	--alias=/.*:\(einkauf\|bezahlung\):.*/=unused \
	--begin 2022-04-09 \
	print --auto > $@
```

and include it into your journal via `include`.


# Installation

Via pip

    pip install mahlzeit
