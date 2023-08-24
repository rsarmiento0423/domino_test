#!/bin/bash
read -p "Please enter env to decrypt [staging,prod]:" env

if [ $env == 'staging' ]
then
  export KMS_KEY=projects/onec-stage/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-staging-cryptokey
  sops -d --gcp-kms $KMS_KEY data/staging.enc.yaml > data/staging.yaml
  echo "Decrypted files for $env"
fi

if [ $env == 'prod' ]
then
  export KMS_KEY=projects/onec-prod/locations/global/keyRings/sops-prod-keyring/cryptoKeys/sops-prod-cryptokey
  sops -d --gcp-kms $KMS_KEY data/prod.enc.yaml > data/prod.yaml
  echo "Decrypted files for $env"
fi

