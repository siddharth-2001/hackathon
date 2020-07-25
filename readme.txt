######################################## Hackathon Submission ########################################
                                  by: Siddharth Bharmoria IT SG19845

I have tested each and every part of both the phases and everything seems to work. If you run into 
errors, you might be passing wrong primary keys.
Also due to the Heroku policies, it is possible that the database gets wiped out in 24 hours after deployment
because of the use of sqlite databse.

To make things easier I have added a check_dictionaries.txt file which contains sample dictionaries that can be used
to test the apis.

Some features use sending of primary keys over the links that were not originally specified in the hackathon pdf
these are:
     changePassword
     deleteUser
     deleteProduct

So to run them correctly you need to specify the id of the object you want to edit
like:
    changePassword/(id)
    deleteUser/(id)

Also the user product list displays the id of the products added
superuser account
username = siddh
password = password123


Working url routes:


path('platform/users', user_list_api, name = 'all-users'),
    path('platform/signup', user_create_api, name = 'sign-up'),
    path('platform/changePassword/<int:pk>', change_password_api, name= 'change-password' ),
    path('platform/login', login_user_api, name='login'),
    path('platform/deleteUser/<int:pk>', delete_user, name = 'delete-user'),
    path('platform/<int:pk>/products',view_product_list, name='list-products')


 path("platform/products", list_all_products, name='all-items' ),
    path("platform/products/create", create_product, name='create-item' ),
    path('platform/products/<int:pk>', view_product, name='view-product' ),
    path('platform/products/purchase', purchase_product, name='add-prod'),
    path('platform/products/review', add_review, name='add-review'),
    path('platform/products/<int:pk>/reviews', get_all_review, name='all-review'),
    path('platform/deleteProduct/<int:pk>', delete_product, name = 'del-product'),
    path('platform/products/rate', rate_product, name = 'rate'),

where substitue <int:pk> for orimary key or the id of the user or the product.