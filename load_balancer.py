from collections import deque, defaultdict
import math

from prettytable import PrettyTable

from recipes import recipes


def determine_rates(desired_product, desired_rate):
    required_rates = defaultdict(float)
    required_rates[desired_product] = desired_rate

    products = deque([(desired_product, desired_rate)])

    while len(products) > 0:
        product, rate = products.popleft()
        recipe = recipes[product]
        recipes_required = rate / recipe['rate']

        for inp, inp_rate in recipe['inputs'].items():
            marginal_inp_rate = recipes_required * inp_rate
            required_rates[inp] += marginal_inp_rate
            if inp in recipes:
                products.append((inp, marginal_inp_rate))

    return required_rates


def determine_buildings(required_rates):
    required_buildings = []

    for product, rate, in required_rates.items():
        if product in recipes:
            recipe = recipes[product]
            min_buildings, clock_rate = underclock(recipe, rate)
            required_buildings.append((recipe['building'], product, clock_rate, min_buildings))

    return required_buildings


def underclock(recipe, required_rate):
    min_buildings = math.ceil(required_rate / recipe['rate'])
    clock_rate = required_rate / (recipe['rate'] * min_buildings)
    return min_buildings, clock_rate


def balance(desired_product, desired_rate):
    required_rates = determine_rates(desired_product, desired_rate)
    required_buildings = determine_buildings(required_rates)

    return required_rates, required_buildings


def print_balancing_spec(rates, buildings):
    rate_table = PrettyTable(field_names=['product', 'required_rate'])
    rate_table.add_rows(list(rates.items()))
    print(rate_table)

    building_table = PrettyTable(field_names=['building', 'product', 'clock rate', 'number'])
    building_table.add_rows(buildings)
    print(building_table)


product = 'supercomputer'
rate = 3.75

rates, buildings = balance(product, rate)

print_balancing_spec(rates, buildings)
