import csv

def write_output(results, filename, fields, delimiter, append=False):
    mode = "a" if append else "w"
    with open(filename, mode, newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter)
        if not append:
            writer.writeheader()
        for row in results:
            filtered_row = {field: row.get(field, "") for field in fields}
            writer.writerow(filtered_row)
