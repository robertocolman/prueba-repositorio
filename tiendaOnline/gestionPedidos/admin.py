from django.contrib import admin

from gestionPedidos.models import Cliente, Articulo, Pedido

class ClientesAdmin(admin.ModelAdmin):
	list_display=("nombre", "direccion", "telefono")
	search_fields=("nombre", "telefono")

class AriculosAdmin(admin.ModelAdmin):
	list_display=("nombre", "seccion", "precio")
	list_filter=['seccion']
	search_fields=("nombre", "seccion")

class PedidosAdmin(admin.ModelAdmin):
	list_display=("numero", "fecha", "entregado")
	list_filter=("fecha",)
	date_hierarchy="fecha"

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulo, AriculosAdmin)
admin.site.register(Pedido, PedidosAdmin)