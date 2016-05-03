class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  def current_user
  	@current_user ||= User.find(session[:user_id]) if session[:user_id]
    @uname = @current_user.user_name
    return @current_user
  end
  helper_method :current_user
  helper_method :uname

  def authorize
  	redirect_to :controller => 'sessions', :action => 'new' unless current_user
  end
end