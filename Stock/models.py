from django.db import models


class stock(models.Model):
    items = [('beds', 'מיטות'), ('bowls', 'קערות'), ('cups', 'כוסות'), ('snacks', 'חטיפים'), ('toys', 'צעצועים'),
             ('straps', 'רצועות'), ('sandbags', 'שקי חול'), ('collar', 'קולרים'), ('cleaning brushes', 'מברשות ניקוי'),
             ('dry dog food', 'מזון יבש לכלבים'), ('dry cat food', 'מזון יבש לחתולים'), ('fences', 'גדרות')]
    item = models.CharField(max_length=100, choices=items, verbose_name="פריט")  # the name of the item
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="כמות")  # the quantity of the item

    def __str__(self):
        return self.item
    class Meta:
        verbose_name_plural = "מלאי"