################################################################
####controllers#################################################
################################################################
  
################################
####about#######################
################################
def about():
    return dict()

################################
####account#####################
################################        
def account():
    return dict()  
    
################################
####contact#####################
################################
def contact():
    return dict()

################################
####discover####################
################################        
def discover():
    return dict()

################################
####faq#########################
################################                  
def faq():
    return dict()

################################
####feed########################
################################
def feed():
    return dict()
    
################################
####inbox#######################
################################ 
def inbox():
    return dict()

################################
####index#######################
################################        
def index():
    return dict()

################################
####mission#####################
################################        
def mission():
    return dict()

################################
####member######################
################################        
def member():

    try:
        username_from_url = db(db.auth_user.username == request.args(0)).select()[0]['username']
    except IndexError:
        redirect(URL('members'))
    
    
    return dict(username_from_url=username_from_url)
    
################################
####members#####################
################################        
def members():
    return dict()     

################################
####notifications###############
################################        
def notifications():
    return dict() 

################################
####privacy#####################
################################
def privacy():
   
    return dict()

def stats():
   
    return dict()   

################################
####search######################
################################        
def search():
    return dict()  
     
################################
####tag#########################
################################          
def tag():
    return dict()
    
################################
####tags########################
################################          
def tags():
    return dict()   

################################
####terms#######################
################################
def terms():
    return dict()
    
################################
####transparency################
################################
def transparency():

    return dict()
    

################################################################
####ajax########################################################
################################################################    
            
################################################################
####helpers#####################################################
################################################################

################################
####download####################
################################   
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

################################
####call########################
################################ 
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

################################
####data########################
################################ 
@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
