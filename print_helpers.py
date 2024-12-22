from typing import List


def table_print(data: List, column_width: int = 20) -> None:
    for column in data:
        print(str(column).ljust(column_width), end="\t")
    print()


def table_header_print(headers: List[str]) -> None:
    print("-------------------------------------------------------------------")
    table_print(headers)
    print("-------------------------------------------------------------------")


