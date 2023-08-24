lint:
	find ./library -type f -name "*.py" | xargs pylint

clean_up:
	@echo "Removing old test results files!"
	rm ./results/*.html || true
	rm ./results/*.xml || true
	rm ./results/*.png || true
	rm *.html *.xml *.png || true

decrypt_staging:
	export KMS_KEY=projects/onec-stage/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-staging-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/stage.enc.yaml > ./data/stage.yaml

decrypt_prod:
	export KMS_KEY=projects/onec-prod/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-prod-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/prod.enc.yaml > ./data/prod.yaml

smoke_staging:
	pabot --processes 4 --testlevelsplit -i Smoke --logtitle Domino_Smoke_Staging --reporttitle Domino_Smoke_Staging \
	-l domino_smoke_staging_log.html -r domino_smoke_staging_report.html -o domino_smoke_staging_output.xml \
	--variable ENVFILE:../data/staging.yaml --pythonpath ./library tests/
#	robot -i Smoke --logtitle Domino_Smoke_Staging --reporttitle Domino_Smoke_Staging \
#	-l domino_smoke_staging_log.html -r domino_smoke_staging_report.html -o domino_smoke_staging_output.xml \
#	--variable ENVFILE:../data/staging.yaml --pythonpath ./library tests/
#	robot -i Smoke --variable ENVFILE:../data/staging.yaml --outputdir results -P ./library tests/

regression_staging:
	pabot --processes 4 --testlevelsplit -i Regression --logtitle Domino_Regression_Staging \
	--reporttitle Domino_Regression_Staging -l domino_regression_staging_log.html \
	-r domino_regression_staging_report.html -o domino_regression_staging_output.xml \
	--variable ENVFILE:../data/staging.yaml --pythonpath ./library tests/
#	robot -i Regression --logtitle Domino_Regression_Staging --reporttitle Domino_Regression_Staging \
#	-l domino_regression_staging_log.html -r domino_regression_staging_report.html \
#	-o domino_regression_staging_output.xml --variable ENVFILE:../data/staging.yaml --pythonpath ./library tests/
#	robot -i Regression --variable ENVFILE:../data/staging.yaml --outputdir results -P ./library tests/

smoke_prod:
	pabot --processes 4 --testlevelsplit -i Smoke --logtitle Domino_Smoke_Prod --reporttitle Domino_Smoke_Prod -l \
	domino_smoke_prod_log.html -r domino_smoke_prod_report.html -o domino_smoke_prod_output.xml \
	--variable ENVFILE:../data/prod.yaml --pythonpath ./library tests/
#	robot -i Smoke --logtitle Domino_Smoke_Prod --reporttitle Domino_Smoke_Prod -l domino_smoke_prod_log.html \
#	-r domino_smoke_prod_report.html -o domino_smoke_prod_output.xml --variable ENVFILE:../data/prod.yaml \
#	--pythonpath ./library tests
#	robot -i Smoke --variable ENVFILE:../data/prod.yaml --outputdir results -P ./library tests/

sanity_prod:
	pabot  --processes 4 --testlevelsplit -i Sanity --logtitle Domino_Sanity_Prod --reporttitle Domino_Sanity_Prod \
	-l domino_sanity_prod_log.html -r domino_sanity_prod_report.html -o domino_sanity_prod_output.xml \
	--variable ENVFILE:../data/prod.yaml --pythonpath ./library tests/
#	robot -i Sanity --logtitle Domino_Sanity_Prod --reporttitle Domino_Sanity_Prod -l domino_sanity_prod_log.html \
#	-r domino_sanity_prod_report.html -o domino_sanity_prod_output.xml --variable ENVFILE:../data/prod.yaml \
#	--pythonpath ./library tests
#	robot -i Sanity --variable ENVFILE:../data/prod.yaml --outputdir results -P ./library tests/
