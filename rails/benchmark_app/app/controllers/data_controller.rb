require 'mongo'

class DataController < ApplicationController
  def write
  	count = 10000
  	count = params[:count].to_i unless params[:count] == nil
  	@dumps = []	
  	@cnt = count
  	# compute count dump objects
  	count.times do |i|
  		params[:dump] = Dump.new
  		params[:dump][:name] = "morpheus"
  		params[:dump][:email] = "morpheus5249@gmail.com"
  		params[:dump][:location] = "New York City!"
  		@dumps.push(params[:dump])
  	end
  	# write each dump to the mongodb
  	@dumps.each do |dump|
  		if dump.save
  			@success = true
  		else
  			@success = false
  			return
  		end
  	end
  end

  def read
  	@dumps_from_db = []
  	db = Mongo::Client.new(['127.0.0.1:27017'], :database => 'benchmark_app_development')
  	coll = db[:dumps]
  	coll.find.each do |row|
  		@dumps_from_db.push(row.inspect)
  	end


  end

  private 

  # generate random strings
  def get_random (length)
  	chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
  	str = ''
  	length.times { str << chars[rand(chars.size)] }
  	str
  end


end
