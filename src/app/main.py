from dynaconf import settings

test = settings.TEST

from domain.filesystem import DirObj

test_dir_str: str = "."
test_dir: DirObj = DirObj(path=test_dir_str)


def main():
    print(f"Test var from Dynaconf ({type(test)}): {test}")

    print(
        f"Test directory [exists:{test_dir.exists}], Path ({type(test_dir.path)}): {type(test_dir.path)}"
    )


if __name__ == "__main__":
    main()
