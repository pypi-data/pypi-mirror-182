# pygmentize -l ./lexer.py:SqlLexer -x test.sql

import re
from pygments.lexers.sql import SqlLexer
from pygments.lexer import inherit, bygroups
from pygments.token import Name, Keyword, Whitespace

class BaldrSqlLexer(SqlLexer):
    name = 'SQL for Baldr project'

    aliases = ['baldrsql']

    flags = re.DOTALL

    # def get_tables(lexer, match):
    #     print(match)
    #     table = match.group(0).split(',')
    #     print(table)
    #     for t in table:
    #         table_match = re.match(r'\s*(\w+)(\s+AS\s+(\w+)\s*)?', t)
    #         yield 0, Name.Class, table_match.group(1)
    #         print(table_match)
    #         if table_match.group(3):
    #                 yield 323, Name.Class, table_match.group(3)



    tokens = {
        'root': [
            (r'[a-z_][\w]*(?=\.[a-z_][\w]*)', Name.Class),
            (r'(?<=\w\.)[a-z_][\w]*', Name.Attribute),
            (r'(\w+)(\s+)(AS)(\s+)(\w+)', bygroups(Name.Class, Whitespace, Keyword, Whitespace,  Name.Class)),
            # (r'(?<=FROM).*?(?=(WHERE|ORDER BY|$))', get_tables),
            inherit,
        ],
        # 'tablelist': [
        #     (r'(\w)( AS (\w))?,?', bygroups(Name.Class, Text, Name.Class))
        # ]
    }
