import math
from bs4 import BeautifulSoup


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


def get_mean_color(data, frequency_data):
    num_of_colors_types = len(frequency_data)
    total_num_of_colors = sum(frequency_data.values())
    mean_color_index = total_num_of_colors // num_of_colors_types
    mean_color = data[mean_color_index]
    return mean_color


def get_mode_color(frequency_data):
    mode_frequency = max(frequency_data.values())
    mode_color = ""
    for color in frequency_data:
        if frequency_data[color] == mode_frequency:
            mode_color = color
    return mode_color


def get_median_color(data):
    median_index = (len(data) + 1) // 2
    median_color = data[median_index]
    return median_color


def get_variance(frequency_data):
    num_of_color_types = len(frequency_data)
    total_number_of_colors = sum(frequency_data.values())
    midpoint = total_number_of_colors / 2
    mean = total_number_of_colors / num_of_color_types
    print(mean)
    print(num_of_color_types)
    variance = (total_number_of_colors * math.pow(midpoint - mean, 2)) / num_of_color_types
    return variance


def get_probability(frequency_data, color):
    num_of_color = frequency_data[color.upper()]
    total_num_of_colors = sum(frequency_data.values())
    probability_of_color = num_of_color / total_num_of_colors
    return probability_of_color


def save_color_data():
    pass

color_array = extract_colors()
color_data = process_colors(color_array)
color_frequency_data = create_color_dictionary(color_data)


# print(get_mean_color(color_data, color_frequency_data))
# print(get_mode_color(color_frequency_data))
# print(get_median_color(color_data))
# print(get_variance(color_frequency_data))
# print(get_probability(color_frequency_data, "red"))
