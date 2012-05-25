# Handlebars.js Template Tag
# Authored by:      Anthony Sutardja
# Last modified:    2012-05-24
#
# use {% load handlebars %} at the beginning of your template
# use {% handlebars %}
#           (Any fragment that contains Django templating {{ tag }})
#     {% endhandlebars %}

from django import template

register = template.Library()

@register.tag(name="handlebars")
def ignore(parser, token):
    """
    Ignores Django block and variable templating.
    
    The method walks through the tokens in the parser
    until 'endhandlebars' is reached. Text tokens and 
    variable tokens remain unchanged.
    """
    ret_str = ''
    # t is either a text, variable, block, or comment token
    for t in parser.tokens:
        if t.contents == 'endhandlebars':
            break
        elif t.token_type == template.TOKEN_TEXT:
            ret_str += t.contents
        elif t.token_type == template.TOKEN_VAR:
            #this is the syntax for Handlebars
            temporary_handle = '{{'+t.contents+'}}'
            ret_str += temporary_handle
        elif t.token_type == template.TOKEN_BLOCK:
            pass
    parser.skip_past('endhandlebars')
    return HandleNode(ret_str)

class HandleNode(template.Node):
    """Template Node object for allowing Handlebar exp."""
    def __init__(self, handle_string):
        """Initializes the string to be returned."""
        self.handle_string = handle_string
    def render(self, context):
        """Return the node rendered as a string."""
        return self.handle_string
