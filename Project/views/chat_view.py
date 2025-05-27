from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Project.models.chatRoom import ChatRoom
from Project.models.message import Message
from Project.forms.chat_form import ChatRoomForm, MessageForm

@login_required
def chat_list(request):
    rooms = ChatRoom.objects.filter(participants=request.user)
    return render(request, 'chat_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, pk=room_id)
    if request.user not in room.participants.all():
        return redirect('chat_list')

    messages = Message.objects.filter(room=room).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.sender = request.user
            message.save()
            return redirect('chat_room', room_id=room.id)
    else:
        form = MessageForm()

    return render(request, 'chat_room.html', {
        'room': room,
        'messages': messages,
        'form': form
    })

@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.participants.add(request.user)
            return redirect('chat_room', room_id=room.id)
    else:
        form = ChatRoomForm()

    return render(request, 'create_chat.html', {'form': form})
