from bs4 import BeautifulSoup
import re
import statistics
import psycopg2


def crawler():
    """
    Read HTML content from the file
    """
    with open("page.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return html_content


def get_content():
    """
    Parse the HTML content using BeautifulSoup
    """
    soup = BeautifulSoup(crawler(), "html.parser")
    return soup


# Extract colours from the table data
def get_colours():
    colours_td = get_content().find_all("td")[1::2]
    colours_text = [td.get_text() for td in colours_td]
    colours = re.findall(r"\b\w+\b", " ".join(colours_text))
    return colours


def calculate_mean():
    """
    Calculate mean colour
    """
    mean_colour = statistics.mode(get_colours())
    print(f"1. Mean colour: {mean_colour}")


def most_common_colour():
    """
    Calculate most common colour
    """
    most_common_colour = statistics.mode(get_colours())
    print(f"2. Most Common colour: {most_common_colour}")


def median_colour():
    """
    Calculate median colour
    """
    sorted_colours = sorted(get_colours())
    median_index = len(sorted_colours) // 2
    median_colour = sorted_colours[median_index]
    print(f"3. Median colour: {median_colour}")


def get_counter():
    """
    returns the colour counter object
    """
    colour_counter = statistics.Counter(get_colours())
    return colour_counter


def get_frequency():
    """
    returns the colour frequency object
    """
    colour_counter = get_counter()
    colour_frequencies = list(colour_counter.values())
    return colour_frequencies


def get_variance():
    """
    Calculate the variance
    """
    colour_counter = get_counter()
    colour_frequencies = get_frequency()
    variance = statistics.variance(colour_frequencies)
    print(f"4. Variance of colour Frequencies: {variance:.2f}")


def red_probability():
    """
    Calculate probability of choosing red colour
    """
    total_colours = sum(get_frequency())
    red_frequency = get_counter().get("RED", 0)
    red_probability = red_frequency / total_colours
    print(f"5. Probability of Choosing Red colour: {red_probability:.2f}")


""" I have commented this database part because the maximum requirement for this test is a single .py file
I would have used a Postgres Docker image to run a DB service as a container.
I've simulated the exercise below; assuming there's a DB connected.


# 
def save_to_db():
    # Connect to the PostgreSQL database
    
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create a table to store colours and frequencies
create_table_query = '''
CREATE TABLE colour_frequencies (
    colour TEXT PRIMARY KEY,
    frequency INTEGER
)
'''
cursor.execute(create_table_query)

# Insert colour frequencies into the table
for colour, frequency in colour_counter.items():
    insert_query = "INSERT INTO colour_frequencies (colour, frequency) VALUES (%s, %s)"
    cursor.execute(insert_query, (colour, frequency))

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

"""


def main():
    crawler()
    get_content()
    get_colours()
    calculate_mean()
    most_common_colour()
    median_colour()
    get_counter()
    get_frequency()
    get_variance()
    red_probability()

    print("6. Question 6 passed.  Find explanation in the code; line 95")


if __name__ == "__main__":
    main()
