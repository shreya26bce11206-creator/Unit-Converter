# Unit Converter

## About the Project

Unit Converter is a simple Python project that I made to convert values
from one unit to another.

The project has different converters for common units like weight,
temperature, length, time, data and speed. The user can select a converter
from the menu and enter the required value.

I also added basic error handling and a conversion history feature so that
the program is easier to use.

## Features

- Weight Converter
- Temperature Converter
- Length Converter
- Time Converter
- Data Converter
- Speed Converter
- Conversion History
- Basic input validation
- Simple menu-based program

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## Project Structure

The project is divided into different Python files so that each converter
can be managed separately.

- `1 main.py`- Main menu of the project
- `weight.py` - Weight conversions
- `temperature.py` - Temperature conversions
- `length.py` - Length conversions
- `timeee.py` - Time conversions
- `storage.py` - Data conversions
- `speed.py` - Speed conversions
- `history.py` - Saves and displays conversion history
- `history.txt` - Stores conversion history
- `statement.md` - Project statement

## How to Run

1. Open the project folder in Visual Studio Code.
2. Make sure Python is installed.
3. Open `1 main.py`.
4. Run the program.
5. Select a converter from the menu.
6. Enter the value when asked.
7. The converted result will be displayed.

## Error Handling

The program checks some invalid inputs. For example, if a user enters
text instead of a number, the program shows an error message instead of
stopping suddenly.

## Conversion History

The project also has a history option. After performing a conversion,
the result can be saved and viewed later from the main menu.

## Testing

I tested the project with normal values as well as some invalid inputs.
The different converters were also checked separately to make sure that
the results were working correctly.

## Future Improvements

In the future, more units can be added to the project. The interface can
also be improved to make the project more interactive and easier to use.

## Conclusion

This project helped me understand how to use Python functions, conditions,
input handling and multiple files together to create a small working
application.