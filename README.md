# creating_gif_with_python

## Description
`creating_gif_with_python` is a Python-based utility designed to [**Describe what the project does in a bit more detail, e.g., "simplify the process of generating animated GIFs from a sequence of static images."**]. It leverages powerful libraries like `imageio` and `pygifsicle` to create and optimize GIFs efficiently. This project is perfect for [**Who is this project for? e.g., "developers, content creators, or anyone looking to quickly create simple animations."**].

## Features

*   [**Feature 1: e.g., Generates animated GIFs from a series of input images (PNG, JPG, etc.).**]
*   [**Feature 2: e.g., Optimizes generated GIFs using Gifsicle for smaller file sizes.**]
*   [**Feature 3: e.g., Simple script-based execution.**]
*   [**Add more specific features if applicable.**]

## Installation Instructions

### Prerequisites
*   Python 3.x
*   pip (Python package installer)

### Setup
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/axellee1994/creating_gif_with_python.git](https://github.com/axellee1994/creating_gif_with_python.git)
    cd creating_gif_with_python
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    This project requires `imageio`, `pygifsicle`, and `Pillow`. Install them using the provided `requirements.txt` (you'll need to create this file).

    Create a file named `requirements.txt` in the project root with the following content:
    ```
    imageio
    pygifsicle
    Pillow
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, install directly (though `requirements.txt` is preferred):
    ```bash
    pip install imageio pygifsicle Pillow
    ```

## Usage Instructions

The core functionality is provided by the [create_gif.py](cci:7://file:///home/axlee/Desktop/codedex/creating_gif_with_python/create_gif.py:0:0-0:0) script.

**Prerequisites for Running:**
*   Ensure you have a folder named `srcs` in the same directory as the [create_gif.py](cci:7://file:///home/axlee/Desktop/codedex/creating_gif_with_python/create_gif.py:0:0-0:0) script.
*   Place your input image files (e.g., `nyan-cat1.png`, `nyan-cat2.png`, `nyan-cat3.png`) into the `srcs` folder. The script is currently hardcoded to use these specific file names and path.

**Running the Script:**
1.  Navigate to the project directory in your terminal.
2.  If you're using a virtual environment, ensure it's activated.
3.  Execute the script:
    ```bash
    python3 create_gif.py
    ```

**Expected Output:**
*   `nyan_cat.gif`: The initial animated GIF created from the images in the `srcs` folder.
*   `nyan_cat_optimized.gif`: An optimized version of `nyan_cat.gif`.
    Both files will be saved in the project's root directory.

**Note on Customization:**
Currently, the input image filenames, path (`srcs/`), output GIF names, and frame duration are hardcoded within the [create_gif.py](cci:7://file:///home/axlee/Desktop/codedex/creating_gif_with_python/create_gif.py:0:0-0:0) script. To use different images or settings, you will need to modify the script directly. Future improvements could include adding command-line arguments for greater flexibility.

## Contribution Guidelines
We welcome contributions to `creating_gif_with_python`! To contribute:
1.  Fork the repository.
2.  Create a feature branch: `git checkout -b feature/your-amazing-feature`
3.  Make your changes. Adhere to PEP 8 for Python code.
4.  Write clear and concise commit messages.
5.  Ensure your changes work as expected.
6.  Submit a pull request with a detailed description of your changes.

## License Information
This project is licensed under the **[Choose a License, e.g., MIT License]**.
Please create a `LICENSE` file in the root of the repository and add the full text of your chosen license. For example, if you choose MIT, you can find the template [here](https://opensource.org/licenses/MIT).

## Contact Information
For questions, suggestions, or issues, please contact:
*   **Author:** axellee1994 - [https://github.com/axellee1994](https://github.com/axellee1994)
*   **Project Link:** [https://github.com/axellee1994/creating_gif_with_python](https://github.com/axellee1994/creating_gif_with_python)
*   Feel free to open an issue on the GitHub repository for any bugs or feature requests.

---

Thank you for checking out `creating_gif_with_python`! If you find this project useful, please consider starring the repository.
