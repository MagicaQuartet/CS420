
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'sourceID NUMBER LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET LGREATER RGREATER PLUS INCREMENT MINUS STAR DIVIDE SEMICOLON STRING COMMA ASSIGN EQUAL NOTEQUAL RGREQUAL LGREQUAL IF FOR RETURN INT FLOAT VOIDsource : declarefuncdeclarefunc : func declarefuncdeclarefunc : funcfunc : INT ID LPAREN paramlist RPAREN LBRACE stmtlist RBRACE\n            | FLOAT ID LPAREN paramlist RPAREN LBRACE stmtlist RBRACE\n            | INT ID LPAREN RPAREN LBRACE stmtlist RBRACE\n            | FLOAT ID LPAREN RPAREN LBRACE stmtlist RBRACEparamlist : param COMMA paramlistparamlist : paramparam : VOID\n             | INT ID\n             | FLOAT ID\n             | INT STAR ID\n             | FLOAT STAR IDstmtlist : stmt stmtliststmtlist : stmtstmt : return SEMICOLON\n            | declarevar SEMICOLON\n            | assignvar SEMICOLON\n            | forloop\n            | incre\n            | if\n            | funccall SEMICOLONreturn : RETURN\n              | RETURN arithexpforloop : FOR LPAREN id ASSIGN arithexp SEMICOLON id cmp arithexp SEMICOLON incre RPAREN LBRACE stmtlist RBRACEif : IF LPAREN arithexp cmp arithexp RPAREN LBRACE stmtlist RBRACEfunccall : ID LPAREN arglist RPAREN\n                | ID LPAREN RPARENarglist : arg COMMA arglistarglist : argarg : arithexp\n           | stringdeclarevar : INT varlist\n                  | FLOAT varlist\n                  | INT STAR varlist\n                  | FLOAT STAR varlistvarlist : id COMMA varlistvarlist : idassignvar : id ASSIGN arithexparithexp : LPAREN arithexp RPAREN\n                | term arithexptail\n                | termarithexptail : PLUS term arithexptail\n                    | PLUS term\n                    | MINUS term arithexptail\n                    | MINUS termterm : factor termtail\n            | factortermtail : STAR factor termtail\n                | STAR factor\n                | DIVIDE factor termtail\n                | DIVIDE factorfactor : NUMBER\n              | PLUS NUMBER\n              | MINUS NUMBERfactor : increincre : INCREMENT idincre : id INCREMENTfactor : id\n              | funccallid : ID\n          | ID LBRACKET arithexp RBRACKETcmp : LGREATER\n           | RGREATER\n           | EQUAL\n           | NOTEQUAL\n           | RGREQUAL\n           | LGREQUALstring : STRING'
    
_lr_action_items = {'INT':([0,3,9,10,22,23,27,29,33,37,38,39,49,55,58,60,61,62,63,78,80,83,84,107,111,135,139,144,146,],[4,4,11,11,30,11,30,30,30,-20,-21,-22,30,-62,-6,-17,-18,-19,-23,-59,-58,-7,-4,-5,-63,30,-27,30,-26,]),'FLOAT':([0,3,9,10,22,23,27,29,33,37,38,39,49,55,58,60,61,62,63,78,80,83,84,107,111,135,139,144,146,],[5,5,16,16,42,16,42,42,42,-20,-21,-22,42,-62,-6,-17,-18,-19,-23,-59,-58,-7,-4,-5,-63,42,-27,42,-26,]),'$end':([1,2,3,6,58,83,84,107,],[0,-1,-3,-2,-6,-7,-4,-5,]),'ID':([4,5,11,16,20,22,25,27,29,30,33,37,38,39,41,42,45,49,53,55,56,57,60,61,62,63,65,76,77,78,79,80,81,86,96,97,99,100,110,111,117,118,119,120,121,122,123,124,132,135,136,139,140,144,146,],[7,8,19,24,28,31,48,31,31,55,31,-20,-21,-22,74,55,55,31,55,-62,74,74,-17,-18,-19,-23,74,55,74,-59,55,-58,74,55,74,74,74,74,74,-63,74,74,-64,-65,-66,-67,-68,-69,55,31,74,-27,55,31,-26,]),'LPAREN':([7,8,31,41,44,46,56,57,65,74,77,81,110,117,118,119,120,121,122,123,124,136,],[9,10,56,65,79,81,65,65,65,56,65,65,65,65,65,-64,-65,-66,-67,-68,-69,65,]),'RPAREN':([9,10,12,14,15,17,19,24,28,47,48,55,56,66,67,68,71,72,73,74,78,80,87,88,89,90,91,92,94,95,98,101,102,109,111,112,113,114,115,116,125,126,127,128,129,131,142,],[13,18,21,-9,-10,26,-11,-12,-13,-8,-14,-62,88,-43,-49,-54,-57,-60,-61,-62,-59,-58,109,-29,-31,-32,-33,-70,112,-42,-48,-55,-56,-28,-63,-41,-45,-47,-51,-53,-30,-44,-46,-50,-52,133,143,]),'VOID':([9,10,23,],[15,15,15,]),'STAR':([11,16,30,42,55,67,68,71,72,73,74,78,80,88,101,102,109,111,115,116,],[20,25,53,76,-62,99,-54,-57,-60,-61,-62,-59,-58,-29,-55,-56,-28,-63,99,99,]),'LBRACE':([13,18,21,26,133,143,],[22,27,29,49,135,144,]),'COMMA':([14,15,19,24,28,48,54,55,66,67,68,71,72,73,74,78,80,88,89,90,91,92,95,98,101,102,109,111,112,113,114,115,116,126,127,128,129,],[23,-10,-11,-12,-13,-14,86,-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,110,-32,-33,-70,-42,-48,-55,-56,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,]),'RETURN':([22,27,29,33,37,38,39,49,55,60,61,62,63,78,80,111,135,139,144,146,],[41,41,41,41,-20,-21,-22,41,-62,-17,-18,-19,-23,-59,-58,-63,41,-27,41,-26,]),'FOR':([22,27,29,33,37,38,39,49,55,60,61,62,63,78,80,111,135,139,144,146,],[44,44,44,44,-20,-21,-22,44,-62,-17,-18,-19,-23,-59,-58,-63,44,-27,44,-26,]),'INCREMENT':([22,27,29,31,33,37,38,39,41,43,49,55,56,57,60,61,62,63,65,72,74,77,78,80,81,96,97,99,100,110,111,117,118,119,120,121,122,123,124,135,136,139,140,141,144,146,],[45,45,45,-62,45,-20,-21,-22,45,78,45,-62,45,45,-17,-18,-19,-23,45,78,-62,45,-59,-58,45,45,45,45,45,45,-63,45,45,-64,-65,-66,-67,-68,-69,45,45,-27,45,78,45,-26,]),'IF':([22,27,29,33,37,38,39,49,55,60,61,62,63,78,80,111,135,139,144,146,],[46,46,46,46,-20,-21,-22,46,-62,-17,-18,-19,-23,-59,-58,-63,46,-27,46,-26,]),'ASSIGN':([31,43,55,105,111,],[-62,77,-62,117,-63,]),'LBRACKET':([31,55,74,],[57,57,57,]),'RBRACE':([32,33,37,38,39,50,51,55,59,60,61,62,63,78,80,82,111,137,139,145,146,],[58,-16,-20,-21,-22,83,84,-62,-15,-17,-18,-19,-23,-59,-58,107,-63,139,-27,146,-26,]),'SEMICOLON':([34,35,36,40,41,52,54,55,64,66,67,68,71,72,73,74,75,78,80,85,88,95,98,101,102,103,104,108,109,111,112,113,114,115,116,126,127,128,129,130,138,],[60,61,62,63,-24,-34,-39,-62,-25,-43,-49,-54,-57,-60,-61,-62,-35,-59,-58,-36,-29,-42,-48,-55,-56,-37,-40,-38,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,132,140,]),'NUMBER':([41,56,57,65,69,70,77,81,96,97,99,100,110,117,118,119,120,121,122,123,124,136,],[68,68,68,68,101,102,68,68,68,68,68,68,68,68,68,-64,-65,-66,-67,-68,-69,68,]),'PLUS':([41,55,56,57,65,66,67,68,71,72,73,74,77,78,80,81,88,96,97,98,99,100,101,102,109,110,111,113,114,115,116,117,118,119,120,121,122,123,124,128,129,136,],[69,-62,69,69,69,96,-49,-54,-57,-60,-61,-62,69,-59,-58,69,-29,69,69,-48,69,69,-55,-56,-28,69,-63,96,96,-51,-53,69,69,-64,-65,-66,-67,-68,-69,-50,-52,69,]),'MINUS':([41,55,56,57,65,66,67,68,71,72,73,74,77,78,80,81,88,96,97,98,99,100,101,102,109,110,111,113,114,115,116,117,118,119,120,121,122,123,124,128,129,136,],[70,-62,70,70,70,97,-49,-54,-57,-60,-61,-62,70,-59,-58,70,-29,70,70,-48,70,70,-55,-56,-28,70,-63,97,97,-51,-53,70,70,-64,-65,-66,-67,-68,-69,-50,-52,70,]),'DIVIDE':([55,67,68,71,72,73,74,78,80,88,101,102,109,111,115,116,],[-62,100,-54,-57,-60,-61,-62,-59,-58,-29,-55,-56,-28,-63,100,100,]),'RBRACKET':([55,66,67,68,71,72,73,74,78,80,88,93,95,98,101,102,109,111,112,113,114,115,116,126,127,128,129,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,111,-42,-48,-55,-56,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,]),'LGREATER':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,119,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,119,]),'RGREATER':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,120,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,120,]),'EQUAL':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,121,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,121,]),'NOTEQUAL':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,122,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,122,]),'RGREQUAL':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,123,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,123,]),'LGREQUAL':([55,66,67,68,71,72,73,74,78,80,88,95,98,101,102,106,109,111,112,113,114,115,116,126,127,128,129,134,],[-62,-43,-49,-54,-57,-60,-61,-62,-59,-58,-29,-42,-48,-55,-56,124,-28,-63,-41,-45,-47,-51,-53,-44,-46,-50,-52,124,]),'STRING':([56,110,],[92,92,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'source':([0,],[1,]),'declarefunc':([0,3,],[2,6,]),'func':([0,3,],[3,3,]),'paramlist':([9,10,23,],[12,17,47,]),'param':([9,10,23,],[14,14,14,]),'stmtlist':([22,27,29,33,49,135,144,],[32,50,51,59,82,137,145,]),'stmt':([22,27,29,33,49,135,144,],[33,33,33,33,33,33,33,]),'return':([22,27,29,33,49,135,144,],[34,34,34,34,34,34,34,]),'declarevar':([22,27,29,33,49,135,144,],[35,35,35,35,35,35,35,]),'assignvar':([22,27,29,33,49,135,144,],[36,36,36,36,36,36,36,]),'forloop':([22,27,29,33,49,135,144,],[37,37,37,37,37,37,37,]),'incre':([22,27,29,33,41,49,56,57,65,77,81,96,97,99,100,110,117,118,135,136,140,144,],[38,38,38,38,71,38,71,71,71,71,71,71,71,71,71,71,71,71,38,71,142,38,]),'if':([22,27,29,33,49,135,144,],[39,39,39,39,39,39,39,]),'funccall':([22,27,29,33,41,49,56,57,65,77,81,96,97,99,100,110,117,118,135,136,144,],[40,40,40,40,73,40,73,73,73,73,73,73,73,73,73,73,73,73,40,73,40,]),'id':([22,27,29,30,33,41,42,45,49,53,56,57,65,76,77,79,81,86,96,97,99,100,110,117,118,132,135,136,140,144,],[43,43,43,54,43,72,54,80,43,54,72,72,72,54,72,105,72,54,72,72,72,72,72,72,72,134,43,72,141,43,]),'varlist':([30,42,53,76,86,],[52,75,85,103,108,]),'arithexp':([41,56,57,65,77,81,110,117,118,136,],[64,90,93,94,104,106,90,130,131,138,]),'term':([41,56,57,65,77,81,96,97,110,117,118,136,],[66,66,66,66,66,66,113,114,66,66,66,66,]),'factor':([41,56,57,65,77,81,96,97,99,100,110,117,118,136,],[67,67,67,67,67,67,67,67,115,116,67,67,67,67,]),'arglist':([56,110,],[87,125,]),'arg':([56,110,],[89,89,]),'string':([56,110,],[91,91,]),'arithexptail':([66,113,114,],[95,126,127,]),'termtail':([67,115,116,],[98,128,129,]),'cmp':([106,134,],[118,136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> source","S'",1,None,None,None),
  ('source -> declarefunc','source',1,'p_source_declarefunc','myyacc.py',9),
  ('declarefunc -> func declarefunc','declarefunc',2,'p_declarefunc_list','myyacc.py',17),
  ('declarefunc -> func','declarefunc',1,'p_declarefunc_single','myyacc.py',22),
  ('func -> INT ID LPAREN paramlist RPAREN LBRACE stmtlist RBRACE','func',8,'p_func','myyacc.py',27),
  ('func -> FLOAT ID LPAREN paramlist RPAREN LBRACE stmtlist RBRACE','func',8,'p_func','myyacc.py',28),
  ('func -> INT ID LPAREN RPAREN LBRACE stmtlist RBRACE','func',7,'p_func','myyacc.py',29),
  ('func -> FLOAT ID LPAREN RPAREN LBRACE stmtlist RBRACE','func',7,'p_func','myyacc.py',30),
  ('paramlist -> param COMMA paramlist','paramlist',3,'p_paramlist_list','myyacc.py',38),
  ('paramlist -> param','paramlist',1,'p_paramlist_single','myyacc.py',46),
  ('param -> VOID','param',1,'p_param','myyacc.py',51),
  ('param -> INT ID','param',2,'p_param','myyacc.py',52),
  ('param -> FLOAT ID','param',2,'p_param','myyacc.py',53),
  ('param -> INT STAR ID','param',3,'p_param','myyacc.py',54),
  ('param -> FLOAT STAR ID','param',3,'p_param','myyacc.py',55),
  ('stmtlist -> stmt stmtlist','stmtlist',2,'p_stmtlist_list','myyacc.py',70),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist_single','myyacc.py',75),
  ('stmt -> return SEMICOLON','stmt',2,'p_stmt','myyacc.py',80),
  ('stmt -> declarevar SEMICOLON','stmt',2,'p_stmt','myyacc.py',81),
  ('stmt -> assignvar SEMICOLON','stmt',2,'p_stmt','myyacc.py',82),
  ('stmt -> forloop','stmt',1,'p_stmt','myyacc.py',83),
  ('stmt -> incre','stmt',1,'p_stmt','myyacc.py',84),
  ('stmt -> if','stmt',1,'p_stmt','myyacc.py',85),
  ('stmt -> funccall SEMICOLON','stmt',2,'p_stmt','myyacc.py',86),
  ('return -> RETURN','return',1,'p_return','myyacc.py',91),
  ('return -> RETURN arithexp','return',2,'p_return','myyacc.py',92),
  ('forloop -> FOR LPAREN id ASSIGN arithexp SEMICOLON id cmp arithexp SEMICOLON incre RPAREN LBRACE stmtlist RBRACE','forloop',15,'p_forloop','myyacc.py',100),
  ('if -> IF LPAREN arithexp cmp arithexp RPAREN LBRACE stmtlist RBRACE','if',9,'p_if','myyacc.py',105),
  ('funccall -> ID LPAREN arglist RPAREN','funccall',4,'p_funccall','myyacc.py',110),
  ('funccall -> ID LPAREN RPAREN','funccall',3,'p_funccall','myyacc.py',111),
  ('arglist -> arg COMMA arglist','arglist',3,'p_arglist_list','myyacc.py',119),
  ('arglist -> arg','arglist',1,'p_arglist_single','myyacc.py',124),
  ('arg -> arithexp','arg',1,'p_arg','myyacc.py',129),
  ('arg -> string','arg',1,'p_arg','myyacc.py',130),
  ('declarevar -> INT varlist','declarevar',2,'p_declarevar','myyacc.py',138),
  ('declarevar -> FLOAT varlist','declarevar',2,'p_declarevar','myyacc.py',139),
  ('declarevar -> INT STAR varlist','declarevar',3,'p_declarevar','myyacc.py',140),
  ('declarevar -> FLOAT STAR varlist','declarevar',3,'p_declarevar','myyacc.py',141),
  ('varlist -> id COMMA varlist','varlist',3,'p_varlist_list_id','myyacc.py',149),
  ('varlist -> id','varlist',1,'p_varlist_single_id','myyacc.py',154),
  ('assignvar -> id ASSIGN arithexp','assignvar',3,'p_assignvar','myyacc.py',158),
  ('arithexp -> LPAREN arithexp RPAREN','arithexp',3,'p_arithexp','myyacc.py',166),
  ('arithexp -> term arithexptail','arithexp',2,'p_arithexp','myyacc.py',167),
  ('arithexp -> term','arithexp',1,'p_arithexp','myyacc.py',168),
  ('arithexptail -> PLUS term arithexptail','arithexptail',3,'p_arithexptail','myyacc.py',178),
  ('arithexptail -> PLUS term','arithexptail',2,'p_arithexptail','myyacc.py',179),
  ('arithexptail -> MINUS term arithexptail','arithexptail',3,'p_arithexptail','myyacc.py',180),
  ('arithexptail -> MINUS term','arithexptail',2,'p_arithexptail','myyacc.py',181),
  ('term -> factor termtail','term',2,'p_term','myyacc.py',189),
  ('term -> factor','term',1,'p_term','myyacc.py',190),
  ('termtail -> STAR factor termtail','termtail',3,'p_termtail','myyacc.py',199),
  ('termtail -> STAR factor','termtail',2,'p_termtail','myyacc.py',200),
  ('termtail -> DIVIDE factor termtail','termtail',3,'p_termtail','myyacc.py',201),
  ('termtail -> DIVIDE factor','termtail',2,'p_termtail','myyacc.py',202),
  ('factor -> NUMBER','factor',1,'p_factor_num','myyacc.py',209),
  ('factor -> PLUS NUMBER','factor',2,'p_factor_num','myyacc.py',210),
  ('factor -> MINUS NUMBER','factor',2,'p_factor_num','myyacc.py',211),
  ('factor -> incre','factor',1,'p_factor_incre','myyacc.py',220),
  ('incre -> INCREMENT id','incre',2,'p_incre_prefix','myyacc.py',225),
  ('incre -> id INCREMENT','incre',2,'p_incre_postfix','myyacc.py',230),
  ('factor -> id','factor',1,'p_factor_notnum','myyacc.py',235),
  ('factor -> funccall','factor',1,'p_factor_notnum','myyacc.py',236),
  ('id -> ID','id',1,'p_id','myyacc.py',241),
  ('id -> ID LBRACKET arithexp RBRACKET','id',4,'p_id','myyacc.py',242),
  ('cmp -> LGREATER','cmp',1,'p_cmp','myyacc.py',253),
  ('cmp -> RGREATER','cmp',1,'p_cmp','myyacc.py',254),
  ('cmp -> EQUAL','cmp',1,'p_cmp','myyacc.py',255),
  ('cmp -> NOTEQUAL','cmp',1,'p_cmp','myyacc.py',256),
  ('cmp -> RGREQUAL','cmp',1,'p_cmp','myyacc.py',257),
  ('cmp -> LGREQUAL','cmp',1,'p_cmp','myyacc.py',258),
  ('string -> STRING','string',1,'p_string','myyacc.py',263),
]