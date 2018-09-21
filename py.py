# piumarta object VM: see doc/

import ply.lex  as lex
import ply.yacc as yacc

class MObject:
	pass

import os,sys

SRC = open(sys.argv[1]).read()
print SRC

tokens = ['SYM']

def t_SYM(t):
	r'[a-zA-Z0-9_]+'
	return t

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

def p_REPL_none(p):
	r'REPL : '
	print p

def p_REPL(p):
	r'REPL : REPL SYM'
	print p

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=None,write_tables=False)

