from src.lexer import Lexer
from src.parser import Parser
from src.parser.error_handler import ErrorSrc as parErrorSrc
from src.analyzer import MemberAnalyzer, TypeChecker
from src.analyzer.error_handler import ErrorSrc
from .compiler import Compiler

if __name__ == "__main__":
    sc = """
    cwass Hololive(a-chan) [[
        fwunc sum-chan(one-chan, two-chan) [[
            b-chan=1~
            iwf (one == 1) [[
                pwint(1)~
                iwf (two == 2) [[
                    b=b*2~
                    pwint(2)~
                    iwf (one == 1) [[
                        pwint(1)~
                    ]]
                ]]
            ]] ewse iwf (two == 2) [[
                i-chan = 1~
                do whiwe (i < 10) [[
                    pwint(i, "inside")~
                    i = i + 1~
                ]]
                pwint(2)~
            ]] ewse [[
                fow (i-chan=1~ i < 10~ i + 1) [[
                    pwint(i)~
                ]]
                pwint(b)~
            ]]
            wetuwn(one + two)~
        ]]
    ]]
    cwass Hololive2(a-chan) [[
        b-chan~
        fwunc sum-chan(one-chan, two-chan) [[
            b=1~
            iwf (one == 1) [[
                pwint(1)~
                iwf (two == 2) [[
                    b=b*2~
                    pwint(2)~
                    iwf (one == 1) [[
                        pwint(1)~
                    ]]
                ]]
            ]] ewse iwf (two == 2) [[
                i-chan = 1~
                do whiwe (i < 10) [[
                    pwint(i, "inside")~
                    i = i + 1~
                ]]
                pwint(2)~
            ]] ewse [[
                fow (i-chan=1~ i < 10~ i + 1) [[
                    pwint(i)~
                ]]
                pwint(b)~
            ]]
            wetuwn(one + two)~
        ]]
    ]]
    fwunc mainuwu-san() [[
        array-chan[] = {1,2,3}~
        string-senpai = "hello" & "world" & "!"~
        s-senpai = inpwt("input 1: ") & inpwt("input 2: ")~
        stringfmt-senpai = "hello | array | world" & "i am a concat in fmt"~
        pwint(array, string, s, stringfmt)~
        wetuwn(nuww)~
    ]]
    fwunc sum-chan(one-chan, two-chan) [[
        one = 1+1*1-1/1%1>1<1>=1<=1||1&&1~
        two = 2~
        wetuwn(one + two)~
    ]]
    """
    source: list[str] = [line if line else '\n' for line in sc.split("\n")]
    max_digit_length = len(str(len(source)))
    max_width = max(len(line) for line in source) + max_digit_length + 3
    print('\nsample text file')
    print("-"*max_width)
    for i, line in enumerate(source):
        line = line if line != '\n' else ''
        print(f"{i+1} | {line}")
    print("-"*max_width)
    print('end of file\n')

    l = Lexer(source)
    if l.errors:
        for err in l.errors:
            print(err)
        exit(1)
    parErrorSrc.src = source
    p = Parser(l.tokens)
    if p.errors:
        for err in p.errors:
            print(err)
        exit(1)

    ErrorSrc.src = source
    ma = MemberAnalyzer(p.program)
    if ma.errors:
        for err in ma.errors:
            print(err)
        exit(1)
    assert p.program

    tc = TypeChecker(p.program)
    if tc.errors:
        for err in tc.errors:
            print(err)
        exit(1)

    c = Compiler(p.program.python_string())
