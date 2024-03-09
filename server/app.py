import controllers.compiler.parser as parser

parser.parser.parse(
'''
// error if
var x d;
var p kk;
'''
)
