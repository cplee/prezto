orgname = ENV['ORGNAME'] 
current_dir = File.dirname(__FILE__)
user = ENV['OPSCODE_USER'] || ENV['USER'] || ENV['USERNAME']
home_dir = ENV['HOME'] || ENV['HOMEPATH']
node_name                user.downcase
client_key               "#{home_dir}/.chef/#{user}.pem"
validation_client_name   "#{orgname}-validator"
validation_key           "#{home_dir}/.chef/#{orgname}-validator.pem"
cache_type               'BasicFile'
cache_options( :path => "#{home_dir}/.chef/checksums" )
cookbook_path            ["#{current_dir}/../cookbooks"]
cookbook_license "apachev2"
cookbook_email "cplee@nektos.com"
log_level                :info
log_location             STDOUT
ssl_verify_mode :verify_peer

knife[:use_sudo]= true

knife[:region] = "us-west-2"

