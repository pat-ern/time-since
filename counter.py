#!/usr/bin/env python3
import argparse
import csv
import os
from datetime import datetime, date

DATA_FILE = os.path.join(os.path.dirname(__file__), 'counters.txt')
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M'
DATE_FORMAT = '%Y-%m-%d'


def ensure_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['name', 'start_date', 'note'])


def parse_counters():
    ensure_data_file()
    counters = []
    with open(DATA_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f, delimiter='|')
        for row in reader:
            if not row.get('name'):
                continue
            counters.append({
                'name': row['name'].strip(),
                'start_date': row['start_date'].strip(),
                'note': row.get('note', '').strip(),
            })
    return counters


def save_counters(counters):
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(['name', 'start_date', 'note'])
        for item in counters:
            writer.writerow([item['name'], item['start_date'], item.get('note', '')])


def parse_start_datetime(start_date_str):
    for fmt in (DATE_TIME_FORMAT, DATE_FORMAT):
        try:
            return datetime.strptime(start_date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha inválido: {start_date_str}")


def format_elapsed(delta):
    total_seconds = int(delta.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    parts = []
    if days:
        parts.append(f"{days} días")
    if hours:
        parts.append(f"{hours} horas")
    if minutes:
        parts.append(f"{minutes} minutos")
    if not parts:
        parts.append("0 minutos")
    return ', '.join(parts)


def elapsed_since(start_date_str):
    try:
        start = parse_start_datetime(start_date_str)
        return datetime.now() - start
    except ValueError:
        return None


def add_counter(name, note):
    counters = parse_counters()
    existing = next((c for c in counters if c['name'].lower() == name.lower()), None)
    if existing:
        print(f"El contador '{name}' ya existe. Usa otro nombre o consulta el contador existente.")
        return
    new_counter = {
        'name': name,
        'start_date': datetime.now().strftime(DATE_TIME_FORMAT),
        'note': note or '',
    }
    counters.append(new_counter)
    save_counters(counters)
    print(f"Contador '{name}' creado con inicio {new_counter['start_date']}.")


def list_counters():
    counters = parse_counters()
    if not counters:
        print('No hay contadores todavía. Agrega uno con el comando "add".')
        return
    print('Contadores guardados:')
    for item in counters:
        elapsed = elapsed_since(item['start_date'])
        elapsed_text = format_elapsed(elapsed) if elapsed is not None else 'fecha inválida'
        note_text = f" - {item['note']}" if item['note'] else ''
        print(f"- {item['name']}: {elapsed_text} (inicio {item['start_date']}){note_text}")


def show_counter(name):
    counters = parse_counters()
    target = next((c for c in counters if c['name'].lower() == name.lower()), None)
    if not target:
        print(f"No se encontró ningún contador llamado '{name}'.")
        return
    elapsed = elapsed_since(target['start_date'])
    if elapsed is None:
        print(f"El contador '{name}' tiene una fecha de inicio inválida: {target['start_date']}")
        return
    print(f"Contador: {target['name']}")
    print(f"Inicio: {target['start_date']}")
    print(f"Tiempo transcurrido: {format_elapsed(elapsed)}")
    if target['note']:
        print(f"Nota: {target['note']}")


def delete_counter(name):
    counters = parse_counters()
    remaining = [c for c in counters if c['name'].lower() != name.lower()]
    if len(remaining) == len(counters):
        print(f"No se encontró ningún contador llamado '{name}'.")
        return

    respuesta = input(f"¿Estás seguro de que quieres eliminar el contador '{name}'? [s/N]: ")
    if respuesta.strip().lower() not in ('s', 'si', 'y', 'yes'):
        print('Eliminación cancelada.')
        return

    save_counters(remaining)
    print(f"Contador '{name}' eliminado.")


def build_parser():
    parser = argparse.ArgumentParser(
        description='Aplicación de terminal para contar días sin usar algo (persistencia local).'
    )
    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Crear un nuevo contador')
    parser_add.add_argument('name', help='Nombre del contador')
    parser_add.add_argument('-n', '--note', help='Nota opcional para el contador', default='')

    subparsers.add_parser('list', help='Mostrar todos los contadores')

    parser_show = subparsers.add_parser('show', help='Mostrar un contador por nombre')
    parser_show.add_argument('name', help='Nombre del contador a consultar')

    parser_delete = subparsers.add_parser('delete', help='Eliminar un contador por nombre')
    parser_delete.add_argument('name', help='Nombre del contador a eliminar')

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == 'add':
        add_counter(args.name, args.note)
    elif args.command == 'list':
        list_counters()
    elif args.command == 'show':
        show_counter(args.name)
    elif args.command == 'delete':
        delete_counter(args.name)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
