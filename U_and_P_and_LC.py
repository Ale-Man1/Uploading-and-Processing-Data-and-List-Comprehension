import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/Ale-Man1/Uploading-and-Processing-Data-and-List-Comprehension/main/cars-sample35.csv')
    df.index += 1
    df.columns = ["Price", "Maintenance Cost", "Number of Doors", "Number of Passengers", "Luggage Capacity", "Safety Rating", "Classification of Vehicle"]
    pd.set_option('display.width', None)

    print(df)


if __name__ == '__main__':
    main()
