# Dash Rotate

Dash Rotate is a Dash component library.
Components for smartphones that detect screen rotation.

### Installation
***

    $ pip install dash_alert


### Properties
***

- id (string)
- orientation (string)

    Correct orientation of the screen. Valid only if reload is true or if a message is specified.

- message (dash component)

    Message to be displayed in case of unintended screen orientation.

- reload (bool; default: true)

    Reloading on screen rotation?

- timing ("all" | "match"; default: "all")

    When to reload. "all": if the screen is rotated. "match": only if the screen is oriented correctly.

- delay (int; default: 10)

    The time from the time the screen is rotated until it is reloaded (milliseconds).