from django.apps import AppConfig

class RulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.rules'         # <-- caminho completo do módulo
    label = 'rules'                # ⚠️ usa 'rules' (não 'doccano_rules')
