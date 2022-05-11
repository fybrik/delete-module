#!/usr/bin/env bash

set -x
set -e

# Notebook sample
kubectl create namespace fybrik-notebook-sample
kubectl config set-context --current --namespace=fybrik-notebook-sample

# localstack installation
helm repo add localstack-charts https://localstack.github.io/helm-charts
helm install localstack localstack-charts/localstack --set startServices="s3" --set service.type=ClusterIP
kubectl wait --for=condition=ready --all pod -n fybrik-notebook-sample --timeout=600s

kubectl port-forward svc/localstack 4566:4566 &

# Configure aws, add objects
export WORKING_DIR=/home/ravivs/delete-module/hack/test-script
export ACCESS_KEY=1234
export SECRET_KEY=1234
export ENDPOINT="http://127.0.0.1:4566"
export BUCKET="demo"
export OBJECT_KEY="PS_20174392719_1491204439457_log.csv"
export FILEPATH="$WORKING_DIR/PS_20174392719_1491204439457_log.csv"
aws configure set aws_access_key_id ${ACCESS_KEY} && aws configure set aws_secret_access_key ${SECRET_KEY} && aws --endpoint-url=${ENDPOINT} s3api create-bucket --bucket ${BUCKET} && aws --endpoint-url=${ENDPOINT} s3api put-object --bucket ${BUCKET} --key ${OBJECT_KEY} --body ${FILEPATH}

alias awsls="aws --endpoint-url=$ENDPOINT"

cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: paysim-csv
type: Opaque
stringData:
  access_key: "${ACCESS_KEY}"
  secret_key: "${SECRET_KEY}"
EOF