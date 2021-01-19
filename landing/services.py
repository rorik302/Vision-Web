from landing.models.landing_models import Landing


def get_landing():
    try:
        landing = Landing.objects.select_related(
            'header', 'header__hero', 'header__navbar',
            'header__navbar__menu', 'header__navbar__contact') \
            .prefetch_related(
            'rowblock1_set',
            'rowblock2_set',
            'columnblock_set',
        ).get()
    except Landing.DoesNotExist:
        raise ValueError('Нужно создать экземпляр лэндинга')

    return landing
