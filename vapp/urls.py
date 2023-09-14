from django.urls import path
from vapp import views

urlpatterns=[
        path('mainpage/',views.mainpage,name="mainpage"),
        path('appointmentpage/',views.appointmentpage,name="appointmentpage"),
        path('saveappointment/',views.saveappointment,name="saveappointment"),
        path('about/',views.about,name="about"),
        path('service/',views.service,name="service"),
        path('department/',views.department,name="department"),
        path('singledepartment/<depname>',views.singledepartment,name="singledepartment"),
        path('doctor/',views.doctor,name="doctor"),
        path('singledoctor/<pro>',views.singledoctor,name="singledoctor"),
        path('contact/',views.contact,name="contact"),
        path('savecontact/',views.savecontact,name="savecontact"),
        # path('medicines/',views.medicines,name="medicines"),
        # path('singlemedicine/<medi>',views.singlemedicine,name="singlemedicine"),
        # path('cartmedicine/', views.cartmedicine, name="cartmedicine"),
         path('register/', views.register, name="register"),
         path('saveregister/', views.saveregister, name="saveregister"),
         path('login/', views.login, name="login"),
         path('userlogin/', views.userlogin, name="userlogin"),
         path('logout/', views.logout, name="logout"),
         path('bookservice/', views.bookservice, name="bookservice"),
         path('savebooking/', views.savebooking, name="savebooking"),
         path('profile/<pr>', views.profile, name="profile"),
         path('editprofile/<int:dataid>/', views.editprofile, name="editprofile"),
         path('updateprofile/<int:dataid>/', views.updateprofile, name="updateprofile"),
         path('history/', views.history, name="history"),
]
