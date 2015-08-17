__author__ = 'dbatalha'

from DuckGo import DuckGo


def main():

    data = DuckGo()
    data.get_duck_websites()

if __name__ == '__main__':
    main()