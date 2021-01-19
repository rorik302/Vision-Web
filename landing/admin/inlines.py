from django.contrib.admin import TabularInline

from landing.models.block_models import ColumnBlock, RowBlock1, RowBlock2
from landing.models.element_models import Benefit, Card, NavbarMenuItem, Paragraph, Percent


class BaseInline(TabularInline):
    extra = 0
    show_change_link = True


class BenefitInline(BaseInline):
    model = Benefit


class CardInline(BaseInline):
    model = Card


class ColumnBlockInline(BaseInline):
    model = ColumnBlock


class MenuItemInline(BaseInline):
    model = NavbarMenuItem


class ParagraphInline(BaseInline):
    model = Paragraph


class PercentInline(BaseInline):
    model = Percent


class RowBlock1Inline(BaseInline):
    model = RowBlock1


class RowBlock2Inline(BaseInline):
    model = RowBlock2
