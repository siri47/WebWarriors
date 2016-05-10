require 'openssl'
require 'fileutils'

class UploadController < ApplicationController

    @@shared_key_size = 0x80
    @@shared_block_size = 16
    @@shared_key = OpenSSL::Random.random_bytes(@@shared_block_size)
    @@shared_iv = OpenSSL::Random.random_bytes(@@shared_block_size)

  @@tmp_path = "//tmp"

  def newimage
    @var = "WELCOME TO UPLOAD IMAGE"
  end

  def upimage
    uploaded_io  = params[:picture]
    uploader = AttachmentUploader.new

    my_file = File.open(uploaded_io.path)
    uploader.store!(my_file)
    @path = uploaded_io.path
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

  def serveimages
    img_path = "/home/ubuntu/software/WebWarriors/rails/benchmark_app/app/assets/images/mkdir.png"
    send_file img_path, type: 'image/png', disposition: 'inline'
  end

  def encrypt
      filename = "/home/ubuntu/software/WebWarriors/rails/benchmark_app/app/assets/images/mkdir.png"
      data = File.open(filename, "r") {|file| file.read() }
      count = 10000
      plain = nil
      count.times do |i|
        cipher = aes_encrypt(data, 1, "")
        plain = aes_decrypt(cipher, 1, "")
      end
      File.open("/home/ubuntu/software/WebWarriors/rails/benchmark_app/app/assets/images/op.png", "wb") {|file| file.write(plain) }
      @success = true
  end

  private


    # implement pkcs#7 padding for string class
    def pkcs7_pad(data, bsize = 16)
        size = data.bytes.length
        bself = data.bytes
        pad_size = bsize - (size % bsize)
        pad_size.times { bself.push(pad_size)}
        return bself.pack("C*")
    end

    # implement unpadding logic for the string class
    def pkcs7_unpad(data, bsize = 16)
        bself = data.bytes
        last = bself[-1]
        return bself[0..-last-1].pack("C*")
    end 
    
       # AES oracle that encrypts under ECB/CBC
    def aes_encrypt(plaintext, mode, key)
        if mode == 0
            cipher = OpenSSL::Cipher::AES.new(@@shared_key_size, :ECB)
            cipher.padding = 0
        else
            cipher = OpenSSL::Cipher.new('aes-128-cbc')
            cipher.iv = @@shared_iv
            padded_plaintext = pkcs7_pad(plaintext)
            cipher.padding = 0
        end
        cipher.encrypt
        cipher.key = @@shared_key 
        if key.length > 0
            cipher.key = key
        end
        return cipher.update(padded_plaintext) + cipher.final
    end

    # AES oracle that decrypts under ECB/CBC
    def aes_decrypt(ciphertext, mode, key)
        if mode == 0
            cipher = OpenSSL::Cipher::AES.new(@@shared_key_size, :ECB)
            cipher.padding = 0
        else
            cipher = OpenSSL::Cipher.new('aes-128-cbc')
            cipher.iv = @@shared_iv
            cipher.padding = 0
            #puts "dec length: #{ciphertext.length}"
        end
        cipher.decrypt
        cipher.key = @@shared_key
        if key.length > 0
            cipher.key = key
        end
        deciphered_text = cipher.update(ciphertext) + cipher.final
        #puts "dec: #{deciphered_text}"
        return pkcs7_unpad(deciphered_text)
    end


end
private
def name(filename)
  filename.split("/").last
end





