from django.contrib import admin
from Project.models.chatRoom import ChatRoom
from Project.models.meeting import Meeting
from Project.models.message import Message
from Project.models.user import User
from Project.models.participant import Participant


admin.site.register(Meeting)
admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Participant)