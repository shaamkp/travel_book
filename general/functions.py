import requests
import pandas as pd


def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        # message += "%s : %s | " %(key,error_message)
        message += f"{key} - {error_message} | "
    return message[:-3]


def downlaod_destination_csv(url):
    url = url
    response = requests.get(url)
    if response.status_code == 200:
        with open('destination_data.csv', 'wb') as f:
            f.write(response.content)
        print("CSV file downloaded successfully.")
    else:
        print("Failed to download CSV file:", response.status_code)
        print(response.json())


def downlaod_costumers_csv(url):
    url = url
    response = requests.get(url)
    if response.status_code == 200:
        with open('costumers_data.csv', 'wb') as f:
            f.write(response.content)
        print("CSV file downloaded successfully.")
    else:
        print("Failed to download CSV file:", response.status_code)
        print(response.json())


def downlaod_bookings_csv(url):
    url = url
    response = requests.get(url)
    if response.status_code == 200:
        with open('bookings_data.csv', 'wb') as f:
            f.write(response.content)
        print("CSV file downloaded successfully.")
    else:
        print("Failed to download CSV file:", response.status_code)
        print(response.json())

def cleanes_and_transform_data(file):
    try:
        data = pd.read_csv(file)
        date_formats = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d']
        for format in date_formats:
            try:
                data['booking_date'] = pd.to_datetime(data['booking_date'], format=format)
                break  
            except ValueError:
               pass
        data.dropna(inplace=True)
        data['total_booking_value'] = data['number_of_passenger'] * data['cost_per_passenger']
        data.to_csv("cleaned_booking_data.csv", index=False)
        print("CSV file cleaned successfully.")
    except Exception as e:
        print(str(e),"=-=-=-=-=-=-=-=-")


