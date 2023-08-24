#!/bin/bash
read -p "Please enter env to encrypt [staging,prod]:" env
if [ $env == 'staging' ]
then
  export KMS_KEY=projects/onec-stage/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-staging-cryptokey
  sops -e --gcp-kms $KMS_KEY data/staging.yaml > data/staging.enc.yaml
  echo "Encrypted files for $env"
fi


if [ $env == 'prod' ]
then
  export KMS_KEY=projects/onec-prod/locations/global/keyRings/sops-prod-keyring/cryptoKeys/sops-prod-cryptokey
  sops -e --gcp-kms $KMS_KEY data/prod.yaml > data/prod.enc.yaml
  echo "Encrypted files for $env"
fi