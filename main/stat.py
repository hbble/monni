from datetime import timedelta
from django.db.models import Sum
from django.utils import formats
from dateutil.relativedelta import relativedelta
from .models import InCategory, OutCategory, Income, Expense


class StatsData:
    '''Class calculates and provides data for charts'''

    @staticmethod
    def pie_exp_data(request):
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

    @staticmethod
    def line_data(request):
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
        labels = [formats.date_format(d, "M d") for d in dates]

        def daily_e_amount_sum(date_param):
            '''Daily expense amount sum'''
            value = Expense.objects.filter(
                user=request.user,
                date__year=date_param.year,
                date__month=date_param.month,
                date__day=date_param.day,
                ).aggregate(Sum('amount')).get('amount__sum')

            return value

        def daily_i_amount_sum(date_param):
            '''Daily income amount sum'''
            value = Income.objects.filter(
                user=request.user,
                date__year=date_param.year,
                date__month=date_param.month,
                date__day=date_param.day,
                ).aggregate(Sum('amount')).get('amount__sum')

            return value

        values_e = list(map(daily_e_amount_sum, dates))
        values_i = list(map(daily_i_amount_sum, dates))

        line_data = {
            "labels": labels,
            "values_e": values_e,
            "values_i": values_i,
            "max": max(x for x in values_e + values_i if x is not None),
        }

        return line_data

    @staticmethod
    def bar_data(request):
        '''Datasets for BarChart'''
        labels = []
        list_e = Expense.objects.filter(user=request.user,).order_by('date')

        min_d = list_e[0].date.date()
        max_d = list_e.reverse()[0].date.date()
        months = (max_d.year - min_d.year) * 12 + max_d.month - min_d.month

        dates = [min_d + relativedelta(months=x) for x in range(months + 1)]
        labels = [formats.date_format(d, "F") for d in dates]

        datasets = []
        categories = [c for c in OutCategory.objects.all()]
        #need to auto generate colors
        colors_bg = ['#007bff', '#dc3545', '#ffc107', '#53f442', '#ff5107', '#07ffee', '#07b4ff']
        colors_bd = ['#007bff', '#dc3545', '#ffc107', '#53f442', '#ff5107', '#07ffee', '#07b4ff']

        def amount_month_cat_sum(cat_param, date_param):
            '''Month expense amount sum by category'''
            value = Expense.objects.filter(
                user=request.user,
                category=cat_param,
                date__year=date_param.year,
                date__month=date_param.month,
                ).aggregate(Sum('amount')).get('amount__sum')

            if value is None:
                return 0
            return value

        all_data = []
        for cat, cl_bg, cl_bd in zip(categories, colors_bg, colors_bd):
            data = [amount_month_cat_sum(cat, d) for d in dates]
            all_data.extend(data)

            datasets.append({
                "label": cat.name,
                "backgroundColor": cl_bg,
                "borderColor": cl_bd,
                "borderWidth": 1,
                "data": data,
            })

        bar_data = {
            "datasets": datasets,
            "labels": labels,
            "max": max(all_data),
        }
        return bar_data

    # exp_data = Expense.objects.filter(
    #     user=request.user,
    #     date__lte=timezone.now(),
    #     date__gte=timezone.now() - timedelta(days=30),
    #     ).order_by('date')

    # inc_data = Income.objects.filter(
    #     user=request.user
    #     ).order_by('date')
