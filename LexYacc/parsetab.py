
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COLON COMMA CONTAINS DOT EQUAL FILENAME FOR GREATEREQUAL GREATERTHAN IN INVERTEDCOMMA JSONLINES LBRACKET LCBRACKET LESSEQUAL LESSTHAN LPAREN NAME NOTEQUAL NUMBER RBRACKET RCBRACKET RETURN RPAREN STRING VARIABLE WHEREquery : forclauses whereclause returnclausequery : forclauses returnclauseforclauses : forclauses forclauseforclauses : forclauseforclause : FOR exprswhereclause : WHERE wexprswexprs : wexprs AND wexprwexprs : wexprwexpr : VARIABLE DOT pathexpr condition VARIABLE DOT pathexprwexpr : VARIABLE condition VARIABLE DOT pathexprwexpr : VARIABLE condition VARIABLEwexpr : VARIABLE DOT pathexpr condition STRINGwexpr : VARIABLE condition STRINGwexpr : VARIABLE DOT pathexpr condition NUMBERwexpr : VARIABLE condition NUMBERwexpr : CONTAINS LPAREN VARIABLE DOT pathexpr COMMA STRING RPARENwexpr : CONTAINS LPAREN VARIABLE COMMA STRING RPARENcondition : EQUALcondition : NOTEQUALcondition : GREATEREQUALcondition : GREATERTHANcondition : LESSEQUALcondition : LESSTHANexprs : exprs COMMA exprexprs : exprexpr : VARIABLE IN JSONLINES LPAREN INVERTEDCOMMA FILENAME INVERTEDCOMMA RPAREN DOT pathexprexpr : VARIABLE IN JSONLINES LPAREN INVERTEDCOMMA FILENAME INVERTEDCOMMA RPARENexpr : rexprpathexpr : pathexpr DOT steppathexpr : stepstep : NAME LBRACKET selector RBRACKETstep : NAMEselector : selector : NUMBERreturnclause : RETURN rexprrexpr : VARIABLE DOT pathexprrexpr : VARIABLErexpr : LCBRACKET jsoncontents RCBRACKETjsoncontents : jsoncontents COMMA jsoncontentjsoncontents : jsoncontentjsoncontent : STRING COLON rexpr'
    
_lr_action_items = {'FOR':([0,2,3,7,10,11,12,13,38,40,41,42,43,62,72,79,82,],[4,4,-4,-3,-5,-25,-37,-28,-24,-36,-30,-32,-38,-29,-31,-27,-26,]),'$end':([1,6,15,20,21,40,41,42,43,62,72,],[0,-2,-1,-35,-37,-36,-30,-32,-38,-29,-31,]),'WHERE':([2,3,7,10,11,12,13,38,40,41,42,43,62,72,79,82,],[8,-4,-3,-5,-25,-37,-28,-24,-36,-30,-32,-38,-29,-31,-27,-26,]),'RETURN':([2,3,5,7,10,11,12,13,16,17,38,40,41,42,43,46,48,49,50,62,66,67,68,72,75,77,79,80,82,],[9,-4,9,-3,-5,-25,-37,-28,-6,-8,-24,-36,-30,-32,-38,-7,-11,-13,-15,-29,-12,-14,-10,-31,-17,-9,-27,-16,-26,]),'VARIABLE':([4,8,9,22,28,30,31,32,33,34,35,36,37,45,57,],[12,18,21,12,18,48,-18,-19,-20,-21,-22,-23,51,21,65,]),'LCBRACKET':([4,9,22,45,],[14,14,14,14,]),'CONTAINS':([8,28,],[19,19,]),'COMMA':([10,11,12,13,21,25,26,38,40,41,42,43,51,55,56,62,69,72,79,82,],[22,-25,-37,-28,-37,44,-40,-24,-36,-30,-32,-38,60,-39,-41,-29,74,-31,-27,-26,]),'IN':([12,],[23,]),'DOT':([12,18,21,40,41,42,47,48,51,62,65,68,69,72,77,79,82,],[24,29,24,53,-30,-32,53,58,59,-29,73,53,53,-31,53,81,53,]),'STRING':([14,30,31,32,33,34,35,36,44,57,60,74,],[27,49,-18,-19,-20,-21,-22,-23,27,66,70,78,]),'AND':([16,17,41,42,46,48,49,50,62,66,67,68,72,75,77,80,],[28,-8,-30,-32,-7,-11,-13,-15,-29,-12,-14,-10,-31,-17,-9,-16,]),'EQUAL':([18,41,42,47,62,72,],[31,-30,-32,31,-29,-31,]),'NOTEQUAL':([18,41,42,47,62,72,],[32,-30,-32,32,-29,-31,]),'GREATEREQUAL':([18,41,42,47,62,72,],[33,-30,-32,33,-29,-31,]),'GREATERTHAN':([18,41,42,47,62,72,],[34,-30,-32,34,-29,-31,]),'LESSEQUAL':([18,41,42,47,62,72,],[35,-30,-32,35,-29,-31,]),'LESSTHAN':([18,41,42,47,62,72,],[36,-30,-32,36,-29,-31,]),'LPAREN':([19,39,],[37,52,]),'RCBRACKET':([21,25,26,40,41,42,43,55,56,62,72,],[-37,43,-40,-36,-30,-32,-38,-39,-41,-29,-31,]),'JSONLINES':([23,],[39,]),'NAME':([24,29,53,58,59,73,81,],[42,42,42,42,42,42,42,]),'COLON':([27,],[45,]),'NUMBER':([30,31,32,33,34,35,36,54,57,],[50,-18,-19,-20,-21,-22,-23,64,67,]),'LBRACKET':([42,],[54,]),'INVERTEDCOMMA':([52,71,],[61,76,]),'RBRACKET':([54,63,64,],[-33,72,-34,]),'FILENAME':([61,],[71,]),'RPAREN':([70,76,78,],[75,79,80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,],[1,]),'forclauses':([0,],[2,]),'forclause':([0,2,],[3,7,]),'whereclause':([2,],[5,]),'returnclause':([2,5,],[6,15,]),'exprs':([4,],[10,]),'expr':([4,22,],[11,38,]),'rexpr':([4,9,22,45,],[13,20,13,56,]),'wexprs':([8,],[16,]),'wexpr':([8,28,],[17,46,]),'jsoncontents':([14,],[25,]),'jsoncontent':([14,44,],[26,55,]),'condition':([18,47,],[30,57,]),'pathexpr':([24,29,58,59,73,81,],[40,47,68,69,77,82,]),'step':([24,29,53,58,59,73,81,],[41,41,62,41,41,41,41,]),'selector':([54,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> forclauses whereclause returnclause','query',3,'p_query_1','MProjectParser.py',6),
  ('query -> forclauses returnclause','query',2,'p_query_2','MProjectParser.py',10),
  ('forclauses -> forclauses forclause','forclauses',2,'p_forclauses_1','MProjectParser.py',16),
  ('forclauses -> forclause','forclauses',1,'p_forclauses_2','MProjectParser.py',20),
  ('forclause -> FOR exprs','forclause',2,'p_forclause','MProjectParser.py',24),
  ('whereclause -> WHERE wexprs','whereclause',2,'p_whereclause_1','MProjectParser.py',29),
  ('wexprs -> wexprs AND wexpr','wexprs',3,'p_wexprs_1','MProjectParser.py',33),
  ('wexprs -> wexpr','wexprs',1,'p_wexprs_2','MProjectParser.py',37),
  ('wexpr -> VARIABLE DOT pathexpr condition VARIABLE DOT pathexpr','wexpr',7,'p_wexpr_1','MProjectParser.py',42),
  ('wexpr -> VARIABLE condition VARIABLE DOT pathexpr','wexpr',5,'p_wexpr_2','MProjectParser.py',46),
  ('wexpr -> VARIABLE condition VARIABLE','wexpr',3,'p_wexpr_3','MProjectParser.py',50),
  ('wexpr -> VARIABLE DOT pathexpr condition STRING','wexpr',5,'p_wexpr_4','MProjectParser.py',54),
  ('wexpr -> VARIABLE condition STRING','wexpr',3,'p_wexpr_5','MProjectParser.py',58),
  ('wexpr -> VARIABLE DOT pathexpr condition NUMBER','wexpr',5,'p_wexpr_6','MProjectParser.py',62),
  ('wexpr -> VARIABLE condition NUMBER','wexpr',3,'p_wexpr_7','MProjectParser.py',66),
  ('wexpr -> CONTAINS LPAREN VARIABLE DOT pathexpr COMMA STRING RPAREN','wexpr',8,'p_wexpr_8','MProjectParser.py',70),
  ('wexpr -> CONTAINS LPAREN VARIABLE COMMA STRING RPAREN','wexpr',6,'p_wexpr_9','MProjectParser.py',74),
  ('condition -> EQUAL','condition',1,'p_condition_1','MProjectParser.py',79),
  ('condition -> NOTEQUAL','condition',1,'p_condition_2','MProjectParser.py',83),
  ('condition -> GREATEREQUAL','condition',1,'p_condition_3','MProjectParser.py',87),
  ('condition -> GREATERTHAN','condition',1,'p_condition_4','MProjectParser.py',91),
  ('condition -> LESSEQUAL','condition',1,'p_condition_5','MProjectParser.py',95),
  ('condition -> LESSTHAN','condition',1,'p_condition_6','MProjectParser.py',99),
  ('exprs -> exprs COMMA expr','exprs',3,'p_exprs_1','MProjectParser.py',105),
  ('exprs -> expr','exprs',1,'p_exprs_2','MProjectParser.py',110),
  ('expr -> VARIABLE IN JSONLINES LPAREN INVERTEDCOMMA FILENAME INVERTEDCOMMA RPAREN DOT pathexpr','expr',10,'p_expr_1','MProjectParser.py',115),
  ('expr -> VARIABLE IN JSONLINES LPAREN INVERTEDCOMMA FILENAME INVERTEDCOMMA RPAREN','expr',8,'p_expr_2','MProjectParser.py',120),
  ('expr -> rexpr','expr',1,'p_expr_3','MProjectParser.py',125),
  ('pathexpr -> pathexpr DOT step','pathexpr',3,'p_pathexpr_1','MProjectParser.py',131),
  ('pathexpr -> step','pathexpr',1,'p_pathexpr_2','MProjectParser.py',136),
  ('step -> NAME LBRACKET selector RBRACKET','step',4,'p_step_1','MProjectParser.py',141),
  ('step -> NAME','step',1,'p_step_2','MProjectParser.py',146),
  ('selector -> <empty>','selector',0,'p_selector_2','MProjectParser.py',152),
  ('selector -> NUMBER','selector',1,'p_selector_1','MProjectParser.py',157),
  ('returnclause -> RETURN rexpr','returnclause',2,'p_returnclause_1','MProjectParser.py',163),
  ('rexpr -> VARIABLE DOT pathexpr','rexpr',3,'p_rexpr_1','MProjectParser.py',168),
  ('rexpr -> VARIABLE','rexpr',1,'p_rexpr_2','MProjectParser.py',173),
  ('rexpr -> LCBRACKET jsoncontents RCBRACKET','rexpr',3,'p_rexpr_3','MProjectParser.py',178),
  ('jsoncontents -> jsoncontents COMMA jsoncontent','jsoncontents',3,'p_jsoncontents_1','MProjectParser.py',183),
  ('jsoncontents -> jsoncontent','jsoncontents',1,'p_jsoncontents_2','MProjectParser.py',188),
  ('jsoncontent -> STRING COLON rexpr','jsoncontent',3,'p_jsoncontent','MProjectParser.py',193),
]
