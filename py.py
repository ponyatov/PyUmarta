# piumarta object VM: see doc/

import ply.lex  as lex
import ply.yacc as yacc

pool = []

class Object:
	def __init__(self,V):
		self.tag = self.__class__.__name__ ; self.val = V
		self.attr = {} ; self.nest = []
		global pool ; pool += [self]
	def __repr__(self): return self.dump()
	def dump(self,depth=0): return self.head()
	def head(self,prefix=''): return '%s<%s:%s>'%(prefix,self.tag,self.val)

class Stack(Object): pass

S = Stack('DATA')

import os,sys

SRC = open(sys.argv[1]).read()
print SRC

tokens = ['SYM','SAVE','QQ','Q','DOT']

t_ignore = ' \t\r\n'
t_ignore_COMMENT = r'\#.*'

def t_QQ(t):
	r'\?\?'
	return t

def t_Q(t):
	r'\?'
	return t

def t_SAVE(t):
	r'\.save'
	return t

def t_DOT(t):
	r'\.'
	return t

def t_SYM(t):
	r'[a-zA-Z0-9_]+'
	return t

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

def p_REPL_none(p):
	r'REPL : '
def p_REPL(p):
	r'REPL : REPL SYM'
	Object(p[2])

def p_SAVE(p):
	r'REPL : REPL SAVE SYM'
	import pickle
	pickle.dump(pool,open(p[3],'w'))

def p_QQ(p):
	r'REPL : REPL QQ'
	print S ; print pool

def p_Q(p):
	r'REPL : REPL Q'
	print S

def p_DOT(p):
	r'REPL : REPL DOT'
	S.flush()

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=None,write_tables=False)

parser.parse(SRC)

