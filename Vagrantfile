# Load configuration file
require 'yaml'
dir = File.dirname(File.expand_path(__FILE__))
local = YAML.load_file("#{dir}/local/nodes.yml")

# Set Vagrant configuration
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'
Vagrant.require_version ">= 1.5.2"
Vagrant.configure("2") do |config|

  # Box definition
  config.vm.box = "landregistry/ubuntu"
  config.vm.box_check_update = true
  config.ssh.forward_agent = true
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'" # Fix TTY error

  # Set count for provisioning
  provision = 0

  # Node creation loop
  local['nodes'].each do |name, conf|
    config.vm.define name do |node|
      node.vm.hostname = name

      # Load Virtualbox modifications
      if conf['specifications'] != ''
        node.vm.provider :virtualbox do |vb|
          conf['specifications'].each do |key, value|
            if key != '' && value != ''
              vb.customize ["modifyvm", :id, "--#{key}", "--#{value}"]
            end
          end
        end
      end

      # Establish network addresses
      if conf['ip'] != ''
        node.vm.network :private_network,
        ip: conf['ip']
      else
        node.vm.network :private_network,
        type: dhcp
      end

      # Set up port forwarding
      if conf['port-forwarding'] != ''
        conf['port-forwarding'].each do |port|
          if port['guest'] != '' && port['host'] != ''
            node.vm.network :forwarded_port,
            guest: port['guest'].to_i,
            host: port['host'].to_i
          else
            puts "Cannot bind guest port #{port['guest']} to host port #{port['host']} as syntax is incorrect"
          end
        end
      end

      # Mount synced folders
      node.vm.synced_folder "local/.apt-cache", "/var/cache/apt/archives/"
      if conf['folders'] != ''
        conf['folders'].each do |folder|
          if folder['source'] != '' && folder['destination'] != ''
            node.vm.synced_folder folder['source'], folder['destination'],
              id: folder['id']
          else
            puts "Cannot mount #{folder['source']} to #{folder['destination']} as syntax is incorrect"
          end
        end
      end

      # Initialise provisioning from the last node to complete
      provision += 1
      if provision == local['nodes'].length
        node.vm.provision :shell,
           path: "local/vagrant.sh",
           privileged: true
      end

    end
  end
end
