# GUI-based Algorithm Calculator

A modern Python Tkinter application for demonstrating sorting and searching algorithms with step-by-step visualization.

## Overview

The Algorithm Calculator is a graphical user interface application that allows users to perform sorting and searching operations on integer arrays. It provides instant results with detailed step-by-step breakdowns, making it an excellent educational tool for students and faculty learning algorithms. The application features a clean, modern UI built with Tkinter and ttk widgets.

## Features

- **Sorting Algorithms**: Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort
- **Searching Algorithms**: Binary Search
- **Step-by-Step Visualization**: Detailed steps showing how each algorithm processes the data
- **Time Complexity Display**: Shows the time complexity for each algorithm
- **Input Validation**: Ensures only valid integer inputs are accepted
- **Error Handling**: Meaningful error messages for invalid inputs
- **Modern UI**: Clean, centered layout with increased font sizes and a modern theme

## Screenshots

### Main Window
![Main Window](screenshots/main_window.png)

### Sorting Window
![Sorting Window](screenshots/sorting_window.png)

### Searching Window
![Searching Window](screenshots/searching_window.png)

## How to Run

### Requirements
- Python 3.6 or higher
- Tkinter (usually included with Python installations)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/GUI-based-Algorithm-Calculator.git
   ```
2. Navigate to the project directory:
   ```
   cd GUI-based-Algorithm-Calculator
   ```
3. Run the application:
   ```
   python -m src.main
   ```
   Or from the src directory:
   ```
   cd src
   python main.py
   ```

## Project Structure

```
src/
├── algorithms/
│   ├── sorting.py      # Sorting algorithm implementations
│   └── searching.py    # Searching algorithm implementations
├── ui.py               # Tkinter UI components
└── main.py             # Application entry point
```

## Usage

1. Launch the application using `python src/main.py`
2. Choose a sorting or searching algorithm from the main window
3. Enter the required input (space-separated integers for arrays, integer for search target)
4. Click the appropriate button (Sort/Search)
5. View the results, steps, and time complexity in the output areas

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

