 #-*- coding: utf-8 -*-
from zope.app.component.hooks import getSite
from Products.CMFCore.interfaces import ISiteRoot


def to_utf8(value):
    return unicode(value, 'utf-8') 

def userupdate(event):
    """ Handler for User Login in Site """
    request = getSite().REQUEST
    membership = getSite().portal_membership
    portalGroup = getSite().portal_groups 
    
    user_login = membership.getAuthenticatedMember()
    folder_clientes = getSite().get('clientes','')
    
    if not 'funcionario' in portalGroup.getGroupsByUserId(user_login.id) and\
        user_login.id != 'admin':
        if not user_login.id in folder_clientes.objectIds():
            objects = {'type_name':'pizzaria.content.cliente',
                       'id': user_login.id,
                       #'title':user_login.getProperties().get('title','')
                       }
            
            folder_clientes.invokeFactory(**objects)  
            cadastro = folder_clientes[user_login.id]

            url = cadastro.absolute_url() + '/edit'                
                
        else:
            
            url = getSite().absolute_url() + '/home-cliente'  
    
    else:
        
        url = getSite().absolute_url() + '/home-funcionario'
      
    request.other["came_from"] = url
    #request.form["came_from"] = url
    request.response.redirect(url, lock=True)
    
    