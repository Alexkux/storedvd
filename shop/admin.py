from django.contrib import admin

from shop.models import Section, Product, Discount, Order, OrderLine

admin.site.register(Section)
# admin.site.register(Product)
# admin.site.register(Discount)
# admin.site.register(Order)
# admin.site.register(OrderLine)


class ProductAdmin(admin.ModelAdmin): # Отображение таблицы с товарами
    list_display = ('title', 'section', 'image', 'price', 'date') # столбцы значений
    actions_on_bottom = True #Активация панели управления внизу
    # actions_on_top = False # Отключение панели вверху
    list_per_page = 10 #  Максимальное кол-во строк на странице
    search_fields = ('title', 'cast') #добавляет форму поиска по столбцам


class DiscountAdmin(admin.ModelAdmin): # таблица дисконта
    list_display = ('code', "value_percent") # столбцы значений

    def save_model(self, request, obj, form, change):
        ''' Функция для отслеживания действий с записями
        '''
        print('Request', request)
        print('Obj', obj)
        print('Form', form)
        print('Change', change)
        super(DiscountAdmin, self).save_model(request, obj, form, change)
        print('Request', request)
        print('Obj', obj)
        print('Form', form)
        print('Change', change)



@admin.register(Order) # Декоратор для регистрации модели, идентично admin.site.register(Order, OrderAdmin)
class OrderAdmin(admin.ModelAdmin): # отображение таблицы заказов
    list_display = (
        'id', 'display_products', 'display_amount',
        'name', 'discount', 'phone',
        'email', 'address', 'notice',
        'date_order', 'date_send', 'status'
    )
    fieldsets = ( # Создание разделов на странице
        ('Информация о заказе', {
            'fields': ('need_delivery', 'discount')
        }),
        ('Информация о клиенте', {
            'fields': ('name', 'phone', 'email', 'address'),
            'description': ('Контактная информация') # Описание блока
        }),
        ('Доставка и оплата', {
            'fields': ('date_send', 'status')
        }),
    )
    date_hierarchy = 'date_order' # фильтрация по дате


class OrderLineAdmin(admin.ModelAdmin): # таблица строк заказов
    list_display = ('order', 'product', 'price', 'count') # столбцы значений

admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(OrderLine, OrderLineAdmin)