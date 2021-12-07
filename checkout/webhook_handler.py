from django.http import HttpResponse


class StripeWH_Handler:
    """ Handler stripe webhooks """

    def__init__(self, request):
    self.request=request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event
        """
        return Handler(
            content=f'webkook received: {event["type"]}',
            status=200) 

