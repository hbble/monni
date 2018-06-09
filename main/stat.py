import functools
from datetime import timedelta
from django.db.models import Sum
from .models import InCategory, OutCategory, Income, Expense


class StatsData:
    '''Class calculates and provides data for charts'''

    def pie_exp_data(self, request):
        '''Data for PieChart'''
        pie_data = {}
        categories = [c.name for c in OutCategory.objects.all()]

        def amount_exp_cat_sum(cat):
            '''Expense category amount sum'''
            return Expense.objects.filter(
                user=request.user,
                category=OutCategory.objects.get(name=cat),
                ).aggregate(Sum('amount')).get('amount__sum')

        values = list(map(amount_exp_cat_sum, categories))

        pie_data = {
            "categories": categories,
            "values": values,
        }
        return pie_data

    #merge for exp and inc
    def line_data(self, request):
        '''Data for LineChart expenses'''
        line_data = {}

        list_e = Expense.objects.filter(user=request.user,).order_by('date')
        list_i = Income.objects.filter(user=request.user,).order_by('date')
        min_d = min([
            list_e[0].date.date(),
            list_i[0].date.date()
            ]) # .date() - converts datetime to date
        max_d = max([
            list_e.reverse()[0].date.date(),
            list_i.reverse()[0].date.date()
            ])

        dates = [min_d + timedelta(days=x) for x in range((max_d-min_d).days + 1)]
        labels = [d.strftime("%b %d") for d in dates] #strftime("%b") returns short name of month
        
        def amount_e_day_sum(date_param):
            '''Daily expense amount sum'''
            value = Expense.objects.filter(
                user=request.user,
                date__year=date_param.year,
                date__month=date_param.month,
                date__day=date_param.day,
                ).aggregate(Sum('amount')).get('amount__sum')
                
            if value is None:
                return 0
            return value

        def amount_i_day_sum(date_param):
            '''Daily income amount sum'''
            value = Income.objects.filter(
                user=request.user,
                date__year=date_param.year,
                date__month=date_param.month,
                date__day=date_param.day,
                ).aggregate(Sum('amount')).get('amount__sum')
            
            if value is None:
                return 0
            return value

        values_e = list(map(amount_e_day_sum, dates))
        values_i = list(map(amount_i_day_sum, dates))

        line_data = {
            "labels": labels,
            "values_e": values_e,
            "values_i": values_i,
            "max": max(values_e + values_i),
        }

        return line_data



    # exp_data = Expense.objects.filter(
    #     user=request.user,
    #     date__lte=timezone.now(),
    #     date__gte=timezone.now() - timedelta(days=30),
    #     ).order_by('date')
    
    # inc_data = Income.objects.filter(
    #     user=request.user
    #     ).order_by('date')

