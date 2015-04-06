# -*- coding: utf-8 -*-
"""
    pygments.styles.codeblocks
    ~~~~~~~~~~~~~~~~~~~~~~~

    The codeblocks highlighting style created by Leandro E. Colombo Viña.

    /usr/local/lib/python2.7/dist-packages/pygments/styles/codeblocks.py

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Whitespace, Punctuation


class CodeblocksStyle(Style):
    """
    The codeblocks style (inspired by Codeblocks).
    """

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
#        Comment:                   "italic #cccccc",
        Comment.Preproc:           "#00AA00",
        Comment.Multiline:         "italic #223344",
        Comment.Single:            "italic #666666",
        Comment.Special:           "#AA0000",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #000088",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "#000066",

        Operator:                  "#DD0000",
        Operator.Word:             "bold #AA22FF",

        Punctuation:               "#DD0000",

        Name.Builtin:              "#008000",
        Name.Function:             "#000000",
        Name.Class:                "bold #0000FF",
        Name.Namespace:            "bold #0000FF",
        Name.Exception:            "bold #D2413A",
        Name.Variable:             "#000000",
        Name.Constant:             "#880000",
        Name.Label:                "#A0A000",
        Name.Entity:               "bold #999999",
        Name.Attribute:            "#7D9029",
        Name.Tag:                  "bold #008000",
        Name.Decorator:            "#AA22FF",

        String:                    "#0000ff",
        String.Doc:                "italic",
        String.Interpol:           "bold #BB6688",
        String.Escape:             "bold #002276",
        String.Regex:              "#BB6688",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#FF00FF",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
