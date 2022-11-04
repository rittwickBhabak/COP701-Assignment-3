import tkinter


def text_count(widget, index1, index2, *options):
    """Hack Text count command. Return integer, or tuple if len(options) > 1.

    Tkinter does not provide a wrapper for the Tk Text widget count command
    at Python 2.7.1

    widget is a Tkinter Text widget.
    index1 and index2 are Indicies as specified in TkCmd documentation.
    options must be a tuple of zero or more option values.  If no options
    are given the Tk default option is used.  If less than two options are
    given an integer is returned.  Otherwise a tuple of integers is returned
    (in the order specified in TkCmd documentation).

    See text manual page in TkCmd documentation for valid option values and
    index specification.

    Example:
    chars, lines = text_count(widget, start, end, '-chars', '-lines')

    """
    return widget.tk.call((widget._w, 'count') + options + (index1, index2))


text = tkinter.Text()

print(text.count("1.0", tkinter.END))                                       # (1,0)
print(text.count("1.0", "1.0"))                                                 # None
print(text_count(text, "1.0", "1.0"))                                        # 0
print(text_count(text, "1.0", tkinter.END))                              # 1
print(text.count("1.0", tkinter.END, "chars"))                         # (1,)
print(text.count("1.0", "1.0", "chars"))                                   # None
print(text_count(text, "1.0", "1.0", "-chars"))                         # 0
print(text_count(text, "1.0", tkinter.END, "-chars"))               # 1
print(text.count(tkinter.END, "1.0", "chars"))                         # (-1,)
print(text_count(text, tkinter.END, "1.0", "-chars"))               # -1
print(text.count("1.0", tkinter.END, "chars", "lines"))             # (1, 1)
print(text.count("1.0", "1.0", "chars", "lines"))                       # (0, 0)
print(text_count(text, "1.0", "1.0", "-chars", "-lines"))            # (0, 0)
print(text_count(text, "1.0", tkinter.END, "-chars", "-lines"))  # (1, 1)