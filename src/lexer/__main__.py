# Entry point for lexer package
from .lexer import *

if __name__ == "__main__":
    # temporary test source code
    source_code = [
        # r'pwint("hello \"hello\"")',
        # 'pwint("hello \|hello\|")',
        # '1bc ',
        'aqua-chan = func()---5',
        'fwunc aqua-Vtuber(shion-chan, 1, "string", fax, 2.50, ojou-Vtuber)',
        # '(1.0, 2.10, 3.)',
        # 'aqua-vtuber = vtuber()~',
        # 'aqua-Vtuber = Vtuber()~',
        # 'Vtuber.uwuwuwu()~',
        # 'vtuber.uwuwuwu()~',
        # 'channel-chan()~',
        # 'channel',
        # '"im an unterminated string"',
        # '>//< this',
        # 'is',
        # 'a',
        # 'multiline',
        # 'comment',
        # '>//<',
        # 'fwunc channel-chan()',
        # 'fwunc channel()',
        # 'fwunc channel-chan[()',
        # 'channel-chan()',
        # 'chan~',
        # 'chan',
        # 'channel',
        # '  21aqua-chan~',
        # 'aqua6-chan = "AKUA AISHITEEE!"~',
        # '"unclosed string',
        # '|what am I|a"~',
        # r'"hello |wo_rld| hello\|world"~ "hello\world|what|is this\|\|\|"~',
        # 'manji-senpai = "foo |aqua7 + shion| foo |ojou| boo"~',
        # '00010000000000000 + 5~',
        # '1.1.1~',
        # '1.111111111111110000000~',
        # '1111111111111111.1~',
        # '0.00~',
        # '1.~',
        # '8.00~',
        # '9.01~',
        # '6.0',
        # 'fwunc aqua-chan() ',
        # 'fwunc aqua() ',
        # 'fwunc aqua-chan ',
        # 'aqua-chan() ',
        # 'aqua()',
        # 'fwunc Shion-chan() ',
        # 'fwunc Shion() ',
        # 'fwunc Shion-chan ',
        # 'Shionchan ',
        # 'Shion()',
        # 'cwass Shion-chan() ',
        # 'cwass Shion() ',
        # 'cwass Shion-chan ',
        # 'Shion-chan() ',
        # 'Shion()',
        # 'cwass shion-chan() ',
        # 'cwass shion() ',
        # 'cwass shion-chan ',
        # 'shion-chan() ',
        # 'shion()',
        # 'bweak~',
        # ' aqua-chan',
        # 'cwass ',
        # 'aqua-chan = cap~',
        # 'cwass~ bweak',
        # 'dono ',
        # 'do whiwe(',
        # 'donee~',
        # 'ewse iwf(',
        # 'ewse(',
        # 'iwf(',
        # 'minato-chan~ojou~',
        # 'pwint (',
        # 'fax,',
        # 'fow',
        # 'gwobaw',
        # 'inpwt(',
        # 'float-kun = 10.5~',
        # 'mainuwu-',
        # 'nuww,',
        # 'san~',
        # 'sama ',
        # 'senpai~',
        # 'staart!',
        # 'whiwe (',
        # 'wetuwn(',
    ]
    print_lex(source_code)