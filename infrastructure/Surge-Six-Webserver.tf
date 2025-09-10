provider "aws" {
	region = "us-east-1"
}

# Setup EC2 instance

resource "aws_instance" "SurgeWebserv" {
	
	#Linux ami
	ami = "ami-00ca32bbc84273381"
	
	instance_type = "t2.micro"
	
	#Script that installs httpd on the instance
	user_data = file("${path.module}/installhttpd.sh")
	
	#Launch-Wizard-5 this allows ssh, https, and http. 
	vpc_security_group_ids = ["sg-037f498c0659e3f2a"]

	tags = {
	
	Name = "Surge-Webserver"

	}
}
