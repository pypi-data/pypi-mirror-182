import traceback
import argparse
from parser.parser import tparse, TagTransformer, Error
from visitor.interpreter import TagInterpreter

def _interactive(f, text: str):
    while True:
        try:
            i = input(text)
            if not i and i.isspace():
                continue
            f(i)
        except EOFError:
            return 0
        except Exception:
            continue
            #traceback.print_exception(e) # type: ignore

def _parse_text(arg):
    if arg.pretty:
        def _(t):
            o = tparse(t)
            if isinstance(o, Error):
                print(o)
            else:
                print(o.pretty())
        return _
    return lambda t: print(tparse(t))

def _debug_transformer(arg):
    def _(t):
        o = tparse(t)
        if isinstance(o, Error):
            print(o)
        else:
            print(TagTransformer().transform(o))
    return _

def repl(arg):
    def _(t):
        o = tparse(t)
        if isinstance(o, Error):
            return
        r = inter.start(TagTransformer().transform(o)[0])
        if inter.globalenv.error:
            for err in inter.globalenv.error:
                print(err)
            return
        if arg.debug:
            for n, v in inter.globalenv:
                print(f"{n} = {v}")
        if r:
            if r.type.NAME != 'NullType':
                if r.type.NAME == 'string':
                    print(r.repr().__repr__())
                else:
                    print(r)
    return _


argparser = argparse.ArgumentParser(
    prog="Tagger", description="Scripting language designed for discord bot tag command"
)

argparser.add_argument("--filename", help="script file path")
argparser.add_argument("--debug-parser", action='store_true', help="debug parser")
argparser.add_argument("--debug-transformer", action='store_true', help="debug transformer")
argparser.add_argument("--debug", action='store_true', help="debug interpreter")
argparser.add_argument("--pretty", action='store_true', help="output pretty output (must have debug parser flag activated)")

arg = argparser.parse_args()

inter = TagInterpreter()

prog = repl

if arg.debug_parser:
    prog = _parse_text
elif arg.debug_transformer:
    prog = _debug_transformer

if arg.filename:
    try:
        with open(arg.filename, 'r') as f:
            c = f.read()
        prog(arg)(c)
        exit(0)
    except PermissionError:
        print("no permission")
        exit(1)
    except FileNotFoundError:
        print("file not found")
        exit(1)
    except EOFError:
        exit(1)
    except Exception:
        exit(1)

exit(_interactive(prog(arg), ">>> "))