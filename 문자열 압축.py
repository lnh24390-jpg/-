def compress_by_unit(text: str, unit: int) -> int:
    parts = []
    previous = text[:unit]
    count = 1

    for start in range(unit, len(text), unit):
        current = text[start:start + unit]

        if current == previous:
            count += 1
            continue

        parts.append(f"{count}{previous}" if count > 1 else previous)
        previous = current
        count = 1

    parts.append(f"{count}{previous}" if count > 1 else previous)
    return len("".join(parts))


def solution(s: str) -> int:
    if len(s) == 1:
        return 1

    min_length = len(s)

    for unit in range(1, len(s) // 2 + 1):
        min_length = min(min_length, compress_by_unit(s, unit))

    return min_length
