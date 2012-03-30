# coding=utf-8
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder

from pizzaria.content import MessageFactory as _
from z3c.relationfield.schema import RelationChoice

from zope.app.component.hooks import getSite 

from zope.interface import Interface

# Interface and schema

class ICadastroProduto(form.Schema):
    """Content Cadastro Produto """
    
    cpf = schema.TextLine(
        title=_(u"Codigo"),
        description=_(u"Digite o código do produto"),
        required=True,
        )
    
    Valor = schema.TextLine(
            title=_(u"Valor do produto"),
        description=_(u"Digite o valor deste produto"),
        required=True,
        )


#    macro = schema.Choice(
#         title=_(u"Categoria"),
#         description=_(u"Selecione a macro para este conteudo.\
#                         Para gerenciar as macros <a href=\"/control-panel-objects/vindula_categories\" target=\"_blank\">clique aqui</a>."),
#         source=ControlPanelMacro('vindula_categories', 'list_macros'),
#         required=False,
#        )
#        
        

        
        