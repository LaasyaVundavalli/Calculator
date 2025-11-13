"""
UI module for the Algorithm Calculator.

This module contains the Tkinter UI components.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from algorithms.sorting import SORTING_ALGORITHMS
from algorithms.searching import SEARCHING_ALGORITHMS


class AlgorithmCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Calculator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Apply theme
        style = ttk.Style()
        style.theme_use('clam')  # or 'azure' if available

        # Configure styles
        style.configure('TButton', font=('Arial', 12))
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="Algorithm Calculator", font=('Arial', 20, 'bold'))
        title_label.pack(pady=10)

        # Sorting section
        sorting_label = ttk.Label(main_frame, text="Sorting Algorithms", font=('Arial', 16))
        sorting_label.pack(pady=5)

        sorting_frame = ttk.Frame(main_frame)
        sorting_frame.pack(pady=5)

        sorting_buttons = [
            "Bubble Sort", "Selection Sort", "Insertion Sort",
            "Quick Sort", "Merge Sort", "Heap Sort"
        ]

        for i, algo in enumerate(sorting_buttons):
            btn = ttk.Button(sorting_frame, text=algo, command=lambda a=algo: self.open_sort_window(a))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')

        # Searching section
        searching_label = ttk.Label(main_frame, text="Searching Algorithms", font=('Arial', 16))
        searching_label.pack(pady=5)

        searching_frame = ttk.Frame(main_frame)
        searching_frame.pack(pady=5)

        searching_buttons = ["Binary Search"]

        for i, algo in enumerate(searching_buttons):
            btn = ttk.Button(searching_frame, text=algo, command=lambda a=algo: self.open_search_window(a))
            btn.grid(row=0, column=i, padx=5, pady=5, sticky='ew')

    def open_sort_window(self, algorithm):
        sort_window = tk.Toplevel(self.root)
        sort_window.title(f"{algorithm} Calculator")
        sort_window.geometry("600x500")
        sort_window.resizable(False, False)

        # Frame
        frame = ttk.Frame(sort_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(frame, text=algorithm, font=('Arial', 18, 'bold'))
        title_label.pack(pady=10)

        # Input label
        input_label = ttk.Label(frame, text="Enter space-separated integers:")
        input_label.pack(pady=5)

        # Input entry
        input_entry = ttk.Entry(frame, width=50)
        input_entry.pack(pady=5)

        # Submit button
        submit_btn = ttk.Button(frame, text="Sort", command=lambda: self.perform_sort(algorithm, input_entry.get(), result_text, steps_text, complexity_label, sort_window))
        submit_btn.pack(pady=10)

        # Result label
        result_label = ttk.Label(frame, text="Sorted Array:")
        result_label.pack(pady=5)

        # Result text
        result_text = tk.Text(frame, height=2, width=50, font=('Arial', 12))
        result_text.pack(pady=5)

        # Steps label
        steps_label = ttk.Label(frame, text="Steps:")
        steps_label.pack(pady=5)

        # Steps text
        steps_text = tk.Text(frame, height=10, width=50, font=('Arial', 10))
        steps_text.pack(pady=5)

        # Time complexity
        complexity_label = ttk.Label(frame, text="", font=('Arial', 12, 'italic'))
        complexity_label.pack(pady=5)

        # Close button
        close_btn = ttk.Button(frame, text="Close", command=sort_window.destroy)
        close_btn.pack(pady=10)

    def open_search_window(self, algorithm):
        search_window = tk.Toplevel(self.root)
        search_window.title(f"{algorithm} Calculator")
        search_window.geometry("600x500")
        search_window.resizable(False, False)

        # Frame
        frame = ttk.Frame(search_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(frame, text=algorithm, font=('Arial', 18, 'bold'))
        title_label.pack(pady=10)

        # Array input
        array_label = ttk.Label(frame, text="Enter sorted space-separated integers:")
        array_label.pack(pady=5)

        array_entry = ttk.Entry(frame, width=50)
        array_entry.pack(pady=5)

        # Target input
        target_label = ttk.Label(frame, text="Enter target integer:")
        target_label.pack(pady=5)

        target_entry = ttk.Entry(frame, width=50)
        target_entry.pack(pady=5)

        # Submit button
        submit_btn = ttk.Button(frame, text="Search", command=lambda: self.perform_search(algorithm, array_entry.get(), target_entry.get(), result_text, steps_text, complexity_label, search_window))
        submit_btn.pack(pady=10)

        # Result label
        result_label = ttk.Label(frame, text="Result:")
        result_label.pack(pady=5)

        # Result text
        result_text = tk.Text(frame, height=2, width=50, font=('Arial', 12))
        result_text.pack(pady=5)

        # Steps label
        steps_label = ttk.Label(frame, text="Steps:")
        steps_label.pack(pady=5)

        # Steps text
        steps_text = tk.Text(frame, height=10, width=50, font=('Arial', 10))
        steps_text.pack(pady=5)

        # Time complexity
        complexity_label = ttk.Label(frame, text="", font=('Arial', 12, 'italic'))
        complexity_label.pack(pady=5)

        # Close button
        close_btn = ttk.Button(frame, text="Close", command=search_window.destroy)
        close_btn.pack(pady=10)

    def perform_sort(self, algorithm, input_str, result_text, steps_text, complexity_label, window):
        try:
            # Validate input
            arr = list(map(int, input_str.split()))
            if not arr:
                raise ValueError("Input cannot be empty")

            # Perform sorting
            func = SORTING_ALGORITHMS[algorithm]
            sorted_arr, steps, complexity = func(arr)

            # Display results
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, ' '.join(map(str, sorted_arr)))

            steps_text.delete(1.0, tk.END)
            steps_text.insert(tk.END, '\n'.join(steps))

            complexity_label.config(text=f"Time Complexity: {complexity}")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {str(e)}. Please enter space-separated integers.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def perform_search(self, algorithm, array_str, target_str, result_text, steps_text, complexity_label, window):
        try:
            # Validate input
            arr = list(map(int, array_str.split()))
            if not arr:
                raise ValueError("Array cannot be empty")
            target = int(target_str)

            # Check if sorted
            if arr != sorted(arr):
                raise ValueError("Array must be sorted for binary search")

            # Perform search
            func = SEARCHING_ALGORITHMS[algorithm]
            index, steps, complexity = func(arr, target)

            # Display results
            result_text.delete(1.0, tk.END)
            if index != -1:
                result_text.insert(tk.END, f"Found at index {index}")
            else:
                result_text.insert(tk.END, "Not found")

            steps_text.delete(1.0, tk.END)
            steps_text.insert(tk.END, '\n'.join(steps))

            complexity_label.config(text=f"Time Complexity: {complexity}")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {str(e)}. Please enter space-separated integers for array and an integer for target.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmCalculator(root)
    root.mainloop()