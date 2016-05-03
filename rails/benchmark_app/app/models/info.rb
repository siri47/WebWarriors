class Info
  include Mongoid::Document
  field :name, type: String
  field :ssn, type: String
  field :secret, type: String
  field :comments, type: String
  field :email, type: String
end
