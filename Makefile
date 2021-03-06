generate-grpc:
	python -m grpc_tools.protoc -I app/api/grpc --python_out=app/api/grpc --grpc_python_out=app/api/grpc app/api/grpc/interface.proto

fmt:
	black . -l 120

check-fmt:
	black . -l 120 --check

mypy:
	cd app && mypy ./.. --ignore-missing-imports

tests:
	cd app && nose2 -v
