#!/bin/bash
DOKKU_HOST=ung.utt.fr
DOKKU_PROD=api.barcamps.uttnetgroup.fr

if [[ -n $encrypted_e378bde8517e_key ]] ; then
    # Set up ssh key
    openssl aes-256-cbc -K $encrypted_e378bde8517e_key -iv $encrypted_e378bde8517e_iv -in deploy_key.enc -out deploy_key -d
    chmod 600 deploy_key
    mv deploy_key ~/.ssh/id_rsa
    eval $(ssh-agent)
    ssh-add ~/.ssh/id_rsa
    # SSH config
    echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
    # Add dokku to known hosts
    ssh-keyscan -H $DOKKU_HOST >> ~/.ssh/known_hosts
    # Deploy
    git remote add dokku dokku@$DOKKU_HOST:$DOKKU_PROD
    git push dokku master -f
fi
