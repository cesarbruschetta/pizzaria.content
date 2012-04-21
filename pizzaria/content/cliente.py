# coding=utf-8
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder

from pizzaria.content import MessageFactory as _
from z3c.relationfield.schema import RelationChoice

from zope.app.component.hooks import getSite
from Products.CMFCore.interfaces import ISiteRoot 

from zope.interface import Interface

# Interface and schema

class ICadastroCliente(form.Schema):
    """Content Cadastro Cliente """
    
    title = schema.TextLine(
        title=_(u"Nome Completo"),
        description=_(u"Digite seu nome Completo"),
        required=True,
        )
    
    cpf = schema.TextLine(
        title=_(u"CPF"),
        description=_(u"Digite seu Cpf"),
        required=True,
        )

    rg = schema.TextLine(
        title=_(u"RG"),
        description=_(u"Digite seu Rg"),
        required=False,
        )

    telefone = schema.TextLine(
                title=_(u"Telefone"),
                description=_(u"Digite seu telefone com DDD"),
                required=True,
                )
    
    endereco = schema.TextLine(
                title=_(u"Endereço para entrega"),
                description=_(u"Digite o entereço para que seu pedito seja entrege"),
                required=True,
                )

    bairro = schema.TextLine(
                title=_(u"Bairro"),
                description=_(u"Digite seu bairro"),
                required=True,
                )
    
    cidade = schema.TextLine(
                title=_(u"Cidade"),
                description=_(u"Digite sua cidade"),
                required=True,
                )
    
    estado = schema.TextLine(
            title=_(u"Estado"),
            description=_(u"Digite seu estado"),
            required=True,
            )

    cep = schema.TextLine(
            title=_(u"Cep"),
            description=_(u"Digite seu Cep"),
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
        
class HomeCliente(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('home-cliente')
    
    def getCadastro(self):
        membership = getSite().portal_membership
        user_login = membership.getAuthenticatedMember()
        try:
            cadastro= getSite()['clientes'][user_login.id]
        except:
            cadastro= None
            
        return cadastro
    
    def getProduto(self):
        urltool = getSite().portal_url
        caminho = urltool.getPortalPath()+'/cardapio';
        ctool = getSite().portal_catalog
        items = ctool(portal_type='pizzaria.content.produto', 
                      review_state='published',
                      path=caminho)        
        return items

        
    
        
class HomeFuncionario(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('home-funcionario')
    
    
    
    
        