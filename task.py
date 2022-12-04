import math
import psycopg2
import random
from bs4 import BeautifulSoup
from config import config


def extract_colors():
    with open("./python_class_question.html") as task_file:
        html_content = task_file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    td_tags = soup.find_all("td")
    td_color_tags = [td_tags[x] for x in range(1, len(td_tags), 2)]
    return td_color_tags


def process_colors(color_tags_list):
    color_list = []
    for tag in color_tags_list:
        color_list.extend(tag.get_text().strip().split(", "))
    return sorted(color_list)


def create_color_dictionary(color_list):
    color_dict = {}
    for color in color_list:
        if color in color_dict:
            color_dict[color] += 1
        else:
            color_dict[color] = 1
    return color_dict


#################################################################################################
################################# Task Solutions ################################################
#################################################################################################

# Solution to task 1
def get_mean_color(data, frequency_data):
    num_of_colors_types = len(frequency_data)
    total_num_of_colors = sum(frequency_data.values())
    mean_color_index = total_num_of_colors // num_of_colors_types
    mean_color = data[mean_color_index]
    return mean_color


# Solution to task 2
def get_mode_color(frequency_data):
    mode_frequency = max(frequency_data.values())
    mode_color = ""
    for color in frequency_data:
        if frequency_data[color] == mode_frequency:
            mode_color = color
    return mode_color


# Solution to task 3
def get_median_color(data):
    median_index = (len(data) + 1) // 2
    median_color = data[median_index]
    return median_color


# Solution to task 4
def get_variance(frequency_data):
    num_of_color_types = len(frequency_data)
    total_number_of_colors = sum(frequency_data.values())
    midpoint = total_number_of_colors / 2
    mean = total_number_of_colors / num_of_color_types
    print(mean)
    print(num_of_color_types)
    variance = (total_number_of_colors * math.pow(midpoint - mean, 2)) / num_of_color_types
    return variance


# Solution to task 5
def get_probability(frequency_data, color):
    num_of_color = frequency_data[color.upper()]
    total_num_of_colors = sum(frequency_data.values())
    probability_of_color = num_of_color / total_num_of_colors
    return probability_of_color


# Solution to task 6
def save_color_data(frequency_data):
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS colors (
            _id INTEGER PRIMARY KEY,
            name VARCHAR ( 50 ) UNIQUE NOT NULL,
            frequency INTEGER NOT NULL
            );
            """
        )

        for id, color in enumerate(frequency_data, 1):
            color_name = color
            color_frequency = str(frequency_data[color])
            cur.execute(
                f"INSERT INTO colors(_id, name, frequency) VALUES('{id}', '{color_name}', '{color_frequency}');"
            )

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Solution to task 7
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Solution to task 8
def convert_to_decimal(binary_value):
    decimal_value = 0
    value_arr = list(binary_value)
    for i, value in enumerate(value_arr, 1):
        power = len(value_arr) - i
        decimal_value += int(value) * math.pow(2, power)
    return int(decimal_value)


def generate_random_binary_value(digits):
    binary_value = ""
    for i in range(digits):
        digit = random.randint(0, 1)
        binary_value += str(digit)
    return binary_value


def task_eight_solution(num_of_digits):
    rand_binary_value = generate_random_binary_value(num_of_digits)
    rand_decimal_equivalent = convert_to_decimal(rand_binary_value)
    return rand_decimal_equivalent


# Solution to task 9
def fibonacci_sum(num):
    if num < 0:
        print("Invaid Value")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci_sum(num - 1) + fibonacci_sum(num - 2)


color_array = extract_colors()
color_data = process_colors(color_array)
color_frequency_data = create_color_dictionary(color_data)


# print(get_mean_color(color_data, color_frequency_data))
# print(get_mode_color(color_frequency_data))
# print(get_median_color(color_data))
# print(get_variance(color_frequency_data))
# print(get_probability(color_frequency_data, "red"))
# save_color_data(color_frequency_data)
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10, 6))
# print(task_eight_solution(4))
# print(fibonacci_sum(50))
