import fire
from cen.repo import Repo


def main():
    fire.Fire({
        'repo': Repo,
    })


if __name__ == '__main__':
    main()
