Rails.application.routes.draw do
  #get 'person/new'

  #get 'person/create'

  #get 'person/get'

  #get 'person/new'

  #get 'person/create'

  #get 'person/get'
  get 'images/index'

  get 'images/new'

  get 'images/show'

  post 'images/create'

  get 'images/showall'

  #get 'sessions/new'

  #get 'sessions/create'

  #get 'sessions/logout'

  #get 'auth/new'

  #get 'auth/create'

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  get 'signup' => 'auth#new'
  post 'users' => 'auth#create'

  get 'signin' => 'sessions#new'
  post 'login' => 'sessions#create'
  get 'logout' => 'sessions#logout'

  get 'userinfo' => 'person#new'
  post 'userdata' => 'person#create'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end