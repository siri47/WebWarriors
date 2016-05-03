class PersonController < ApplicationController
	before_filter	:authorize
  def new
    begin
      @info = Info.find_by(email: current_user.email)
    rescue Exception => e
      @info = nil
    end
    
  end

  def create
  	@info = Info.new info_params
    @info.email = current_user.email
  	if @info.save
  		flash[:success] = 'user info updated!'
  		@current_user = current_user
  		#redirect_to :controller => 'person', :action => 'new'
  		render 'new'
  	else
  		@info = nil
  	end
  end

  def get
  end

  private

  def info_params
  	params.require(:info).permit(:name, :ssn, :secret, :comments)
  end
end
