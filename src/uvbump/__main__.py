from ._core import uvbump, format_python_info


def main() -> None:
    print(format_python_info(uvbump()))


if __name__ == "__main__":
    main()
