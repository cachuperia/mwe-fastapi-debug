$script = <<-'SCRIPT'
sudo apt update
sudo apt install apt-transport-https curl gnupg-agent ca-certificates software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install containerd.io docker-buildx-plugin docker-ce docker-ce-cli docker-compose-plugin -y
sudo usermod -aG docker vagrant
sudo reboot
SCRIPT


Vagrant.configure("2") do |config|

  config.vm.define "focal64", primary: true do |c|
    c.vm.box = "ubuntu/focal64"
    config.vm.network "private_network", ip: "192.168.56.4"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 2
  end

   config.vm.provision "shell", inline: $script

end
