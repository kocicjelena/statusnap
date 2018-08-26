# statusnap


snapcraft

(snapcraft prime, sudo snap try --devmode prime)

snapcraft 

sudo snap install stausnap_1_*.snap --dangerous

snapcraft push statusnap_1_amd64.snap --release=candidate

sudo snap install statusnap --channel=candidate

#snapcraft release <snap-name> <revision> <channel>

snapcraft release 1 stable

snap install docker

sudo docker run -v $(pwd):/statusnap snapcore/snapcraft sh -c "apt update && cd /statusnap ^& snapcraft"

sudo apt install ruby-dev
export GEM_HOME=$HOME/gems
export PATH=$PATH:$GEM_HOME/bin
gem install travis
~/.bashrc
travis login

snapcraft enable-ci travis

sudo: required
	services:
	- docker
	after_success:
	- openssl aes-256-cbc -K <travis-key> -iv <travis-iv>
  	  -in .snapcraft/travis_snapcraft.cfg
  	  -out .snapcraft/snapcraft.cfg -d
	deploy:
  	  skip_cleanup: true
    	  provider: script
  	  script: docker run -v $(pwd):$(pwd) -t snapcore:snapcraft sh -c
    	    "apt update -qq && cd $(pwd) &&
    	    snapcraft && snapcraft push *.snap --release edge"
  	  on:
    	    branch: master



	$ snapcraft enable-ci travis --refresh
  snap install statusnap-kocicjelena --edge
