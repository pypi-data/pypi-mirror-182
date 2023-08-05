import argparse
import sys
from . import sealedsecret


args_parser = argparse.ArgumentParser("sealedsecretmgr")

subparsers = args_parser.add_subparsers(help="sub-command help", dest="command")

create_parser = subparsers.add_parser(
    "create", help="Print a new SealedSecret resource as JSON"
)
create_parser.add_argument("name", type=str, help="Name of SelaedSecret to create")
create_parser.add_argument("key", type=str, help="Key contained by SealedSecret")
create_parser.add_argument(
    "value", type=str, help="Unencoded value associated with key"
)
create_parser.add_argument("--namespace", type=str, default="default")
create_parser.add_argument(
    "--merge-into",
    type=str,
    help="Path to existing SealedSecret to merge",
    required=False,
    default="",
)

update_parser = subparsers.add_parser(
    "update",
    help="Retrieve existing SealedSecret, add or edit a key, and print the resulting SealedSecret Resource as JSON",
)
update_parser.add_argument("name", type=str, help="Name of existing SealedSecret")
update_parser.add_argument(
    "key", type=str, help="Name of new or existing key contained in SealedSecret"
)
update_parser.add_argument(
    "value", type=str, help="Unencoded value associated with key"
)
update_parser.add_argument(
    "--namespace", type=str, default="default", help="Kubernetes namepsace"
)

get_parser = subparsers.add_parser(
    "get", help="Retrieve a SealedSecret and by name and print the SealedSecret as JSON"
)
get_parser.add_argument("name", type=str, help="Name of existing SealedSecret")
get_parser.add_argument(
    "--namespace", type=str, default="default", help="Kubernetes namepsace"
)

list_parser = subparsers.add_parser(
    "list", help="List all SealedSecretsand by name along with keys in it"
)
list_parser.add_argument(
    "--namespace", type=str, default="default", help="Kubernetes namepsace"
)


def __main__():
    args = args_parser.parse_args(sys.argv[1:])

    if args.command == "create":
        print(
            sealedsecret.create(
                args.name, args.key, args.value, args.namespace, args.merge_into
            )
        )
    elif args.command == "update":
        print(sealedsecret.update(args.name, args.key, args.value, args.namespace))
    elif args.command == "list":
        for (name, keys) in sealedsecret.list_names(args.namespace).items():
            print(name)
            for key in keys:
                print(f"\t{key}")
    elif args.command == "get":
        print(sealedsecret.get(args.name, args.namespace))
