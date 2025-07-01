import argparse
from .project import add_user, show_users, update_user, delete_user

def cli_main():
    parser = argparse.ArgumentParser(description="CLI user-crud")
    subparsers = parser.add_subparsers(dest="command", required=True)

    
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--age", type=int, required=True)

    
    subparsers.add_parser("list")


    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--name")
    update_parser.add_argument("--age", type=int)

    
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    args = parser.parse_args()

    if args.command == "add":
        add_user(args.name, args.age)
    elif args.command == "list":
        show_users()
    elif args.command == "update":
        update_user(args.id, args.name, args.age)
    elif args.command == "delete":
        delete_user(args.id)

if __name__ == "__main__":
    cli_main()