# json5Plus

### JSON5 Merge or Remove Properties

A Python script to merge or remove properties from two JSON5 files.

### Options

- `-h, --help`: Show the help message and exit.
- `-action ACTION`: Specify the action to perform: 'merge' to merge properties or 'remove' to remove properties.
- `-source SOURCE`: Path to the JSON5 file with the data to be merged.
- `-target TARGET`: Path to the JSON5 file where the data is going to be placed.

## Example

```sh
python main.py -action merge -source file.json5 -taget file2.json5
```

## Generate binary
In order to generate a binary for the target OS, you must install pyinstaller first by running the followig command.

```sh
pip install pyinstaller
```

Then you can run the bat file

```sh
create_binary.bat
```

## Requirements

- Python 3.5 or higher.
- `json5` library. Install it using the following command:

```sh
pip install json5
```
