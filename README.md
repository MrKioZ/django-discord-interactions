# django-discord-interactions
A django reusable application for discord interactions

---

Quick start
-----------

1. Add "discord_interactions" to your INSTALLED_APPS setting like this::
```py
    INSTALLED_APPS = [
        ...
        'discord_interactions',
    ]
```
2. Include the polls URLconf in your project urls.py like this::

    path('api/', include('discord_interactions.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a discord interactions (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/api/interactions to participate in the poll.

---

### Settings.py
```python
DISCORD_INTERACTION_PUBLIC_KEY = ''
DISCORD_INTERACTION_APPLICATION_ID = ''
DISCORD_INTERACTION_BOT_TOKEN = ''
```

---

### Usage
```py
from discord_interactions.commands import GlobalCommands
from discord_interactions.variables import InteractionsResponse

@GlobalCommand(name="hello", description="Saying Hello World")
def hello(request):
    response = {
        "data": {
            "content": "Welcome to Master OF Art <a:moa_19:784732933050990592>"
        }
    }
    return InteractionResponse(**response)
```

---

## TODO
- [ ] Convert Application into reusable application
- [x] Implement Reusable functions
- [ ] Support Guild Command
- [ ] Support Multiple Applications at once
