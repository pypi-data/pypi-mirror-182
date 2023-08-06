import argparse
from .. import Mahlzeit

parser = argparse.ArgumentParser(description="Interact with the data in ledger.py")
group = parser.add_mutually_exclusive_group()
group.add_argument('--ledger', action='store_true', help='Print (h)ledger compatible journal (requires all transactions to be properly annotated according to the mahlzeit python package).')

def main(args):
    if args.get_email:
        email = emailmap.get(args.get_email)
        if email is None:
            print(args.get_email, "was not found", file=sys.stderr)
            sys.exit(1)
        if isinstance(email, list) or isinstance(email, tuple):
            print(*email)
        else:
            print(email)
    elif args.emails or args.all_emails:
        for name, value in m.calc().items():
            email = emailmap.get(name)
            if email == None:
                print("Warning:", name, "is not present in emailmap", file=sys.stderr)
                continue
            if args.all_emails or not iszero(value):
                if isinstance(email, list) or isinstance(email, tuple):
                    for e in email:
                        print(e)
                else:
                    print(email)
    elif args.names or args.all_names:
        for name, value in m.calc().items():
            if args.all_names or not iszero(value):
                print(name)
    elif args.ledger:
        m.journal()
    else:
        m.pretty()


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
