from .catalog import FURNITURE_CATALOG
from .rules import RULES

def rule_matches_order(rule, order):
    window_type = order.type.name
    width = order.width
    height = order.height

    if window_type in rule['window_type']:
        if not rule['conditions']:
            return True
        else:
            min_width = rule['conditions']['width']['min']
            max_width = rule['conditions']['width']['max']
            min_height = rule['conditions']['height']['min']
            max_height = rule['conditions']['height']['max']
            if min_width <= width <= max_width and min_height <= height <= max_height:
                return True

    return False

def get_components(rule, order):
    result = {}

    manufacturer = order.manufacturer.name
    system = order.system.name

    furniture = rule['components'][manufacturer]
    system_furniture = furniture.get(system)
    default_furniture = furniture.get('default')
    system_catalog_components = FURNITURE_CATALOG[manufacturer][system]
    default_catalog_components = FURNITURE_CATALOG[manufacturer]['default']

    for k, v in system_furniture.items():
        if system_catalog_components[k] not in result:
            result[system_catalog_components[k]] = v
        else:
            result[system_catalog_components[k]] += v

    for k, v in default_furniture.items():
        if default_catalog_components[k] not in result:
            result[default_catalog_components[k]] = v
        else:
            result[default_catalog_components[k]] += v


    return result

def result_components(rules, order):
    result = {}

    for rule in rules:
        components = get_components(rule, order)

        for k, v in components.items():
            if k.article not in result:
                result[k] = v
            else:
                result[k] += v

    return result

def engine(order):
    rules_result = []
    for r in RULES:
        result = rule_matches_order(r, order)
        if result:
            rules_result.append(r)

    furniture_result = result_components(rules_result, order)

    for k, v in furniture_result.items():
        furniture_result[k] = v * order.count

    return furniture_result

def price_calculate(furniture_result):
    total_price = 0
    for k, v in furniture_result.items():
        total_price += k.price * v

    return total_price

def storage_output(furniture_result):
    result = {}
    for k, v in furniture_result.items():
        result[k.article] = v

    return result
