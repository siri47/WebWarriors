class ImagesController < ApplicationController
  def index
  end

  def new
  end

  def create
  	@image = Image.new(image_params)
  	if @image.save
  		redirect_to :action => :show, :id => @image.id
  end
end

  def show
  	@id = params[:id]
  	@image = Image.find(@id)
  end

  def showall
    @images = Image.all
  end

private
  def image_params
    params.require(:image).permit(:image)
  end
end