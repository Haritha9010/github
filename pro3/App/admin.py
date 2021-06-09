from django.contrib import admin
from App.models import User,Worker,Category,Product,Customise,Cart,Myorders

# Register your models here.
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customise)
admin.site.register(Cart)
admin.site.register(Myorders)

