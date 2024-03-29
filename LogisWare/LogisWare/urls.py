
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

from core import views as core_views
from users import views as users_view
from staffleave import views as staffleave_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [

    url('api/v1/', include("staffleave.urls")),

    url(r'app', staffleave_views.home, name='staff_leave'),

    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # SALES TEAM
    path('sales', core_views.sales_dashboard, name='dashboard_sales'),
    path('quotes', core_views.all_quotes_sales, name='all_quotes_sales'),
    path('quotes/add', core_views.add_quotes_sales, name='add_quotes_sales'),
    path('quotes/edit/<int:pk>', core_views.edit_quote, name='edit_quote'),
    path('quotes/insert', core_views.insert_quote, name='insert_quote'),
    path('quotes/items/<int:pk>', core_views.QuoteDetailView.as_view(),
         name='all_quotes_items_sales'),
    path('quotes/remove/<int:pk>/<int:qid>',
         core_views.delete_quote_item, name='remove_quotes_items_sales'),
    path('clients', core_views.ClientView.as_view(), name='my_clients_sales'),
    
    path('human/resource/clients', core_views.AllClientView.as_view(), name='all_clients'),


    path('quotes/modify/<int:pk>',
         core_views.edit_quote_apply, name='edit_quote_apply'),
    path('quotes/extend/eta/<int:pk>',
         core_views.extend_eta, name='extend_eta'),

    path('quotes', core_views.all_quotes_sales,
         name='total_quotes_sales'),
    path('quotes/done', core_views.done_deals_sales,
         name='done_deals_sales'),
    path('quotes/pending', core_views.pending_items_sales,
         name='pending_items_sales'),

    path('procurements/edit/<int:pk>', core_views.edit_quote, name='edit_quote_procurements'),
    path('procurements/unattended/quotes', core_views.unattended_quptes,
         name='unattended_quptes'),
    path('procurements/awaiting/quotes', core_views.awaiting_arrival_quotes,
         name='awaiting_arrival_quotes'),
    path('procurements/total/quotes', core_views.total_quotes_procurement,
         name='total_quotes_procurement'),
    path('procurements/today/quotes', core_views.today_quotes_procurement,
         name='today_quotes_procurement'),
    path('procurement', core_views.dashboard_procurement,
         name='dashboard_procurement'),
    path('procurement/quotes', core_views.all_quotes_procurement,
         name='all_quotes_procurement'),
    path('procurement/quote/status/<int:quote_pk>/<str:status_code>',
         core_views.update_quote_prodcurement, name='update_quote_procurement'),
    path('procurement/quote/add', core_views.add_quotes_sales,
         name='add_quotes_procurement'),
    path('procurement/quotes', core_views.all_quotes_sales,
         name='all_quotes_procurement'),
    path('procurement/users', core_views.users_dashboard_procurement, name='users_dashboard_procurement'),

    path('delivery', core_views.dashboard_delivery, name='dashboard_delivery'),

    path('delivery/days_deliveries/<str:date_string>',
         core_views.days_deliveries_procurement, name='days_deliveries_procurement'),
    path('delivery/days_deliveries/<str:date_string>',
         core_views.days_deliveries, name='days_deliveries'),
    path('delivery/awaiting_deliveries',
         core_views.awaiting_deliveries, name='awaiting_deliveries'),
    path('delivery/todays_deliveries',
         core_views.todays_deliveries, name='todays_deliveries'),
    path('delivery/not_delivered',
         core_views.not_delivered, name='not_delivered'),
    path('delivery/total_delivered',
         core_views.total_delivered, name='total_delivered'),

    path('delivery/deliveries', core_views.all_deliveries,
         name='all_deliveries'),

    path('delivery/quote/status/<int:quote_pk>/<str:status_code>',
         core_views.update_quote_delivery, name='update_quote_delivery'),
    path('delivery/quote/not_delivered',
         core_views.mark_items_not_delivered, name='mark_items_not_delivered'),
    path('users', core_views.users_dashboard, name='dashboard_delivery_users'),
    path('users/create', core_views.create_new_user, name='create_new_user'),
    path('users/deactivate/<int:pk>',
         core_views.deactivate_user, name='deactivate_user'),
    path('users/activate_user/<int:pk>',
         core_views.activate_user, name='activate_user'),



    path('admin/', admin.site.urls),

    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name="users/registrations/password_reset.html",
        email_template_name='users/email/password_reset_email.html',
        subject_template_name='users/email/password_reset_subject.txt',
        html_email_template_name='users/email/password_reset_email.html'
    ), name='password_reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name="users/registrations/password_reset_done.html",
    ), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="users/registrations/password_reset_confirm.html"), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="users/registrations/password_reset_complete.html"), name='password_reset_complete'),


    url(r'login_success/$', users_view.login_success, name='login_success'),
    path('login', auth_views.LoginView.as_view(
        template_name="users/registrations/login.html"), name='login'),

    path('logout', auth_views.LogoutView.as_view(
        template_name="users/registrations/login.html"), name='logout'),

    path("", core_views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
