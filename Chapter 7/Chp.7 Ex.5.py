"""
Chapter 7 Exercise 5 Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.
"""


def describe_city(city,
                  country='United Arab Emirates'):  # makes a function and has one parameter and another parameter with a default value

    print(
        f"{city.title()} is located in {country.title()}.\n")  # prints the city and the country with proper capitalization


describe_city('abu dhabi')  # calls the function and adds a value using positional arguments
describe_city(city='Sharjah',
              country='UAE')  # calls the function and replaces the values using keyword arguments
describe_city('dubai')  # calls the function and adds the value using positional arguments