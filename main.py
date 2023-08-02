import json5
import argparse

# Creating ArgumentParser object
parser = argparse.ArgumentParser(description='Merge or remove properties from two JSON5 files.', prog='json5Plus')


# Add arguments to the parser
parser.add_argument('-action', type=str, help=' merge | remove')
parser.add_argument('-source', type=str, help='JSON5 file with the data to be merge')
parser.add_argument('-target', type=str, help='JSON5 file where the data is going to be place')


# Parse the command-line arguments
args = parser.parse_args()


# read json5 file
def load_file(_path):
    try:
        with open(_path) as _json5:
            return json5.load(_json5)
    except Exception as e:
        print(e)


# merge two files together
def merge_files(_input, _source):
    _obj1 = load_file(_input)
    _obj2 = load_file(_source)

    for key, value in _obj1.items():
        if key not in _obj2:
            _obj2[key] = value
    return _obj2


# remove keys from JSON5
def remove_files(_input, _source):
    _obj1 = load_file(_input)
    _obj2 = load_file(_source)

    for key, _ in _obj1.items():
        if key in _obj2:
            del _obj2[key]
    return _obj2


# write results to a json5 file
def write_file(_file, _content):
    with open(_file, 'w') as file:
        json5.dump(_content, file, indent=4, quote_keys=True)
    print(f"{args.action} completed")


# handling arguments
if (args.action == 'merge'):
    _result = merge_files(args.source, args.target)
    write_file(args.target, _result)

elif (args.action == 'remove'):
    _result = remove_files(args.source, args.target)
    write_file(args.target, _result)

else:
    print("run -h to get help")