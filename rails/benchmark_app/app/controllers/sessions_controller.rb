class SessionsController < ApplicationController
  def new
  end

  def create
  	@user = User.find_by(email: params[:email])
  	if @user and @user.authenticate(params[:password])
  		session[:user_id] = @user.id
  		flash[:success] = "login successful!"
  		redirect_to :controller => 'person', :action => 'new'
  		#render 'new'
  	else
  		flash[:error] = 'login failed!'
  		#redirect_to :controller => 'sessions', :action => 'new'
  		render 'new'
  	end
  end

  def logout
  	session[:user_id] = nil
  	flash[:success] = 'logout successful!'
  	redirect_to :controller => 'sessions', :action => 'new'
  end
end
