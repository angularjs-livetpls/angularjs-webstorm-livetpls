import os
import xml.etree.ElementTree as etree

def printTemplates(tplGroupXmlTree, tplGroupName, lang):
	print('####'+tplGroupName)
	for template in tplGroupXmlTree.getroot():
		print('`'+template.attrib['name']+'` - ' + template.attrib['description']+'\n')
		print('```'+lang)
		print(template.attrib['value'])
		print('```')

print('##Live Templates')
print('###AngularJS')
printTemplates(etree.parse('angularjs_global.xml'), 'Globals', 'JavaScript')
printTemplates(etree.parse('angularjs_scope.xml'), 'Scope related abbrevations', 'JavaScript')
printTemplates(etree.parse('angularjs_module.xml'), 'Module related abbrevations', 'JavaScript')
printTemplates(etree.parse('angularjs_directive.xml'), 'Directives related abbrevations', 'JavaScript')
printTemplates(etree.parse('angularjs_route.xml'), 'Routes related abbrevations', 'JavaScript')
printTemplates(etree.parse('angularjs_html.xml'), 'HTML - abbrevations to be used in HTML files', 'HTML')
print('###Jasmine')
printTemplates(etree.parse('Jasmine.xml'), 'Various Jasmine + AngularJS abbrevations', 'HTML')