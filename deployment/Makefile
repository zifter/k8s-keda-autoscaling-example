cluster-create:
	$(info Create kind cluster)
	kind create cluster -v 1 --config kind-config.yaml

cluster-delete:
	$(info Delete kind cluster)
	kind delete cluster --name k8s-keda-autoscaling-example

cluster-deploy:
	$(info Deploy helmfile)
	helmfile sync --concurrency 1

print-urls:
	$(info ===========================================================)
	$(info Site: 			http://localhost:1080/)
	$(info Grafana: 		http://localhost:1080/grafana (admin - admin))
	$(info Prometheus: 		http://localhost:1080/prometheus)
	$(info ===========================================================)
