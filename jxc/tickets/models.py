from django.db import models
from customers.models import Customer
from products.models import ProductInfo


class ProductAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(ProductInfo, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=127)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=127)

    price = models.IntegerField()
    num = models.FloatField()

    class Meta:
        abstract = True


class ProductPurchaseAction(ProductAction):
    pass


class ProductSaleAction(ProductAction):
    pass


class TicketBasic(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket_name = models.CharField(max_length=127, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    total_money = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    discount = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)

    class Meta:
        abstract = True


# 进货单
class PurchaseTicket(TicketBasic):
    items = models.ManyToManyField(ProductPurchaseAction)


# 出货单
class SalesTicket(TicketBasic):
    items = models.ManyToManyField(ProductSaleAction)
