Here's a `README.md` file for your project. This file will help users understand how to set up and use your script.

```markdown
# Image Dataset Splitter

This project contains a Python script to organize a set of images into training, validation, and testing datasets. The images are categorized based on their filenames, and users can interactively select categories for each dataset.

## Features

- Automatically categorize images based on their filenames.
- Interactively select categories for training, validation, and testing datasets.
- Save the selected images' paths to separate text files for each dataset.

## Prerequisites

- Python 3.x
- An `images` directory containing your JPEG images.

## Getting Started

### Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Ensure you have an `images` directory**:
    Place all your JPEG images in an `images` directory within the project folder.

### Usage

Run the script using Python:
```sh
python main.py
```

Follow the interactive prompts to select categories for the training, validation, and testing datasets.

### Script Explanation

The script performs the following steps:

1. **Load and categorize images**:
    - Reads all `.jpg` files from the `images` directory.
    - Categorizes images based on the first three parts of their filenames separated by underscores.

2. **Interactively select categories**:
    - Prompts the user to input categories for the training, validation, and testing datasets.
    - Displays the remaining categories after each selection.

3. **Save the selections**:
    - Saves the paths of the selected images into `train.txt`, `val.txt`, and `test.txt`.

### Example

If your `images` directory contains the following files:
```
image1_cat_dog_001.jpg
image2_cat_dog_002.jpg
image3_bird_fish_001.jpg
image4_bird_fish_002.jpg
```

You can categorize them as follows:
- Training set: `cat_dog`
- Validation set: `bird_fish`
- Testing set: `cat_dog` or any other remaining categories

The script will generate three text files (`train.txt`, `val.txt`, `test.txt`) containing the paths to the selected images.

## File Structure

```
project-directory/
│
├── images/
│   ├── image1_cat_dog_001.jpg
│   ├── image2_cat_dog_002.jpg
│   ├── image3_bird_fish_001.jpg
│   └── image4_bird_fish_002.jpg
│
├── main.py
└── README.md
```

## Contributing

Feel free to open issues or submit pull requests with improvements or suggestions.
```

Make sure to replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name of your repository. Additionally, ensure you include the appropriate `LICENSE` file if your project has a specific license.
