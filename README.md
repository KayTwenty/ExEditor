<p align="center">
  <a href="https://google.com">
    <img src="./src/images/exe.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">ExEditor</h1>
  <p align="center">
  <img src="https://img.shields.io/github/last-commit/KayTwenty/ExEditor?style=for-the-badge" alt="Commit"/>
  <img src="https://img.shields.io/github/license/KayTwenty/ExEditor?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/python-3.7+-blue?style=for-the-badge" alt="Python"/>
  <img src="https://img.shields.io/badge/code%20style-black-black?style=for-the-badge" alt="Black" />
  </p>
  <p align="center">
    A IDE that tries to give the user the best working environment
    <br />
    <a href="">Explore Website</a>
    ·
    <a href="https://github.com/KayTwenty/ExEditor/releases/download/0.5/ExEditor.zip">Download ExEditor</a>
  </p>
</p>

# Preview Screenshots
<p align="left">
  <img src="./src/images/preview.png" alt="Preview" width="700" height="400">
  <img src="./src/images/preview2.png" alt="Preview2" width="700" height="400">
</p>

# Installation
This project requires **Pygments** as well as **PyYAML**. Both of these packages can be installed through a virtual environment with **requirements.txt**.

**Mac and Linux installation:**

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

```sh
pip3 install -r requirements.txt
```

**Windows:**

```sh
python -m venv env
```

```
env\Scripts\activate.bat
```
```
pip install -r requirements.txt
```


# Keyboard Shortcuts
ExEditor has shortcuts for most commonly performed actions. The list of all the shortcuts is presented bellow:

| Command | KeyBinding | Description |
| ------- | ---------- | ----------- |
| Copy | <kbd>ctrl</kbd>+<kbd>c</kbd> | Copy selected text |
| Cut | <kbd>ctrl</kbd>+<kbd>x</kbd> | Cut selected text |
| Paste | <kbd>ctrl</kbd>+<kbd>v</kbd> | Paste text from the clipboard |
| Bold | <kbd>ctrl</kbd>+<kbd>b</kbd> | Bold selected text |
| Find and Replace | <kbd>ctrl</kbd>+<kbd>f</kbd> | Find and replace specified text |
| Highlight | <kbd>ctrl</kbd>+<kbd>g</kbg> | Highlight selected text |
| New File | <kbd>ctrl</kbd>+<kbd>n</kbd> | Open a new empty file |
| Open File | <kbd>ctrl</kbd>+<kbd>o</kbd> | Open an existing file |
| Run File | <kbd>ctrl</kbd>+<kbd>r</kbd> | Run the currently active file (Doesn't work) |
| Save | <kbd>ctrl</kbd>+<kbd>s</kbd> | Save the currently active file |
| Save As | <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>s</kbd> | Save the currently active file under a different name |
