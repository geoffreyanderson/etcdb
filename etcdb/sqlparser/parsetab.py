
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER STRING STRING_VALUE GREATER_OR_EQ LESS_OR_EQ N_EQ SELECT VERSION AUTO_INCREMENT CREATE DEFAULT FULL INTEGER KEY NULL PRIMARY SHOW TABLE TABLES VARCHAR NOT DATETIME DATABASE DATABASES USE INT FROM COMMIT WHERE OR AND IS SET AUTOCOMMIT LONGTEXT SMALLINT UNSIGNED BOOL TINYINT UNIQUE NAMES INSERT INTO VALUES DROP LIMIT AS UPDATE COUNT ORDER BY ASC DESC WAIT IF EXISTSstatement : select_statement\n        | show_tables_statement\n        | create_table_statement\n        | create_database_statement\n        | show_databases_statement\n        | use_database_statement\n        | commit_statement\n        | set_statement\n        | insert_statement\n        | drop_database_statement\n        | drop_table_statement\n        | desc_table_statement\n        | update_table_statement\n        | wait_statementwait_statement : WAIT \'(\' identifier \')\' FROM identifierupdate_table_statement : UPDATE identifier SET col_expr_list opt_WHERE col_expr_list : col_exprcol_expr_list : col_expr_list \',\' col_exprcol_expr :  identifier \'=\' exprdesc_table_statement : DESC identifierdrop_database_statement : DROP DATABASE identifierdrop_table_statement : DROP TABLE identifier opt_IF_EXISTSopt_IF_EXISTS : opt_IF_EXISTS : IF EXISTSinsert_statement : INSERT INTO identifier opt_fieldlist VALUES \'(\' values_list \')\'opt_fieldlist : opt_fieldlist : \'(\' fieldlist \')\'fieldlist : identifierfieldlist : fieldlist \',\' identifier  values_list : valuevalues_list : values_list \',\' valueset_statement : set_autocommit_statement\n        | set_names_statementset_names_statement : SET NAMES STRINGset_autocommit_statement : SET AUTOCOMMIT \'=\' NUMBERcommit_statement : COMMITcreate_table_statement : CREATE TABLE identifier \'(\' create_definition_list \')\'create_database_statement : CREATE DATABASE identifiershow_databases_statement : SHOW DATABASESuse_database_statement : USE identifieridentifier : STRINGidentifier : \'`\' STRING \'`\'create_definition_list : create_definition\n        | create_definition_list \',\' create_definitioncreate_definition : identifier column_definitioncolumn_definition : data_type opt_column_def_options_listdata_type : INTEGER opt_UNSIGNED\n        | VARCHAR \'(\' NUMBER \')\'\n        | DATETIME\n        | DATETIME \'(\' NUMBER \')\'\n        | INT opt_UNSIGNED\n        | LONGTEXT\n        | SMALLINT opt_UNSIGNED\n        | TINYINT\n        | BOOLopt_UNSIGNED :\n        | UNSIGNEDopt_column_def_options_list : opt_column_def_options_list : opt_column_def_options opt_column_def_options_listopt_column_def_options : DEFAULT valueopt_column_def_options : NULLopt_column_def_options : NOT NULLopt_column_def_options : AUTO_INCREMENTopt_column_def_options : PRIMARY KEYopt_column_def_options : UNIQUEvalue : q_STRING\n        | NUMBER\n        | STRING_VALUE q_STRING : "\'" STRING "\'" q_STRING :  select_statement : SELECT select_item_list opt_FROM opt_WHERE opt_ORDER_BY opt_LIMITopt_ORDER_BY : opt_ORDER_BY : ORDER BY identifier opt_ORDER_DIRECTIONopt_ORDER_BY : ORDER BY identifier \'.\' identifier opt_ORDER_DIRECTIONopt_ORDER_DIRECTION : opt_ORDER_DIRECTION : ASC\n        | DESC opt_LIMIT : opt_LIMIT : LIMIT NUMBERshow_tables_statement : SHOW opt_FULL TABLESopt_FROM : opt_FROM : FROM table_referencetable_reference : identifiertable_reference : identifier \'.\' identifieropt_FULL : opt_FULL : FULLselect_item_list : select_item select_item_list : select_item_list \',\' select_item select_item_list : \'*\'select_item : select_item2 select_aliasselect_item2 : table_wild\n        | expr select_alias : select_alias : AS identifiertable_wild : identifier \'.\' \'*\' opt_WHERE : opt_WHERE : WHERE exprexpr : expr OR exprexpr : expr AND exprexpr : NOT exprexpr : boolean_primaryboolean_primary : boolean_primary IS NULLboolean_primary : boolean_primary IS NOT NULLboolean_primary : boolean_primary comparison_operator predicateboolean_primary : predicatecomparison_operator : \'=\'\n        | GREATER_OR_EQ\n        | \'>\'\n        | LESS_OR_EQ\n        | \'<\'\n        | N_EQpredicate : bit_expr bit_expr : simple_exprsimple_expr : identifiersimple_expr : identifier \'.\' identifiersimple_expr : \'(\' expr \')\'simple_expr : variablevariable : \'@\' \'@\' STRINGsimple_expr : literalliteral : q_STRING\n        | NUMBER\n        | STRING_VALUEsimple_expr : function_callfunction_call : VERSION \'(\' \')\'function_call : COUNT \'(\' \'*\' \')\''
    
_lr_action_items = {'USE':([0,],[1,]),'*':([6,70,92,],[42,105,122,]),'DEFAULT':([112,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,190,192,193,202,203,204,208,209,],[-69,-56,185,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,185,-70,-63,-61,-47,-51,-60,-64,-62,-48,-50,]),'AUTOCOMMIT':([7,],[56,]),'DATABASES':([18,],[64,]),'NUMBER':([6,52,53,73,76,78,79,80,81,82,83,87,88,93,110,148,151,154,182,185,191,195,],[35,35,35,35,-111,-107,-110,-109,-106,35,-108,35,35,124,35,35,174,177,200,174,205,174,]),'UNSIGNED':([158,166,167,],[180,180,180,]),'TINYINT':([31,102,143,],[-41,-42,163,]),'SMALLINT':([31,102,143,],[-41,-42,158,]),'LIMIT':([6,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,73,74,76,78,79,80,81,82,83,85,87,88,90,91,102,106,107,108,109,110,111,112,114,115,116,117,118,119,120,122,123,135,137,138,140,152,178,196,198,199,207,210,],[-70,-41,-121,-123,-113,-81,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-70,-96,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-42,-118,-83,-82,-88,-70,-72,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,-125,-97,154,-103,-84,-75,-73,-76,-77,-75,-74,]),'IF':([31,97,102,],[-41,127,-42,]),'N_EQ':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,76,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'ORDER':([6,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,73,74,76,78,79,80,81,82,83,85,87,88,90,91,102,106,107,108,109,110,111,112,114,115,116,117,118,119,120,122,123,135,137,140,152,],[-70,-41,-121,-123,-113,-81,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-70,-96,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-42,-118,-83,-82,-88,-70,139,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,-125,-97,-103,-84,]),'SELECT':([0,],[6,]),'IS':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,77,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'INSERT':([0,],[4,]),'SET':([0,31,67,102,],[7,-41,101,-42,]),'VARCHAR':([31,102,143,],[-41,-42,159,]),'STRING_VALUE':([6,52,53,73,76,78,79,80,81,82,83,87,88,110,148,151,185,195,],[39,39,39,39,-111,-107,-110,-109,-106,39,-108,39,39,39,39,172,172,172,]),"'":([6,52,53,73,75,76,78,79,80,81,82,83,87,88,110,148,151,185,195,],[40,40,40,40,112,-111,-107,-110,-109,-106,40,-108,40,40,40,40,40,40,40,]),')':([31,35,36,37,39,43,44,45,46,47,49,52,53,76,78,79,80,81,82,83,84,87,88,89,90,91,99,102,105,106,112,114,115,116,118,119,120,123,132,133,135,140,141,142,151,158,160,161,162,163,164,165,166,167,171,172,173,174,175,176,179,180,181,183,184,185,186,188,190,192,193,195,200,201,202,203,204,205,206,208,209,],[-41,-121,-123,-113,-122,-120,-101,-112,-105,-119,-117,-70,-70,-111,-107,-110,-109,-106,-70,-108,116,-70,-70,120,-114,-100,128,-42,135,-118,-69,-102,-104,-124,-99,-98,-116,-115,149,-28,-125,-103,156,-43,-70,-56,-58,-52,-49,-54,-55,-45,-56,-56,-29,-68,-30,-67,194,-66,-44,-57,-53,-65,-58,-70,-63,-46,-61,-47,-51,-70,208,-59,-60,-64,-62,209,-31,-48,-50,]),'(':([6,16,31,33,48,52,53,69,73,76,78,79,80,81,82,83,87,88,96,102,110,134,148,159,162,],[52,62,-41,70,84,52,52,103,52,-111,-107,-110,-109,-106,52,-108,52,52,125,-42,52,151,52,182,191,]),'CREATE':([0,],[10,]),'DROP':([0,],[11,]),'NULL':([77,112,113,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,189,190,192,193,202,203,204,208,209,],[114,-69,140,-56,190,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,190,-70,-63,204,-61,-47,-51,-60,-64,-62,-48,-50,]),',':([6,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,73,76,78,79,80,81,82,83,85,87,88,90,91,102,106,109,112,114,115,116,117,118,119,120,122,123,129,131,132,133,135,140,141,142,148,151,158,160,161,162,163,164,165,166,167,169,170,171,172,173,174,175,176,179,180,181,183,184,185,186,188,190,192,193,195,201,202,203,204,206,208,209,],[-70,-41,-121,-123,-113,73,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-70,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-42,-118,-88,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,146,-17,150,-28,-125,-103,157,-43,-70,-70,-56,-58,-52,-49,-54,-55,-45,-56,-56,-18,-19,-29,-68,-30,-67,195,-66,-44,-57,-53,-65,-58,-70,-63,-46,-61,-47,-51,-70,-59,-60,-64,-62,-31,-48,-50,]),'.':([31,55,90,102,107,178,],[-41,92,121,-42,136,197,]),'ASC':([31,102,178,207,],[-41,-42,198,198,]),'NAMES':([7,],[57,]),'COMMIT':([0,],[19,]),'WAIT':([0,],[16,]),'=':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,56,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,130,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,81,-112,-105,-119,-117,-70,-70,-114,93,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,148,-125,-103,-70,]),'<':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,79,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'$end':([2,3,5,6,8,9,12,13,14,15,17,19,20,21,22,23,26,27,28,30,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,64,66,73,74,76,78,79,80,81,82,83,85,87,88,90,91,94,95,97,98,100,102,106,107,108,109,110,111,112,114,115,116,117,118,119,120,122,123,124,126,129,131,135,137,138,140,144,147,148,152,153,156,168,169,170,177,178,194,196,198,199,207,210,],[-7,-2,-33,-70,-10,-4,-13,-5,0,-8,-12,-36,-14,-1,-11,-9,-32,-6,-3,-40,-41,-121,-123,-113,-81,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-39,-20,-70,-96,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-34,-38,-23,-21,-80,-42,-118,-83,-82,-88,-70,-72,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,-35,-22,-96,-17,-125,-97,-78,-103,-24,-16,-70,-84,-71,-37,-15,-18,-19,-79,-75,-25,-73,-76,-77,-75,-74,]),'COUNT':([6,52,53,73,76,78,79,80,81,82,83,87,88,110,148,],[33,33,33,33,-111,-107,-110,-109,-106,33,-108,33,33,33,33,]),'@':([6,34,52,53,73,76,78,79,80,81,82,83,87,88,110,148,],[34,71,34,34,34,-111,-107,-110,-109,-106,34,-108,34,34,34,34,]),'FULL':([18,],[65,]),'STRING':([1,6,24,25,29,32,40,52,53,57,58,59,60,61,62,71,72,73,76,78,79,80,81,82,83,86,87,88,92,101,103,110,121,125,136,145,146,148,150,155,157,197,],[31,31,31,31,68,31,75,31,31,94,31,31,31,31,31,106,31,31,-111,-107,-110,-109,-106,31,-108,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'EXISTS':([127,],[144,]),'SHOW':([0,],[18,]),'INTO':([4,],[32,]),'BY':([139,],[155,]),'UPDATE':([0,],[25,]),'DATETIME':([31,102,143,],[-41,-42,162,]),'AS':([6,31,35,36,37,39,41,43,44,45,46,47,49,50,51,53,55,73,76,78,79,80,81,82,83,87,88,90,91,102,106,112,114,115,116,118,119,120,122,123,135,140,],[-70,-41,-121,-123,-113,-122,-91,-120,-101,-112,-105,-119,-117,86,-92,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-100,-42,-118,-69,-102,-104,-124,-99,-98,-116,-95,-115,-125,-103,]),'VERSION':([6,52,53,73,76,78,79,80,81,82,83,87,88,110,148,],[48,48,48,48,-111,-107,-110,-109,-106,48,-108,48,48,48,48,]),'LESS_OR_EQ':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,80,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'TABLE':([10,11,],[59,60,]),'UNIQUE':([112,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,190,192,193,202,203,204,208,209,],[-69,-56,183,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,183,-70,-63,-61,-47,-51,-60,-64,-62,-48,-50,]),'WHERE':([6,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,73,74,76,78,79,80,81,82,83,85,87,88,90,91,102,106,107,108,109,112,114,115,116,117,118,119,120,122,123,129,131,135,140,148,152,169,170,],[-70,-41,-121,-123,-113,-81,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-70,110,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-42,-118,-83,-82,-88,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,110,-17,-125,-103,-70,-84,-18,-19,]),'DESC':([0,31,102,178,207,],[24,-41,-42,199,199,]),'AND':([6,31,35,36,37,39,43,44,45,46,47,49,51,52,53,55,73,76,78,79,80,81,82,83,87,88,89,90,91,102,106,110,112,114,115,116,118,119,120,123,135,137,140,148,170,],[-70,-41,-121,-123,-113,-122,-120,-101,-112,-105,-119,-117,87,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,87,-114,87,-42,-118,-70,-69,-102,-104,-124,87,87,-116,-115,-125,87,-103,-70,87,]),'`':([1,6,24,25,32,52,53,58,59,60,61,62,68,72,73,76,78,79,80,81,82,83,86,87,88,92,101,103,110,121,125,136,145,146,148,150,155,157,197,],[29,29,29,29,29,29,29,29,29,29,29,29,102,29,29,-111,-107,-110,-109,-106,29,-108,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'GREATER_OR_EQ':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,78,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'FROM':([6,31,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,53,54,55,73,76,78,79,80,81,82,83,85,87,88,90,91,102,106,109,112,114,115,116,117,118,119,120,122,123,128,135,140,],[-70,-41,-121,-123,-113,72,-122,-91,-89,-120,-101,-112,-105,-119,-117,-93,-92,-70,-87,-114,-70,-111,-107,-110,-109,-106,-70,-108,-90,-70,-70,-114,-100,-42,-118,-88,-69,-102,-104,-124,-94,-99,-98,-116,-95,-115,145,-125,-103,]),'DATABASE':([10,11,],[58,61,]),'INT':([31,102,143,],[-41,-42,167,]),'INTEGER':([31,102,143,],[-41,-42,166,]),'TABLES':([18,63,65,],[-85,100,-86,]),'LONGTEXT':([31,102,143,],[-41,-42,161,]),'PRIMARY':([112,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,190,192,193,202,203,204,208,209,],[-69,-56,187,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,187,-70,-63,-61,-47,-51,-60,-64,-62,-48,-50,]),'BOOL':([31,102,143,],[-41,-42,164,]),'KEY':([187,],[203,]),'VALUES':([31,69,102,104,149,],[-41,-26,-42,134,-27,]),'AUTO_INCREMENT':([112,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,190,192,193,202,203,204,208,209,],[-69,-56,186,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,186,-70,-63,-61,-47,-51,-60,-64,-62,-48,-50,]),'NOT':([6,52,53,73,77,87,88,110,112,148,158,160,161,162,163,164,166,167,172,174,176,180,181,183,184,185,186,190,192,193,202,203,204,208,209,],[53,53,53,53,113,53,53,53,-69,53,-56,189,-52,-49,-54,-55,-56,-56,-68,-67,-66,-57,-53,-65,189,-70,-63,-61,-47,-51,-60,-64,-62,-48,-50,]),'>':([6,31,35,36,37,39,43,44,45,46,47,49,52,53,55,73,76,78,79,80,81,82,83,87,88,90,102,106,110,112,114,115,116,120,123,135,140,148,],[-70,-41,-121,-123,-113,-122,-120,83,-112,-105,-119,-117,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,-114,-42,-118,-70,-69,-102,-104,-124,-116,-115,-125,-103,-70,]),'OR':([6,31,35,36,37,39,43,44,45,46,47,49,51,52,53,55,73,76,78,79,80,81,82,83,87,88,89,90,91,102,106,110,112,114,115,116,118,119,120,123,135,137,140,148,170,],[-70,-41,-121,-123,-113,-122,-120,-101,-112,-105,-119,-117,88,-70,-70,-114,-70,-111,-107,-110,-109,-106,-70,-108,-70,-70,88,-114,88,-42,-118,-70,-69,-102,-104,-124,88,88,-116,-115,-125,88,-103,-70,88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'commit_statement':([0,],[2,]),'show_tables_statement':([0,],[3,]),'function_call':([6,52,53,73,82,87,88,110,148,],[36,36,36,36,36,36,36,36,36,]),'variable':([6,52,53,73,82,87,88,110,148,],[49,49,49,49,49,49,49,49,49,]),'set_names_statement':([0,],[5,]),'column_definition':([143,],[165,]),'opt_WHERE':([74,129,],[111,147,]),'simple_expr':([6,52,53,73,82,87,88,110,148,],[37,37,37,37,37,37,37,37,37,]),'show_databases_statement':([0,],[13,]),'opt_column_def_options':([160,184,],[184,184,]),'select_item_list':([6,],[38,]),'opt_ORDER_BY':([111,],[138,]),'drop_database_statement':([0,],[8,]),'create_database_statement':([0,],[9,]),'table_wild':([6,73,],[41,41,]),'opt_LIMIT':([138,],[153,]),'update_table_statement':([0,],[12,]),'literal':([6,52,53,73,82,87,88,110,148,],[47,47,47,47,47,47,47,47,47,]),'fieldlist':([103,],[132,]),'statement':([0,],[14,]),'set_statement':([0,],[15,]),'opt_FROM':([38,],[74,]),'desc_table_statement':([0,],[17,]),'q_STRING':([6,52,53,73,82,87,88,110,148,151,185,195,],[43,43,43,43,43,43,43,43,43,176,176,176,]),'boolean_primary':([6,52,53,73,87,88,110,148,],[44,44,44,44,44,44,44,44,]),'bit_expr':([6,52,53,73,82,87,88,110,148,],[45,45,45,45,45,45,45,45,45,]),'predicate':([6,52,53,73,82,87,88,110,148,],[46,46,46,46,115,46,46,46,46,]),'values_list':([151,],[175,]),'table_reference':([72,],[108,]),'data_type':([143,],[160,]),'opt_UNSIGNED':([158,166,167,],[181,192,193,]),'create_definition_list':([125,],[141,]),'opt_ORDER_DIRECTION':([178,207,],[196,210,]),'wait_statement':([0,],[20,]),'opt_FULL':([18,],[63,]),'select_statement':([0,],[21,]),'drop_table_statement':([0,],[22,]),'col_expr_list':([101,],[129,]),'opt_IF_EXISTS':([97,],[126,]),'insert_statement':([0,],[23,]),'identifier':([1,6,24,25,32,52,53,58,59,60,61,62,72,73,82,86,87,88,92,101,103,110,121,125,136,145,146,148,150,155,157,197,],[30,55,66,67,69,90,90,95,96,97,98,99,107,55,90,117,90,90,123,130,133,90,123,143,152,168,130,90,171,178,143,207,]),'opt_column_def_options_list':([160,184,],[188,201,]),'select_item2':([6,73,],[50,50,]),'expr':([6,52,53,73,87,88,110,148,],[51,89,91,51,118,119,137,170,]),'opt_fieldlist':([69,],[104,]),'create_definition':([125,157,],[142,179,]),'value':([151,185,195,],[173,202,206,]),'use_database_statement':([0,],[27,]),'select_alias':([50,],[85,]),'create_table_statement':([0,],[28,]),'select_item':([6,73,],[54,109,]),'set_autocommit_statement':([0,],[26,]),'col_expr':([101,146,],[131,169,]),'comparison_operator':([44,],[82,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> select_statement','statement',1,'p_statement','parser.py',12),
  ('statement -> show_tables_statement','statement',1,'p_statement','parser.py',13),
  ('statement -> create_table_statement','statement',1,'p_statement','parser.py',14),
  ('statement -> create_database_statement','statement',1,'p_statement','parser.py',15),
  ('statement -> show_databases_statement','statement',1,'p_statement','parser.py',16),
  ('statement -> use_database_statement','statement',1,'p_statement','parser.py',17),
  ('statement -> commit_statement','statement',1,'p_statement','parser.py',18),
  ('statement -> set_statement','statement',1,'p_statement','parser.py',19),
  ('statement -> insert_statement','statement',1,'p_statement','parser.py',20),
  ('statement -> drop_database_statement','statement',1,'p_statement','parser.py',21),
  ('statement -> drop_table_statement','statement',1,'p_statement','parser.py',22),
  ('statement -> desc_table_statement','statement',1,'p_statement','parser.py',23),
  ('statement -> update_table_statement','statement',1,'p_statement','parser.py',24),
  ('statement -> wait_statement','statement',1,'p_statement','parser.py',25),
  ('wait_statement -> WAIT ( identifier ) FROM identifier','wait_statement',6,'p_wait_statement','parser.py',30),
  ('update_table_statement -> UPDATE identifier SET col_expr_list opt_WHERE','update_table_statement',5,'p_update_table_statement','parser.py',37),
  ('col_expr_list -> col_expr','col_expr_list',1,'p_col_expr_list_one','parser.py',44),
  ('col_expr_list -> col_expr_list , col_expr','col_expr_list',3,'p_col_expr_list','parser.py',49),
  ('col_expr -> identifier = expr','col_expr',3,'p_col_expr','parser.py',54),
  ('desc_table_statement -> DESC identifier','desc_table_statement',2,'p_desc_table_statement','parser.py',59),
  ('drop_database_statement -> DROP DATABASE identifier','drop_database_statement',3,'p_drop_database_statement','parser.py',65),
  ('drop_table_statement -> DROP TABLE identifier opt_IF_EXISTS','drop_table_statement',4,'p_drop_table_statement','parser.py',71),
  ('opt_IF_EXISTS -> <empty>','opt_IF_EXISTS',0,'p_opt_if_exists_empty','parser.py',78),
  ('opt_IF_EXISTS -> IF EXISTS','opt_IF_EXISTS',2,'p_opt_if_exists','parser.py',83),
  ('insert_statement -> INSERT INTO identifier opt_fieldlist VALUES ( values_list )','insert_statement',8,'p_insert_statement','parser.py',88),
  ('opt_fieldlist -> <empty>','opt_fieldlist',0,'p_opt_fieldlist_empty','parser.py',104),
  ('opt_fieldlist -> ( fieldlist )','opt_fieldlist',3,'p_opt_fieldlist','parser.py',109),
  ('fieldlist -> identifier','fieldlist',1,'p_fieldlist_one','parser.py',114),
  ('fieldlist -> fieldlist , identifier','fieldlist',3,'p_fieldlist_many','parser.py',119),
  ('values_list -> value','values_list',1,'p_values_list_one','parser.py',128),
  ('values_list -> values_list , value','values_list',3,'p_values_list_many','parser.py',133),
  ('set_statement -> set_autocommit_statement','set_statement',1,'p_set_statement','parser.py',142),
  ('set_statement -> set_names_statement','set_statement',1,'p_set_statement','parser.py',143),
  ('set_names_statement -> SET NAMES STRING','set_names_statement',3,'p_set_names_statement','parser.py',147),
  ('set_autocommit_statement -> SET AUTOCOMMIT = NUMBER','set_autocommit_statement',4,'p_set_statement_autocommit','parser.py',152),
  ('commit_statement -> COMMIT','commit_statement',1,'p_commit_statement','parser.py',158),
  ('create_table_statement -> CREATE TABLE identifier ( create_definition_list )','create_table_statement',6,'p_create_table_statement','parser.py',163),
  ('create_database_statement -> CREATE DATABASE identifier','create_database_statement',3,'p_create_database_statement','parser.py',169),
  ('show_databases_statement -> SHOW DATABASES','show_databases_statement',2,'p_show_databases_statement','parser.py',175),
  ('use_database_statement -> USE identifier','use_database_statement',2,'p_use_database_statement','parser.py',180),
  ('identifier -> STRING','identifier',1,'p_identifier','parser.py',186),
  ('identifier -> ` STRING `','identifier',3,'p_identifier_escaped','parser.py',191),
  ('create_definition_list -> create_definition','create_definition_list',1,'p_create_definition_list','parser.py',196),
  ('create_definition_list -> create_definition_list , create_definition','create_definition_list',3,'p_create_definition_list','parser.py',197),
  ('create_definition -> identifier column_definition','create_definition',2,'p_create_definition','parser.py',201),
  ('column_definition -> data_type opt_column_def_options_list','column_definition',2,'p_column_definition','parser.py',206),
  ('data_type -> INTEGER opt_UNSIGNED','data_type',2,'p_data_type','parser.py',214),
  ('data_type -> VARCHAR ( NUMBER )','data_type',4,'p_data_type','parser.py',215),
  ('data_type -> DATETIME','data_type',1,'p_data_type','parser.py',216),
  ('data_type -> DATETIME ( NUMBER )','data_type',4,'p_data_type','parser.py',217),
  ('data_type -> INT opt_UNSIGNED','data_type',2,'p_data_type','parser.py',218),
  ('data_type -> LONGTEXT','data_type',1,'p_data_type','parser.py',219),
  ('data_type -> SMALLINT opt_UNSIGNED','data_type',2,'p_data_type','parser.py',220),
  ('data_type -> TINYINT','data_type',1,'p_data_type','parser.py',221),
  ('data_type -> BOOL','data_type',1,'p_data_type','parser.py',222),
  ('opt_UNSIGNED -> <empty>','opt_UNSIGNED',0,'p_opt_UNSIGNED','parser.py',227),
  ('opt_UNSIGNED -> UNSIGNED','opt_UNSIGNED',1,'p_opt_UNSIGNED','parser.py',228),
  ('opt_column_def_options_list -> <empty>','opt_column_def_options_list',0,'p_opt_column_def_options_list_empty','parser.py',232),
  ('opt_column_def_options_list -> opt_column_def_options opt_column_def_options_list','opt_column_def_options_list',2,'p_opt_column_def_options_list','parser.py',239),
  ('opt_column_def_options -> DEFAULT value','opt_column_def_options',2,'p_DEFAULT_CLAUSE','parser.py',248),
  ('opt_column_def_options -> NULL','opt_column_def_options',1,'p_NULL','parser.py',255),
  ('opt_column_def_options -> NOT NULL','opt_column_def_options',2,'p_NOT_NULL','parser.py',262),
  ('opt_column_def_options -> AUTO_INCREMENT','opt_column_def_options',1,'p_AUTO_INCREMENT','parser.py',269),
  ('opt_column_def_options -> PRIMARY KEY','opt_column_def_options',2,'p_PRIMARY_KEY','parser.py',276),
  ('opt_column_def_options -> UNIQUE','opt_column_def_options',1,'p_UNIQUE','parser.py',283),
  ('value -> q_STRING','value',1,'p_value','parser.py',290),
  ('value -> NUMBER','value',1,'p_value','parser.py',291),
  ('value -> STRING_VALUE','value',1,'p_value','parser.py',292),
  ("q_STRING -> ' STRING '",'q_STRING',3,'p_q_STRING','parser.py',297),
  ('q_STRING -> <empty>','q_STRING',0,'p_q_STRING_EMPTY','parser.py',302),
  ('select_statement -> SELECT select_item_list opt_FROM opt_WHERE opt_ORDER_BY opt_LIMIT','select_statement',6,'p_select_statement','parser.py',307),
  ('opt_ORDER_BY -> <empty>','opt_ORDER_BY',0,'p_opt_ORDER_BY_empty','parser.py',316),
  ('opt_ORDER_BY -> ORDER BY identifier opt_ORDER_DIRECTION','opt_ORDER_BY',4,'p_opt_ORDER_BY_simple','parser.py',320),
  ('opt_ORDER_BY -> ORDER BY identifier . identifier opt_ORDER_DIRECTION','opt_ORDER_BY',6,'p_opt_ORDER_BY_extended','parser.py',326),
  ('opt_ORDER_DIRECTION -> <empty>','opt_ORDER_DIRECTION',0,'p_opt_ORDER_DIRECTION_empty','parser.py',332),
  ('opt_ORDER_DIRECTION -> ASC','opt_ORDER_DIRECTION',1,'p_opt_ORDER_DIRECTION','parser.py',337),
  ('opt_ORDER_DIRECTION -> DESC','opt_ORDER_DIRECTION',1,'p_opt_ORDER_DIRECTION','parser.py',338),
  ('opt_LIMIT -> <empty>','opt_LIMIT',0,'p_opt_LIMIT_empty','parser.py',343),
  ('opt_LIMIT -> LIMIT NUMBER','opt_LIMIT',2,'p_opt_LIMIT','parser.py',348),
  ('show_tables_statement -> SHOW opt_FULL TABLES','show_tables_statement',3,'p_show_tables_statement','parser.py',353),
  ('opt_FROM -> <empty>','opt_FROM',0,'p_opt_from_empty','parser.py',359),
  ('opt_FROM -> FROM table_reference','opt_FROM',2,'p_opt_from','parser.py',363),
  ('table_reference -> identifier','table_reference',1,'p_table_reference','parser.py',368),
  ('table_reference -> identifier . identifier','table_reference',3,'p_table_reference_w_database','parser.py',373),
  ('opt_FULL -> <empty>','opt_FULL',0,'p_opt_FULL_empty','parser.py',379),
  ('opt_FULL -> FULL','opt_FULL',1,'p_opt_FULL','parser.py',384),
  ('select_item_list -> select_item','select_item_list',1,'p_select_item_list_select_item','parser.py',389),
  ('select_item_list -> select_item_list , select_item','select_item_list',3,'p_select_item_list','parser.py',394),
  ('select_item_list -> *','select_item_list',1,'p_select_item_list_star','parser.py',399),
  ('select_item -> select_item2 select_alias','select_item',2,'p_select_item','parser.py',407),
  ('select_item2 -> table_wild','select_item2',1,'p_select_item2','parser.py',412),
  ('select_item2 -> expr','select_item2',1,'p_select_item2','parser.py',413),
  ('select_alias -> <empty>','select_alias',0,'p_select_alias_empty','parser.py',418),
  ('select_alias -> AS identifier','select_alias',2,'p_select_alias','parser.py',423),
  ('table_wild -> identifier . *','table_wild',3,'p_table_wild','parser.py',428),
  ('opt_WHERE -> <empty>','opt_WHERE',0,'p_opt_WHERE_empty','parser.py',433),
  ('opt_WHERE -> WHERE expr','opt_WHERE',2,'p_opt_WHERE','parser.py',437),
  ('expr -> expr OR expr','expr',3,'p_expr_OR','parser.py',442),
  ('expr -> expr AND expr','expr',3,'p_expr_AND','parser.py',447),
  ('expr -> NOT expr','expr',2,'p_expr_NOT','parser.py',452),
  ('expr -> boolean_primary','expr',1,'p_expr_bool_primary','parser.py',457),
  ('boolean_primary -> boolean_primary IS NULL','boolean_primary',3,'p_boolean_primary_is_null','parser.py',462),
  ('boolean_primary -> boolean_primary IS NOT NULL','boolean_primary',4,'p_boolean_primary_is_not_null','parser.py',467),
  ('boolean_primary -> boolean_primary comparison_operator predicate','boolean_primary',3,'p_boolean_primary_comparison','parser.py',472),
  ('boolean_primary -> predicate','boolean_primary',1,'p_boolean_primary_predicate','parser.py',477),
  ('comparison_operator -> =','comparison_operator',1,'p_comparison_operator','parser.py',482),
  ('comparison_operator -> GREATER_OR_EQ','comparison_operator',1,'p_comparison_operator','parser.py',483),
  ('comparison_operator -> >','comparison_operator',1,'p_comparison_operator','parser.py',484),
  ('comparison_operator -> LESS_OR_EQ','comparison_operator',1,'p_comparison_operator','parser.py',485),
  ('comparison_operator -> <','comparison_operator',1,'p_comparison_operator','parser.py',486),
  ('comparison_operator -> N_EQ','comparison_operator',1,'p_comparison_operator','parser.py',487),
  ('predicate -> bit_expr','predicate',1,'p_predicate','parser.py',492),
  ('bit_expr -> simple_expr','bit_expr',1,'p_bit_expr','parser.py',497),
  ('simple_expr -> identifier','simple_expr',1,'p_simple_expr_identifier','parser.py',502),
  ('simple_expr -> identifier . identifier','simple_expr',3,'p_simple_expr_identifier_full','parser.py',507),
  ('simple_expr -> ( expr )','simple_expr',3,'p_simple_expr_parent','parser.py',517),
  ('simple_expr -> variable','simple_expr',1,'p_simple_expr_variable','parser.py',522),
  ('variable -> @ @ STRING','variable',3,'p_variable','parser.py',527),
  ('simple_expr -> literal','simple_expr',1,'p_simple_expr_literal','parser.py',532),
  ('literal -> q_STRING','literal',1,'p_literal','parser.py',537),
  ('literal -> NUMBER','literal',1,'p_literal','parser.py',538),
  ('literal -> STRING_VALUE','literal',1,'p_literal','parser.py',539),
  ('simple_expr -> function_call','simple_expr',1,'p_simple_expr_function_call','parser.py',544),
  ('function_call -> VERSION ( )','function_call',3,'p_function_call_version','parser.py',549),
  ('function_call -> COUNT ( * )','function_call',4,'p_function_call_count_star','parser.py',554),
]
