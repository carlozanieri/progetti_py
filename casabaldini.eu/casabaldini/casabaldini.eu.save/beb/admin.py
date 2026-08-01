from django.contrib import admin

# Register your models here.
from .models import Menuweb
#from .models import Blog
from .models import Entries
from .models import EntriesHome
from .models import Slider
from .models import Links

admin.site.register(Menuweb)
#admin.site.register(Blog)
admin.site.register(Entries)
admin.site.register(EntriesHome)
admin.site.register(Slider)
admin.site.register(Links)
