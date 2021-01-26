#Se importan las librerias necesarias
import sys
import ply.yacc as yacc
from analizador_lexico import tokens #Se importan los tokens declarados en el analizador lexico.

VERBOSE = 1

#A continuación se declaran las precedencias.
precedence = (
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMA'),
    ('left', 'IGUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'PUNTOYCOMA'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ES_IGUAL', 'DESIGUAL'),
    ('nonassoc', 'MENOR', 'MENOR_IGUAL', 'MAYOR', 'MAYOR_IGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('right', 'CORCHETE_IZQ'),
    ('nonassoc', 'NEW'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)


#A continuación se declaran varias funciones las cuales nos servirán para poder validar los errores sintacticos.
#En este apartado se hace uso de los tokens que fueron declarados en el analizador lexico.

def p_program(p):
    'program : declaration_list'
			 
    pass

def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
					   | additive_expression
   '''
   pass

#Se declara una funcion que nos servirá para juntas las posibles formas de declaración
def p_declaration(p):
	'''declaration : var_declaration
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
				   | alert_stmt
				   | additive_expression
	'''
	pass

#Se declara una función que valida las distintas formas de escribir una expresión
def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING PUNTOYCOMA
				 | echo_stmt ECHO IDVAR PUNTOYCOMA
				 | empty
				 | echo_stmt ECHO NUMERO PUNTOYCOMA
				 | echo_stmt ECHO boolean PUNTOYCOMA
				 | echo_stmt ECHO fun_declaration PUNTOYCOMA
	'''
	pass

#Esta funcion es para validar la estructura que tendrá "Alert"
def p_alert_stmt(p):
	'''alert_stmt : ALERT PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
				  | empty

	'''
	pass

#Se declara una función que nos servirá para validar los encabezados
def p_header_declaration(p):
	'''header_declaration : REQUIRE PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
                          | INCLUDE PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
    '''
	pass

#Se declara una función que nos servirá para validar la declaración de una clase
def p_class_declaration(p):
	'''class_declaration : area CLASS VARIABLE LLAVE_IZQ attribute LLAVE_DER
						 | CLASS VARIABLE LLAVE_IZQ attribute LLAVE_DER
	'''
	pass

#Se declara una función que nos servirá para validar la forma en la que se ponen atributos
def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass

#Se declara una funcioón que nos servirá para validar si es private, public o protected
def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass

#Se declara una función que nos servirá para validar las distintas formas de declarar una variable
def p_var_declaration(p):
	'''var_declaration : VARIABLE PUNTOYCOMA var_declaration
                       | VAR VARIABLE IGUAL simple_expression
					   | VARIABLE PUNTOYCOMA
                       | TIMESTIMES VARIABLE PUNTOYCOMA
                       | TIMESTIMES VARIABLE PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL NUMERO PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL NUMERO PUNTOYCOMA
                       | VARIABLE IGUAL boolean PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL boolean PUNTOYCOMA
                       | VARIABLE IGUAL VARIABLE PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL VARIABLE PUNTOYCOMA
                       | AMPERSANT VARIABLE PUNTOYCOMA var_declaration
                       | AMPERSANT VARIABLE IGUAL VARIABLE PUNTOYCOMA selection_stmt
                       | AMPERSANT VARIABLE PUNTOYCOMA
                       | VARIABLE IGUAL simple_expression PUNTOYCOMA
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una función
def p_fun_declaration(p):
	'''fun_declaration : FUNCTION VARIABLE PARENT_IZQ params PARENT_DER
					   | FUNCTION VARIABLE PARENT_IZQ params PARENT_DER compount_stmt
	'''
	pass

#Se declara una función que nos servirá para validar una lista de parametros o simplemente un espacio vacio
def p_params(p):
	'''params : param_list
			  | empty
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una lista de parametros
def p_param_list(p):
	'''param_list : param_list COMA param_list
				  | param
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de un parametro
def p_param(p):
	'''param : VARIABLE
             | VARIABLE CORCHETE_IZQ CORCHETE_DER PUNTOYCOMA
    '''
	pass

#Se declara una función que nos servirá para validar la estructura de una declaración compuesta
def p_compount_stmt(p):
	'compount_stmt : LLAVE_IZQ echo_stmt local_declarations echo_stmt statement_list echo_stmt LLAVE_DER'
	pass

#Se declara una función que nos servirá para validar la estructura de una declaración de forma local
def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						  | empty
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una lista de declaraciones
def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
					  | alert_stmt
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una declaración
def p_statement(p):
	'''statement : expression_stmt
				 | compount_stmt
				 | selection_stmt
				 | iteration_stmt
			     | return_stmt
			     | class_declaration
				 | echo_stmt
				 | expression
				 | additive_expression
				 | alert_stmt
	'''
	pass

#Se declara una función que nos servirá para validar las posibles expresiones que acompañarian a una declaración
def p_expression_stmt(p):
	'''expression_stmt : expression PUNTOYCOMA
					   | additive_expression
					   | alert_stmt
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de un IF
def p_selection_stmt_1(p):
	'''selection_stmt : IF PARENT_IZQ expression PARENT_DER statement
					  | IF PARENT_IZQ expression PARENT_DER statement selection

	'''
	pass

#Se declara una función que nos servirá para validar la estructura de un ELSE y ELSEIF
def p_selection(p):
	'''selection : ELSE statement
				 | ELSEIF statement selection
	 '''
	pass

#Se declara una función que nos servirá para validar la estructura de un SWITCH CASE
def p_selection_stmt_2(p):
	'''selection_stmt : SWITCH PARENT_IZQ var PARENT_DER statement
					  | CASE NUMERO DOS_PUNTOS statement BREAK PUNTOYCOMA
					  | DEFAULT DOS_PUNTOS statement BREAK PUNTOYCOMA

	'''
	pass

#Se declara una función que nos servirá para validar la estructura de un FOR
def p_iteration_stmt_1(p):
	'iteration_stmt : FOR PARENT_IZQ var_declaration PUNTOYCOMA expression PUNTOYCOMA additive_expression PARENT_DER statement '
	pass

#Se declara una función que nos servirá para validar la estructura de un WHILE
def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE PARENT_IZQ expression PARENT_DER statement'
	pass

#Se declara una función que nos servirá para validar la estructura de un DO WHILE
def p_iteration_stmt_3(p):
	'iteration_stmt : DO LLAVE_IZQ statement PUNTOYCOMA LLAVE_DER WHILE PARENT_IZQ expression PARENT_DER'
	pass

#Se declara una función que nos servirá para validar la estructura de un return
def p_return_stmt(p):
	'''return_stmt : RETURN PUNTOYCOMA
				   | RETURN expression PUNTOYCOMA
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una expresión
def p_expression(p):
	'''expression : VARIABLE relop NUMERO
				  | simple_expression
				  | VARIABLE IGUAL AMPERSANT VARIABLE
			      | expression AND expression
				  | expression OR expression
				  | additive_expression
				  | alert_stmt
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una variable
def p_var(p):
	'''var : VARIABLE
		   | VARIABLE CORCHETE_IZQ expression CORCHETE_DER
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una expresión simple
def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
						 | alert_stmt
	'''
	pass

#Se declara una función que nos servirá para validar expresiones de comparación como mayor, menor, etc.
def p_relop(p):
	'''relop : MENOR
			 | MENOR_IGUAL
			 | MAYOR
			 | MAYOR_IGUAL
			 | DESIGUAL
			 | DISTINTO
			 | ES_IGUAL
	'''
	pass

#Se declara una función que nos servirá para validar la estructura de una expresión aditiva, es decir un incremento
def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | VARIABLE DECREMENTO PUNTOYCOMA
    				       | VARIABLE INCREMENTO PUNTOYCOMA
						   | VARIABLE DECREMENTO
    				       | VARIABLE INCREMENTO
	'''
	pass

#Se declara una función que nos servirá para validar operadores basicos como la suma y resta
def p_addop(p):
	'''addop : SUMA
			 | RESTA
	'''
	pass

#Se declara una función que nos servirá para validar algunos operadores
def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass

#Se declara una función que nos servirá para validar operadores basicos como la multiplicación y la división
def p_mulop(p):
	'''mulop : MULTIPLICACION
			 | DIVISION
	'''
	pass

#Se declara una función que nos servirá para validar los parentesis en las expresiones
def p_factor(p):
	'''factor : PARENT_IZQ expression PARENT_DER
			  | var
			  | NUMERO
			  | boolean
			  | IDVAR PARENT_IZQ args PARENT_DER
	'''
	pass

#Se declara una función que nos servirá para validar ya sea args o VOID
def p_args(p):
	'''args : args_list
			| empty
			| VOID
	'''
	pass

#Se declara una función que nos servirá para validar lista de args junto al punto y coma
def p_args_list(p):
	'''args_list : args_list COMA expression
				 | expression
	'''
	pass

#Se declara una función que nos servirá para validar expresiones booleanas
def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass

#Se declara una función que nos servirá para validar la forma en la que se declara una nueva clase
def p_tclass(p):
	'typeclass : VARIABLE IDVAR IGUAL NEW constructor PUNTOYCOMA'
	pass

#Se declara una función que nos servirá para validar la estructura de un constructor
def p_costructor(p):
	'''constructor : VARIABLE PARENT_IZQ PARENT_DER
				   | VARIABLE PARENT_IZQ args PARENT_DER
	'''
	pass

#Se declara una función que nos servirá para validar los espacios vacios
def p_empty(p):
	'empty :'
	pass

#Se declara una función que nos servirá para mostrar en consola los posibles errores detectados
def p_error(p):
    if VERBOSE:
        if p is not None:
            print (chr(27)+"[1;31m"+"\t ERROR: Error de sintaxis - Token Inesperado" + chr(27)+"[0m")
            print ("\t\tLinea: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print (chr(27)+"[1;31m"+"\t Error durante la compilación: “Error de sintáxis”"+chr(27)+"[0m")
            print ("\t\tLinea:  "+str(p))

    else:
        raise Exception('syntax', 'error')


#Se hace uso de la libreria yacc
parser = yacc.yacc()

script = 'prueba.js' #En esta linea se agrega el nombre del archivo .js que se va analizar
scriptfile = open(script, 'r') #Con esta linea abrimos el archivo .js
scriptdata = scriptfile.read() #Con esta linea leemos el archivo .js
#print (scriptdata)

#Finalmente se hace las impresiones correspondientes para mostrar si se detectaron errores o no en el programa analizado
print (chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
parser.parse(scriptdata, tracking=False) #En esta parte se mostrarían los errores en caso de existir alguna
print (chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")
#Se imprime los integrantes del equipi
print("Programa elaborado por:"+"\n"
        +"<<Mis Oy Cristina de Jesus>>"+"\n"
        +"<<Poot Can Gener Emmanuel>>"+"\n"
        +"<<Uicab Balam Nanci Arai>>")
