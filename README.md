# tdim - Show and help size terminal dimensions

A simple tool to help when I want to size any terminal "just so".

## Installation

`tdim` can be installed with either `pip`

```sh
$ pip install tdim
```

or ideally `pipx`:

```sh
$ pipx install tdim
```

## Usage

To run the tool, just run `tdim`. Once you run it up you'll see a simple
display of the dimensions of your terminal. Resize your terminal and be
amazed as the numbers change!

You can show/hide a border by pressing <kbd>b</kbd>.

To aim seeking a specific aspect ratio, a number of keys are set up for
common ones. When pressed the border will be shown, the width set to the
width of your terminal at that moment, and then height to the corresponding
target height for that ratio.

The keys are:

| Key          | Ratio              |
|--------------|--------------------|
| <kbd>0</kbd> | Clear target ratio |
| <kbd>1</kbd> | 16 x 9             |
| <kbd>2</kbd> | 4 x 3              |
| <kbd>3</kbd> | 2 x 1              |
| <kbd>4</kbd> | 1 x 1              |

To exit the application press <kbd>Esc</kbd>.

[//]: # (README.md ends here)
