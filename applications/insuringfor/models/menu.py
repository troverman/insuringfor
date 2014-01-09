################################################################
####menu.py#####################################################
################################################################

################################
####title#######################
################################  
if request.function == 'index':
    response.title = 'insuringfor'
else:
    response.title = request.function

################################
####meta########################
################################ 
response.meta.author = 'Trevor Overman'
response.meta.description = 'the internet is hospitable'
response.meta.keywords = 'insurance, nonprofit, crowd owned, evolution, transparent'
response.meta.generator = 'we are one'
