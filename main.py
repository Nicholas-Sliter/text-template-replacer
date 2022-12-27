# Text template variable replacement
# Path: main.py

import json

VARIABLES = r'''{
    "${VARIABLE1}": "value1",
    "${VARIABLE2}": "value2"
}'''

TEMPLATE = r'''{sometexthere}'''

vars = json.loads('{VARIABLES}')
template = json.loads('{TEMPLATE}')


def main():
    for key, value in vars.items():
        template = template.replace(key, value)

    if '${' in template:
        index = template.find('${')
        print(f'Error: variable not found: {template[index:index + 10]}')
        exit(1)

    print(template)


if __name__ == '__main__':
    main()
