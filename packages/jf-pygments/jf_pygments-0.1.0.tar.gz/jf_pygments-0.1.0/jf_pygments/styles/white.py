from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class WhiteStyle(Style):

    styles = {
        Whitespace:                "#FFFFFF",

        Comment:                   "#FFFFFF",
        Comment.Preproc:           "#FFFFFF",
        Comment.Special:           "bold #FFFFFF",

        Keyword:                   "bold #FFFFFF",
        Keyword.Pseudo:            "#FFFFFF",
        Keyword.Type:              "#FFFFFF",

        Operator:                  "#FFFFFF",
        Operator.Word:             "bold #FFFFFF",

        Name.Builtin:              "#FFFFFF",
        Name.Function:             "bold #FFFFFF",
        Name.Class:                "bold #FFFFFF",
        Name.Namespace:            "bold #FFFFFF",
        Name.Exception:            "bold #FFFFFF",
        Name.Variable:             "#FFFFFF",
        Name.Variable.Instance:    "#FFFFFF",
        Name.Variable.Class:       "#FFFFFF",
        Name.Variable.Global:      "bold #FFFFFF",
        Name.Constant:             "bold #FFFFFF",
        Name.Label:                "bold #FFFFFF",
        Name.Entity:               "bold #FFFFFF",
        Name.Attribute:            "#FFFFFF",
        Name.Tag:                  "#FFFFFF",
        Name.Decorator:            "bold #FFFFFF",

        String:                    "bg:#FFFFFF",
        String.Char:               "#FFFFFF bg:",
        String.Doc:                "#FFFFFF bg:",
        String.Interpol:           "bg:#FFFFFF",
        String.Escape:             "bold #FFFFFF",
        String.Regex:              "bg:#FFFFFF #FFFFFF",
        String.Symbol:             "#FFFFFF bg:",
        String.Other:              "#FFFFFF",

        Number:                    "bold #FFFFFF",
        Number.Integer:            "bold #FFFFFF",
        Number.Float:              "bold #FFFFFF",
        Number.Hex:                "bold #FFFFFF",
        Number.Oct:                "bold #FFFFFF",

        Generic.Heading:           "bold #FFFFFF",
        Generic.Subheading:        "bold #FFFFFF",
        Generic.Deleted:           "#FFFFFF",
        Generic.Inserted:          "#FFFFFF",
        Generic.Error:             "#FFFFFF",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #FFFFFF",
        Generic.Output:            "#FFFFFF",
        Generic.Traceback:         "#FFFFFF",

        Error:                     "#FFFFFF bg:#FFFFFF"
    }
