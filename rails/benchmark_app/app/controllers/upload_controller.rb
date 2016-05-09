class UploadController < ApplicationController
  def newimage
    @var = "WELCOME TO UPLOAD IMAGE"
  end

  def upimage
    uploaded_io  = params[:picture]
    uploader = AttachmentUploader.new

    my_file = File.open(uploaded_io.path)
    uploader.store!(my_file)

    @image = name uploader.current_path.to_s
  end

  def newvideo
    @var = "WELCOME TO UPLOAD VIDEO"
  end

  def upvideo
    uploaded_io  = params[:video]
    uploader = AttachmentUploader.new

    my_file = File.open(uploaded_io.path)
    uploader.store!(my_file)

    @video = name uploader.current_path.to_s
  end

end
private
def name(filename)
  filename.split("/").last
end
