def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        if line.strip() == "":
            continue

        parts = [part.strip() for part in line.split(",")]

        if header is None:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        row = {}
        for i, column in enumerate(header):
            row[column] = parts[i]
        rows.append(row)

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row.get("тип")
        if kind is None:
            continue
        counts[kind] = counts.get(kind, 0) + 1

    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row.get("тип") != kind:
            continue

        value = row.get("минуты")
        if value is None:
            continue

        text = str(value).strip().replace(",", ".")

        try:
            total += float(text)
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts):
    lines = ["тип,количество"]

    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")

    return "\n".join(lines) + "\n"