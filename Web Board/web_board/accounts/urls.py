from django.urls import path
from .views import board,topic,board_topics,board_update,topic_update,topic_delete,board_delete,change_password,homepage,register_user,user,user_update,user_delete,user_login,user_logout

urlpatterns =[ 
    path('registerboard/',board),
    path('registertopic/',topic,name="newtopic"),
    path('board_topics/<int:id>',board_topics,name="board_topics"),   
    path('home/',homepage),  
    path('register/',register_user,name="signup"),
    path('user_login/',user_login,name="user_login"),
    path('logout/',user_logout,name="logout"),
    path('resetpassword/',change_password,name="password"),
    path('users/',user,name="users"),
    path('delete/<int:id>/',user_delete,name="delete"),
    path('update/<int:id>/',user_update,name="update"),
    path('updateboard/<int:id>/',board_update,name="updateboard"),
    path('deleteboard/<int:id>/',board_delete,name="deleteboard"),    
    path('updatetopic/<int:id>/',topic_update,name="updatetopic"),
    path('deletetopic/<int:id>/',topic_delete,name="deletetopic"),    
    ]