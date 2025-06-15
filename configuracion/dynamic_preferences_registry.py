# myapp/preferences.py
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import BooleanPreference, StringPreference, IntegerPreference
from dynamic_preferences.preferences import Section

homepage = Section('configuracion')

@global_preferences_registry.register
class ShowHomeBanner(BooleanPreference):
    section = homepage
    name = 'show_home_banner'
    default = True
    verbose_name = "Mostrar banner en página de inicio"

@global_preferences_registry.register
class WelcomeDiscountEnabled(BooleanPreference):
    section = homepage
    name = 'welcome_discount'
    default = False
    verbose_name = "Activar descuento para usuarios nuevos"
