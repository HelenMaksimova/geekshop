from django import template


def price_format(value):
    number_parts = str(value).split('.')
    main_part = list(number_parts[0])
    rest_part = '00' if len(number_parts) < 2 else number_parts[1]
    for idx in range(len(main_part), -1, -3):
        main_part.insert(idx, ' ')
    result = '.'.join((''.join(main_part).strip(), rest_part))
    return result


register = template.Library()

register.filter('price_format', price_format)
