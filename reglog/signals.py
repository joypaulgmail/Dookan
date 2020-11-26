from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from reglog.models import delivard
from django.core.signals import request_finished
from django.dispatch import Signal,receiver
from django.core.signals import request_started,request_finished



"""
def postsave(sender,instance,**kwargs):
    print("it done")


def presave(sender,instance,**kwargs):
    print("presave")

def predelete(sender,instance,**kwargs):
    print("predlete")

def postdelete(sender,instance,**kwargs):
    print("postdelete")

post_save.connect(postsave,sender=delivard)
pre_save.connect(presave,sender=delivard)
pre_delete.connect(predelete,sender=delivard)
post_delete.connect(postdelete,sender=delivard)

"""



"""
@receiver(user_logged_in,sender=User)
def funs(sender,**kwargs):
    print("----------------------------")
    print("sender",sender)



@receiver(user_logged_out,sender=User)
def fun(sender,**kwargs):
    print("logged out")
"""




"""
@receiver(pre_save,sender=delivard)

def presave(sender,**kwargs):
    print(sender)
    print(kwargs)

@receiver(post_save,sender=delivard)
def postsave(sender,**kwargs):
    print("post save")

@receiver(post_delete,sender=delivard)
def postdelete(sender,**kwargs):
    print("post delete")

@receiver(pre_delete,sender=delivard)
def pretdelete(sender,**kwargs):
    print("pre delete")
@receiver(request_started)
def reqstarted(sender,**kwargs):
    print("************")
    print("request_started")
    print(sender)

@receiver(request_finished)
def reqfinished(sender,**kwargs):
    print("##########")
    print("request_finished")
"""
#CUSTOM SIGNAL

"""mysig=Signal(providing_args=["lis"])
@receiver(mysig)
def funse(sender,**kwargs):
    print("********CUSTOME SIGNAL")
    print("signal",sender)
    """

"""
mysign=Signal(providing_args=["india"])

@receiver(mysign,sender=delivard)
def funsd(sender,**kwargs):
    print("hello sir")"""
