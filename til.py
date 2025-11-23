#!/usr/bin/env python3
"""til-cli: A command-line TIL (Today I Learned) diary.

Track your daily learnings from the terminal. Entries are stored
locally in ~/.til/entries.json.

Usage:
    python til.py add "learned something" --tag python
    python til.py list --today
    python til.py search "python"
    python til.py delete 1
"""
import argparse
from src.commands import add_entry, list_entries, search_entries, delete_entry


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        Configured ArgumentParser with all subcommands.
    """
    parser = argparse.ArgumentParser(description="TIL - Today I Learned CLI")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # add
    add_parser = subparsers.add_parser("add", help="Añadir una nueva entrada")
    add_parser.add_argument("content", help="Contenido de la entrada")
    add_parser.add_argument("--tag", "-t", action="append", dest="tags", help="Etiqueta (puede repetirse)")

    # list
    list_parser = subparsers.add_parser("list", help="Listar entradas")
    list_parser.add_argument("--today", action="store_true", help="Solo entradas de hoy")
    list_parser.add_argument("--tag", "-t", help="Filtrar por etiqueta")

    # search
    search_parser = subparsers.add_parser("search", help="Buscar en las entradas")
    search_parser.add_argument("query", help="Texto a buscar")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Eliminar una entrada")
    delete_parser.add_argument("id", type=int, help="ID de la entrada a eliminar")

    return parser


def main():
    """Entry point for the TIL CLI application.

    Parses command-line arguments and executes the appropriate command.
    """
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        entry = add_entry(args.content, args.tags)
        print(f"Entrada #{entry.id} añadida")
    elif args.command == "list":
        entries = list_entries(filter_today=args.today, filter_tag=args.tag)
        if not entries:
            print("No hay entradas")
        else:
            for entry in entries:
                tags_str = f" [{', '.join(entry.tags)}]" if entry.tags else ""
                date_str = entry.created_at.strftime("%Y-%m-%d %H:%M")
                print(f"#{entry.id} ({date_str}){tags_str}")
                print(f"  {entry.content}")
                print()
    elif args.command == "search":
        entries = search_entries(args.query)
        if not entries:
            print(f"No se encontraron entradas con '{args.query}'")
        else:
            print(f"Encontradas {len(entries)} entradas:")
            for entry in entries:
                print(f"  #{entry.id}: {entry.content[:50]}...")
    elif args.command == "delete":
        if delete_entry(args.id):
            print(f"Entrada #{args.id} eliminada")
        else:
            print(f"No se encontró la entrada #{args.id}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
