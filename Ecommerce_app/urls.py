from django.urls import path,include
from Ecommerce_app.views import*
from .import views

urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('reg',views.reg),
    path('login',views.login),
    path('admin_home',views.admin_home),
    path('add_admin_page',views.add_admin_page),
    path('login',views.login),
    path('cart',views.cart),
    path('about',views.about),
    path('contact',views.contact),
    path('detail/<int:id>',views.detail),
    path('profile',views.profile),
    path('online_payment_page',views.online_payment_page),
    path('order',views.order),
    path('feedback',views.feedback),
    path('contact_add',views.contact_add),
    path('search',views.search),
    path('add_item_page',views.add_item_page),

    path('show_users',views.show_users),
    
    path('seed',views.seed),
    path('fertilizer',views.fertilizer),
    path('veg',views.veg),

    path('edit_profile',views.edit_profile),
    path('save_profile/<int:id>',views.save_profile),

    path('demo',views.demo),
    path('bill',views.bill),
    path('html_to_pdf',views.html_to_pdf),
    path('add_to_cart',views.add_to_cart),
    path('delete_cart/<int:cid>',views.delete_cart),

    path('no_login/<int:id>',views.no_login),

    path('addonlinepayment',views.addonlinepayment),

   

    path('showItems',views.showItems),
    path('user_logout',views.user_logout),
    path('admin_logout',views.admin_logout),
    path('add_Admin',views.add_Admin),
    path('my_order',views.my_order),
    path('show_online',views.show_online),
    path('show_cod',views.show_cod),
    
    path('del_session',views.del_session),
    
    path('edit_admin/<int:id>',views.edit_admin),
    path('delete_admin/<int:id>',views.delete_admin),
    path('show_admin',views.show_admin),

    #ADD ITEM,DELETE,UPDATE
    path('add_item',views.add_item),
    path('showItems',views.showItems),
    # UPDATE DELETE ITEM URLS
    path('delete/<int:iid>',views.delete),
    path('update/<int:iid>',views.update),
    # EDIT ITEM URL
    path('edit/<int:iid>',views.edit), 

    #SEARCH
    path('product-list',views.productlistAjax), 

    #BUY ONLINE
    path('buy',views.buy), 
    path('send_mail_for_confirmation',views.send_mail_for_confirmation),
    path('send_mail_for_Payment_Attendance',views.send_mail_for_Payment_Attendance),



    # forgot password
    path('forgotpassword',views.forgotpassword,name='forgotpassword'), # forgot password page 
    path('forgotpassword_code',views.forgotpassword_code,name='forgotpassword_code'), # forgot password code
    path('otp_confirm',views.otp_confirm,name='otp_confirm'), # confirm otp page
    path('otp_confirm_code',views.otp_confirm_code,name='otp_confirm_code'), # confirm otp code
    path('new_password_code',views.new_password_code,name='new_password_code'), # new password code

]
