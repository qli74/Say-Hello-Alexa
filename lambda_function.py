"""
In this file we specify default event handlers which are then populated into the handler map using metaprogramming
Copyright Anjishnu Kumar 2015
Happy Hacking!
"""

from ask import alexa

def lambda_handler(request_obj, context=None):
    '''
    This is the main function to enter to enter into this code.
    If you are hosting this code on AWS Lamibda, this should be the entry point.
    Otherwise your server can hit this code as long as you remember that the
    input 'request_obj' is JSON request converted into a nested python object.
    '''

    metadata = {'user_name' : 'SomeRandomDude'} # add your own metadata to the request using key value pairs
    
    ''' inject user relevant metadata into the request if you want to, here.    
    e.g. Something like : 
    ... metadata = {'user_name' : some_database.query_user_name(request.get_user_id())}

    Then in the handler function you can do something like -
    ... return alexa.create_response('Hello there {}!'.format(request.metadata['user_name']))
    '''
    return alexa.route_request(request_obj, metadata)


@alexa.default_handler()
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request type """
    return alexa.create_response(message="Just ask")


@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    ''' Handler for LaunchRequest '''
    return alexa.create_response(message="Welcome to My Skill!")


@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!")


@alexa.intent_handler('RepeatEverythingIntent')
def repeat_intent_handler(request):

    query = request.slots["query"]

    return alexa.create_response(message='You said, "'+query+'"')


@alexa.intent_handler('HelloWorldIntent')
def helloworld_intent_handler(request):
    return alexa.create_response(message='Hello.')

@alexa.intent_handler('SchoolBuildingIntent')
def schoolbuilding_intent_handler(request):
    hallname=request.slots['hallname'].lower()
    if hallname=='gilman':
        answer='Gilman hall lies to the west of MSE Library, across the Keyser Quad.'
    elif hallname=='garland':
        answer='It is on the south of Levering Hall.'
    elif hallname=='krieger':
        answer='It is on the west of Brody Learning Commons.'
    elif hallname=='hodson':
        answer='It is on the west of Levering Hall and Garland Hall.'
    elif hallname=='levering':
        answer='It is on the south of Gilman Hall.'
    elif hallname=='mason':
        answer='It is right on the south gate.'
    elif hallname=='clark':
        answer='It is on the south of Hodson hall, nouthwest of Mason Hall.'
    return alexa.create_response(message=answer)

