# piumarta object VM: see doc/

import ply.lex  as lex
import ply.yacc as yacc

class MObject:
	def __init__(self,V): self.val = V
	def __repr__(self): return self.dump()
	def dump(self,depth=0): return self.head()
	def head(self,prefix=''): return '%s<%s>'%(prefix,self.val)

import os,sys

SRC = open(sys.argv[1]).read()
print SRC

tokens = ['SYM']

t_ignore = ' \t\r\n'
t_ignore_COMMENT = r'\#.*'

def t_SYM(t):
	r'[a-zA-Z0-9_]+'
	return t

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

def p_REPL_none(p):
	r'REPL : '

def p_REPL(p):
	r'REPL : REPL SYM'
	print MObject(p[2])

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=None,write_tables=False)

parser.parse(SRC)

