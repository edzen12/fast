from modeltranslation.translator import register, TranslationOptions
from apps.service.models import Service
from apps.social.models import Social
from apps.tarif.models import DataTarif, Tarif



@register(Service)
class ServiceTranslationOption(TranslationOptions):
    fields = ('title', )


@register(DataTarif)
class DataTarifTranslationOption(TranslationOptions):
    fields = ('name', )

@register(Social)
class SocialTranslationOption(TranslationOptions):
    fields = ('title', )

@register(Tarif)
class TarifTranslationOption(TranslationOptions):
    fields = ('name', 'price', 'cause_time')

