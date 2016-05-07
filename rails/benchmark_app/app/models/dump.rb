class Dump
  include Mongoid::Document
  field :name, type: String
  field :email, type: String
  field :location, type: String
end
