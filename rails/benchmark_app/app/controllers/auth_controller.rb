class AuthController < ApplicationController
  def new
  end

  def create
  	@user = User.new user_params
  	if @user.save
  		flash[:success] = "success: #{@user.user_name} has been signed up!"
  		redirect_to :controller => 'sessions', :action => 'new'
  	else
  		flash[:error] = 'error: could not signup!'
  		redirect_to :controller => 'auth', :action => 'new'
  	end
  end

  private

  def user_params
  	params.require(:user).permit(:user_name, :email, :password, :password_confirmation)
  end
end
